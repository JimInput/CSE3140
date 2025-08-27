import os

files = os.listdir()

python_files = []

if __name__ == '__main__':
    for file in files:
        if file.endswith('.py'):
            python_files.append(file)
            
    with open("Q1A.out", "w") as file:
        for py_file in python_files:
            file.write(py_file + "\n")
