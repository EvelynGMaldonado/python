'''
Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt". 
Each text file contains three rows with one word per row. 
Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line. 
Output the new file contents.

The solution output should be in the format
    word1
    word2
    word3 
    sentence

Sample Input/Output:
    If the input is
        WordTextFile1.txt
    
    then the expected output is
        cat
        chases
        dog
        cat chases dog

*
Input to program: 
WordTextFile1.txt
*

'''

#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence

# EASY WAY REQUESTED IN THE PREASSESMENT
file = open(file_name, "r")
for row in file:
    rows = row.rstrip()
    concat_list_of_rows.append(rows)
#print(concat_list_of_rows)

all_rows_sentence = " ".join(concat_list_of_rows)
#print(all_rows_sentence)

file.close()

#print(concat_list_of_rows)
#print(all_rows_sentence)


file = open(file_name, "a")
file.write(f"\n{all_rows_sentence}")
file.close()

file = open(file_name, "r")
print(file.read())
file.close()



# ****MORE COMPLETE, USING MAIN() AND ADDITIONAL FUNCTIONS****
import errno  #it got authomatically imported so I don't know if is needed - need to check!


def main():
    file_name = str(input("Please enter the file name: "))
    path_to_file = "C:/Users/Evelyn/Code/python/test"
    file_content = ["Word1 \n", "Word2 \n", "Word3 \n"]

    file_exists(file_name, path_to_file, file_content)

def file_exists(file_name, path_to_file, file_content):
    try:
        file = open(f"{path_to_file}/{file_name}", "r")
        file.read()
        #print(file.tell())
        file_size = file.tell()

        file.close()

        #is_empty(file_size, file_content, path_to_file, file_name)
        has_content(file_size, path_to_file, file_name)

        return file_size

    except FileNotFoundError:
        create_file(path_to_file, file_name, file_content)

def has_content(file_size, path_to_file, file_name):
    if file_size >= 1:
        print("file exists already and size >= 1")
        file = open(f"{path_to_file}/{file_name}", "r")
        existent_rows = file.read()
        print(existent_rows)
        file.close()

    else:
        print("something is wrong and file is 0 characters ~ empty")


def create_file(path_to_file, file_name, file_content):
    #"w" write only --> creates a file if the file does not exist
    file = open(f"{path_to_file}/{file_name}", "w")
    #file.writelines(file_content)
    file.close()

    file_size_check(path_to_file, file_name, file_content)

def file_size_check(path_to_file, file_name, file_content):
    file = open(f"{path_to_file}/{file_name}", "r")
    file.read()
    print(file.tell())
    file_size = file.tell()

    file.close()

    is_empty(file_size, path_to_file, file_name, file_content)

    return file_size


def is_empty(file_size, path_to_file, file_name, file_content):
    if file_size == 0:
        print("exception and file_empty")
        file = open(f"{path_to_file}/{file_name}", "w")
        file.writelines(file_content)
        file.close()

        file_size_check(path_to_file, file_name, file_content)

    else:
        print("exception and file is not empty")
        file_iteration(path_to_file, file_name)

    

def file_iteration(path_to_file, file_name):
    print_concatenated_rows(path_to_file, file_name)
    print_single_rows(path_to_file, file_name)

def print_single_rows(path_to_file, file_name):
    file = open(f"{path_to_file}/{file_name}", "r")
    single_rows = file.read()
    print(single_rows)
    file.close()

def print_concatenated_rows(path_to_file, file_name):
    file = open(f"{path_to_file}/{file_name}", "r")
    
    single_line_of_lines = []
    for line in file:
        lines = line.rstrip()
        single_line_of_lines.append(lines)
    #print(single_line_of_lines)
    line_of_lines_string = " ".join(single_line_of_lines)
    #print(line_of_lines_string)
    result(line_of_lines_string, path_to_file, file_name)

def result(line_of_lines_string, path_to_file, file_name):
    file = open(f"{path_to_file}/{file_name}", "a")
    file.write(line_of_lines_string)
    file.close()





    #check if the file exist -function
        #yes 
            #file_size_check call function
            #is the file empty -function?
                #yes -->  call enter the desired text -function
                #no --> call the file_iteration -function
        # no --> 
            # create the file -function
            #call is the file empty -function

    #file_iteration -function **********************
        #print single rows -function
        #get rid of trailing newline characters at the end of the line
        #store the file data by rows, in a list of strings called rows_list 
            # rows_list= [""]
        #join the list with each item/row separated by comma in a variable called row_string 
            #row_string = " ".join()
        #print concatenated rows

        #enter desited text -function

main()    

