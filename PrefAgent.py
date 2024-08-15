from Penalty import penalty
from ChoiceLogic import qual_choice
from Attribute import Attribute
from Logic_help import *

print("Welcome to Preference Agent\n")

attribute_file = input("Enter Attributes File Name: ")
constraint_file = input("Enter Hard Contraints File Name: ")
print()
print('!!!!! Take input for files, hard code only for testing')


#parse attribute file
attr = attribute_parse(attribute_file)
pairs_of_att = get_pairs(attribute_file)

#assign attributes along with their negation 
attributes = Attribute.assignments(attr)
pair_con_list = con_parse(constraint_file, attributes)

while True:

    print("Choose which preference logic to use: \n 1. Penalty Logic \n 2. Qualitative Choice Logic \n 3. Quit \n")
    choice = input('You Chose: ')
    print() 

    try:
        if int(choice) == 1:
            #go to penalty logic
            penalty(attributes, pairs_of_att, pair_con_list)
        elif int(choice) == 2:
            #go to choice logic
            qual_choice(attributes, pairs_of_att, pair_con_list, attr)
        elif int(choice) == 3:
            print("You have chose to quit, goodbye. \n")
            break
        else:
            print("That is not a valid menu option, please select an option of 1, 2, or 3.\n")
    except ValueError as exce:
        print("That is not a valid menu option, please select an option of 1, 2, or 3.\n")
        continue