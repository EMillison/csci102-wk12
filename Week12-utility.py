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

#UpdateString:
def UpdateString(string1, string2, index):
    string1_list = list(string1) #list function from here https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters/29225966
    print(string1_list)
    string1_list[index] = string2

    string3 = ''
    for i in range(len(string1_list)):
        string3 += string1_list[i]
    return string3
    
