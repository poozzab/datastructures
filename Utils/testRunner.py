import sys
from termcolor import colored

infoKeywords = ["man","info","help","h","-h"]

descMsg = "Runs a line by line comparison of two provided files with an option for verbose and quiet. Writes to results.txt"
expUseErrorMsg = "Expected use: python testRunner.py [v] act <filename> exp <filename>"
helpMsg = "Include flag 'v' to always print the value of actual and expected, q to omit correct lines"


actFileName = ""
expFileName = ""
resultsFileName = "results.txt"
verbose = False
quiet = False

for i in range(0,len(sys.argv)):
    if sys.argv[i] in infoKeywords:
        print(descMsg)
        print(expUseErrorMsg)
        print(helpMsg)
        exit()
    elif sys.argv[i] == 'q':
        quiet = True
    elif sys.argv[i] == 'v':
        verbose = True
    elif sys.argv[i] == 'act' and i+1 < len(sys.argv):
        actFileName = sys.argv[i+1]
    elif sys.argv[i] == 'exp' and i+1 < len(sys.argv):
        expFileName = sys.argv[i+1]

if actFileName is "" or expFileName is "":
    print(expUseErrorMsg)
    print( "Was provided: " + str(sys.argv))
    exit()

numErrors = 0
lineNum = 1
with open(actFileName,"r") as actualFile:
    with open(expFileName,"r") as expectedFile:
        with open(resultsFileName,"w") as results:
            for actLine in actualFile:
                expLine = expectedFile.readline()
                if actLine.rstrip('\n') == expLine.rstrip('\n'):
                    if verbose:
                        results.write(str(lineNum) + " equal; actual '{}' expected '{}'\n".format(actLine.rstrip('\n'),expLine.rstrip('\n')))
                    elif not quiet:
                        results.write(str(lineNum) + " equal\n")
                else:
                    numErrors+=1
                    results.write(str(lineNum) + " error: actual '{}' expected '{}'\n".format(actLine.rstrip('\n'), expLine.rstrip('\n')))
                lineNum += 1

if numErrors > 0:
    print(colored("There were {0}/{1} ({2:.5}%) errors".format(numErrors,lineNum-1,numErrors/(lineNum-1)*100),"red"))
else:
    print(colored("Test Passed","green"))