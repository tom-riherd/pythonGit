# **************************************************************
# *  P Y T H O N    S T R I N G    M A N I P U L A T I O N     *
# **************************************************************
#  string_manipulation.py program
#  Tom Riherd, last modified 12/04/2021
#
import os.path

# Set location of sales data (use "data/students.txt" for Macs)
file_path = "data/students.txt"

# Create an empty names list
names = []
students = []


def load_names():
    '''
    Loads the student list from a file.
    file_path is where the file is to be found.
    Raises a file exception if the load fails.
    '''
    print("Load the students from:", file_path)
    # Clear the names list
    names.clear()
    try:
        #Open the file for input
        with open(file_path, "r") as input_file :
            for line in input_file:
                line = line.strip()
                # remove the grade level and the tab from string
                stop_at = line.rfind("\t")
                line = line[0:stop_at]
                names.append(line)
        # remove the header row
        del names[0]
    except: 
        print("A problem occurred reading file", file_path)  


# Print the names
def print_names():
    '''
    Prints the names of the students
    '''
    # Print a heading
    print("\n* * * *   S T U D E N T   N A M E S   * * * *\n")
    # Initialize the counter
    count = 1
    #Print out the list of students
    for name in names:
        print("Student #", count, "is", name)
        count += 1

def fix_names():
    '''
    Puts student names in Last, First M. format
    Removes grade from name
    Sorts the list alphabetically
    Changes to correct case for names
    Prints the name list
    '''
    students.clear
    global names
    # Print a heading
    print("\n* * * *   O R D E R E D   N A M E S   * * * *\n")
    # Initialize the counter
    count = 1
    #Print out the list of students
    for x in range(len(names)):
        student = names[x]
        start_last = student.rfind(" ") + 1
        last_name = student[start_last:len(student)]
        first_name = student[0:start_last - 1]
        student = last_name + ", " + first_name
        student = student.title()
        print("Index #", x, "is", student)
        students.append(student)
        count += 1



# * * * *   M A I N    P R O G R A M  * * * *
load_names()
print(names)
print_names()
names.sort()  # SORTS THE NAMES AND RE-ORDERS THE LIST
print(names)
fix_names()
students.sort()
print(students)