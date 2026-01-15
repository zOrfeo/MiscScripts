import os
import sys
from timeit import default_timer as timer

# Get the current size of the terminal, this is used later to format the results into columns.
columns, rows = os.get_terminal_size(0)

# Read in the parm file, and store each parameter in a newly constructed dictionary. In case of error, report & exit.
parms={}
try:
	with open("conf.conf","r") as file:
		for line in file:
			key, value = line.strip().split("=")
			parms[key] = value

except FileNotFoundError:
	print("AnagramSolver: Couldn't find config file")
	sys.exit()

except Exception:
	print("AnagramSolver: An error occurred reading config file")
	sys.exit()
	
# Check if the required paramters have been set, if any are missing then report & exit.
if 'anagramWords' not in parms:
	print("AnagramSolver: wordFile parameter missing from config file.")
	sys.exit()
	
# Define initial list to hold the words to be read from the wordFile.
wordList = []

# Read the wordFile and save each word as a list of characters. In case of error, report & exit.
try:
	with open(parms['anagramWords'], 'r', encoding='UTF-8') as file:
		while line := file.readline():
			wordList.append(line.rstrip().lower())

	print("AnagramSolver: Imported",parms['anagramWords'])
	
except FileNotFoundError:
	print("AnagramSolver: Couldn't find wordFile",parms['anagramWords'])
	sys.exit()

except Exception:
	print("AnagramSolver: An error occurred reading wordFile",parms['anagramWords'])
	sys.exit()
	
# Count how many words have been imported & display the count.
wordList_Count = len(wordList)
print("AnagramSolver:",wordList_Count, "words in the input file")

anagram = [list(input("AnagramSolver: Anagram    => ")),0,""]
anagram_length = len(anagram[0])
lengthFilteredWordList = []

for word in wordList:
	if len(word) == anagram_length:
		lengthFilteredWordList.append(word)

try:
	lengthFilteredWordList.remove("".join(anagram[0]))
except:
	pass 

lengthFilteredWordList_Count = len(lengthFilteredWordList)

# stamps = tomato
letterScores2 = {'a':1,
				'b':2,
				'c':4,
				'd':8,
				'e':16,
				'f':32,
				'g':64,
				'h':128,
				'i':256,
				'j':512,
				'k':1024,
				'l':2048,
				'm':4096,
				'n':8192,
				'o':16384,
				'p':32768,
				'q':65536,
				'r':131072,
				's':262144,
				't':524288,
				'u':1048576,
				'v':2097152,
				'w':4194304,
				'x':8388608,
				'y':16777216,
				'z':33554432}

letterScores3 ={'a':1,
				'b':3,
				'c':9,
				'd':27,
				'e':81,
				'f':243,
				'g':729,
				'h':2187,
				'i':6561,
				'j':19683,
				'k':59049,
				'l':177147,
				'm':531441,
				'n':1594323,
				'o':4782969,
				'p':14348907,
				'q':43046721,
				'r':129140163,
				's':387420489,
				't':1162261467,
				'u':3486784401,
				'v':10460353203,
				'w':31381059609,
				'x':94143178827,
				'y':282429536481,
				'z':847288609443}

time1 = timer()
for j in range(anagram_length):
	anagram[1] = anagram[1] + letterScores3[anagram[0][j]]

anagramList = []
for i in range(lengthFilteredWordList_Count):
	letters = list(lengthFilteredWordList[i])
	score = 0
	for j in range (anagram_length):
		try:
			score = score + letterScores3[letters[j]]
		except:
			score = 0

	if score == anagram[1]:
		anagramList.append(lengthFilteredWordList[i])

time2 = timer()
print("AnagramSolver: Numeric method \033[3m(took",str(round(((time2-time1)*1000),0))[:-2],"ms)\033[0m:")
if len(anagramList) == 0:
	print("AnagramSolver: Answers    => \033[3mNo answers found.\033[0m")
else:
    print("AnagramSolver: Answers    =>", ", ".join(anagramList))

time3 = timer()
anagramList2 = []
anagram[2] = anagram[0]
anagram[2].sort()
alphaSortedAnagram = "".join(anagram[2])
for i in range(lengthFilteredWordList_Count):
	letters = list(lengthFilteredWordList[i])
	letters.sort()
	if "".join(letters) == alphaSortedAnagram:
		anagramList2.append(lengthFilteredWordList[i])
		
time4 = timer()

print("AnagramSolver: Letters method \033[3m(took",str(round(((time4-time3)*1000),0))[:-2],"ms)\033[0m:")
if len(anagramList2) == 0:
	print("AnagramSolver: Answers    => \033[3mNo answers found.\033[0m")
else:
    print("AnagramSolver: Answers    =>", ", ".join(anagramList2))