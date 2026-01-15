#!/bin/bash

# Configure Colours.
BLUE_COLOUR='\e[36m'
WHITE_COLOUR='\e[0m'

# Set script echo header.
HEADER="[${BLUE_COLOUR}AUTO KBL${WHITE_COLOUR}]"

CONFIG_LIST=~/.config/autoKBL.list
LOG_DIR=~/.temp

# Log the message to the logfile.
log()
{
	# Read takes the input from stdin so that we can use this function in a pipeline.
	read -t 0.01 MESSAGE

	# If the message is not empty, log it to the file.
	if [ ! -z "$MESSAGE" ]; then
		echo  "$MESSAGE" >> ~/.temp/autoKBL
	fi
}

# Log the message to the terminal / console
logc()
{
	if [[ $(id -u) -ne "0" ]]; then
		# Using read for the same reason as for the log function.
		read -t 0.01 MESSAGE
		# Prefix the formatted header.
		echo -e "$HEADER $MESSAGE"
	fi
}

# If the log file doesn't yet exist, create it. Then write the current timestamp to it.
if [ ! -f "${LOG_DIR}/autoKBL" ]; then
	touch "${LOG_DIR}/autoKBL"
	echo "$(date '+%F_%H:%M:%S')" | log
else
	echo "$(date '+%F_%H:%M:%S')" | log
fi

# If the config file is missing, exit.
if [ ! -f ~/.config/autoKBL.list ];then
	echo -e "Config list file '$CONFIG_LIST' is missing." | tee >(log) | logc
	exit 1
else
	# If the config file is empty, exit. Otherwise read the config file into an array.
	if [ $(wc -l < "${CONFIG_LIST}" | cut -d ' ' -f 1 ) -eq "0" ]; then
		echo -e "Config file empty." | tee >(log) | logc
		exit 1
	else
		mapfile -t configList < ${CONFIG_LIST}
	fi
fi

# Initialise a counter to display an appropriate summary after the run.
DEVICE_COUNT=0

# Loop through the array of config items.
for line in "${configList[@]}"; do

	# Extract the layout and keyboard name from the config list item.
	LAYOUT=$(echo ${line} | cut -d '|' -f 1)
	KEYBOARD_NAME=$(echo ${line} | cut -d '|' -f 2)

	# Find the device ID of the keyboard. Log any erros by redirecting stderr
	DEVICE_ID=$(xinput list --id-only "keyboard:""$KEYBOARD_NAME" 2> >(log))

	# Check if a device ID was found.
	if [ ! -z "$DEVICE_ID" ]; then
		echo -e "$KEYBOARD_NAME detected with device ID $DEVICE_ID." | log

		# Increment counter.
		((DEVICE_COUNT++))

		# Set the keyboard layout.
		setxkbmap -device "$DEVICE_ID" -layout "$LAYOUT"

		# Report the success or failure of the command. Exit on failure.
		if [ $? -eq 0 ]; then
			echo -e "$KEYBOARD_NAME (id=$DEVICE_ID) layout set to $LAYOUT." | tee >(log) | logc
		else
			echo -e "Failed to modify keyboard layout for $KEYBOARD_NAME." | tee >(log) | logc
			exit 1
		fi
	fi
done

# Report summary of run.
if [ "$DEVICE_COUNT" -eq "0" ];then
	echo -e "No configured devices detected." | tee >(log) | logc
else
	echo -e "$DEVICE_COUNT device(s) setup." | tee >(log) | logc
fi
