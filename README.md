# Incremental Build Method
# Emily Millison
# CSCI 102 - Section A
# Week 12 - Part A

1. PrintOutput function:
	Copied from 10B Lab. Used function definition and pritn function.
2. LoadFile function:
	Used the basic open() file syntax and used a for loop to remove all of the newline characters.
3. UpdateString function:
	Used the list() function to make a list of characters of the first string. Then created
	a new string where the second string was put in at the ideal index. Joined the list 
	back into a string using a for loop and addition.
4. FindWordCount funtion:
	Used a for loop to loop through list1 and then if the the string was the same as that 
	list element, increase the word counter by 1
5. ScoreFinder function:
	Used a for loop to make all of the characters lowercase in the player list so that there would
	not be problems when checking for equality. Then if the player name was in the player list,
	I found the index, and then used that to find the player's score as it was the same index
	but in the score list. If the player was not in the player list, I used an else to print the
	error message.
6. Union function:
	I used a for loop to add all elements of the first list to a new list. Then I used a second
	for list to add elements to the new list only if they were not already in this new (union)
	list.
7. Intersection function:
	I used a nested for loop to go through both lists, and if an element in list1 was also in
	list2, I added it to a new list of intersections and returned this list
8. NotIn function:
	Used a for loop to loop through the first list, and if the element of that list was not
	in the other list, then I added it to a "not_in" list which kept track of these values.