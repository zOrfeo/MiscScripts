# Convert Hex <=> Decimal

while getopts "hHdD" arg; do
	case ${arg} in
		h)	tfmt=H;;
		H)	tfmt=H;;
		d)  tfmt=D;;
		D)	tfmt=D;;
	esac
done

shift $((OPTIND - 1))

if [[ -p /dev/stdin ]]; then
	toConvert=$(</dev/stdin)
fi

if [[ -z $toConvert && $# -gt 0 ]]; then
    toConvert=$1
fi

if [[ -z $toConvert ]]; then
	echo "No Input Provided"
	exit 1
fi

if [[ -z $tfmt ]]; then
    tfmt=D
fi

if [ "$tfmt" = "D" ]; then
	if [[ ! $toConvert =~ ^[0-9A-Fa-f]+$ ]]; then
		printf "Invalid Hexadecimal provided: {"$toConvert"}"
		exit 1
	fi
	
	printf "%d\n" $(( 16#$toConvert ))
fi

if [ "$tfmt" = "H" ]; then
	if [[ ! $toConvert =~ ^[0-9]+$ ]]; then
		printf "Invalid Decimal provided: {"$toConvert"}"
		exit 1
 	fi

	printf "%X\n" "$toConvert"
fi
