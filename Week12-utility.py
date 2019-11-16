# INSERT GITHUB REPOSITORY HEREEEEEEEEEEEEEEEEEEEEE
# Emily Millison
# CSCI 102 - Section A
# Week 12 - Part A

#PrintOutput:
def PrintOutput(input_str):
    print("OUTPUT", input_str)

#LoadFile:
def LoadFile(filename):
    file = open(filename, "r+")
    file_list = file.readlines()

    new_list = []
    for i in range(len(file_list)):
        stringi = file_list[i].replace('\n', '')
        new_list.append(stringi)
    return new_list

