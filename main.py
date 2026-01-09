import sys 


def readstudent_file(path):

    file_path = 'students.txt'

    try: 
        with open(file_path, 'r') as file: ## r for read mode , using open function to open student
            file_content = file.read() ##just reads the file, need this im pretty sure

            print("File Content:\n",file_content)
    except FileNotFoundError:
        print(f"{file_path} not found or doesnt exist")

readstudent_file('students.txt')
