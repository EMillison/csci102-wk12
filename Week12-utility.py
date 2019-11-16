# INSERT GITHUB REPOSITORY HEREEEEEEEEEEEEEEEEEEEEE
# Emily Millison
# CSCI 102 - Section A
# Week 12 - Part A

#PrintOutput:
def PrintOutput(input_str):
    print("OUTPUT", input_str)

#LoadFile:
#Return a list that is the length of the number of lines of the file and where each element is a string that is the text in that line
def LoadFile(filename):
    file = open(filename, "r+")
    file_list = file.readlines()

    new_list = []
    for i in range(len(file_list)):
        stringi = file_list[i].replace('\n', '')
        new_list.append(stringi)
    return new_list

#UpdateString:
#Take in two strings and an index. Prints a string where the first stringn is modified by replacing the character at the index with the second string
def UpdateString(string1, string2, index):
    string1_list = list(string1) #list function from here https://stackoverflow.com/questions/4978787/how-to-split-a-string-into-array-of-characters/29225966
    string1_list[index] = string2

    string3 = ''
    for i in range(len(string1_list)):
        string3 += string1_list[i]
    print("OUTPUT", string3)

#FindWordCount:
#find the amount of times that string1 appears in list 1
def FindWordCount(list1, string1):
    counter = 0
    for word in list1:
        if word == string1:
            counter += 1
        else:
            pass
    return counter

#ScoreFinder:
#Given a list of names, scores, and a certain player name, find the player name in the list, and find their corresponding score in the second list (it will be at the same index)
def ScoreFinder(player_names_list, player_scores_list, player_name):
    player_names_list2 = []
    for i in range(len(player_names_list)):
        new_name = player_names_list[i].lower()
        player_names_list2.append(new_name)
    if player_name.lower() in player_names_list2:
        player_index = player_names_list2.index(player_name.lower())
        player_score = player_scores_list[player_index]
        output_str = 'OUTPUT ' + player_names_list[player_index] + ' got a score of ' + str(player_score)
        print(output_str)
    else:
        error_string = "OUTPUT player not found"
        print(error_string)

#Union:
#Takes in two lists and returns a single list that is the union of the two lists (no duplicates between 2 lists)
def Union(list1, list2):
    union_list = []
    for i in range(len(list1)):
        union_list.append(list1[i])
    for j in range(len(list2)):
        if list2[j] not in union_list:
            union_list.append(list2[j])
    return union_list
    
