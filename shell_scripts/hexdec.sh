# Convert Hex <=> Decimal

while getopts "h:d:" arg; do
	case ${arg} in
		h)
		  toConvert=$OPTARG
		  tfmt=H
		  ;;
		d)
		  toConvert=$OPTARG
		  tfmt=D
		  ;;
	esac
done

shift $((OPTIND - 1))

# If no option was used, take the remaining argument
if [[ -z $toConvert && $# -gt 0 ]]; then
    toConvert=$1
    tfmt=D
fi

if [ "$tfmt" = "D" ]; then
	if [[ ! $toConvert =~ ^[0-9A-Fa-f]+$ ]]; then
		printf "Invalid Hexadecimal provided."
		exit 1
	fi
	
	printf "%d\n" $(( 16#$toConvert ))
fi

if [ "$tfmt" = "H" ]; then
	if [[ ! $toConvert =~ ^[0-9]+$ ]]; then
		printf "Invalid Decimal provided."
		exit 1
 	fi

	printf "%X\n" "$toConvert"
fi
