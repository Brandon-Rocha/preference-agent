from Attribute import Attribute
from Logic_help import *
from tabulate import tabulate
import random
def qual_choice(attributes, attr_pairs, constraints, attr):
    print("You have chosen Qualitative Choice Logic \n")
    preference = input("Please enter the Preferences File Name: ")
    print()
    choices = prefer_parse(preference) #separate choices into lines
    choices_to_pass = choice_translate(choices, attr, attributes)



    combos = Attribute.generate_combinations(attr_pairs) #get all combinations posstible with the given attributes
    coms = combos[::-1]
    combo_nums = translate_to_nums(combos, attributes) #translate cominations to numerical equivalents and reverse them so all negations is first combo
    feas_combos = get_feas_combos(combo_nums, constraints) #get the feasible combos once the constraints are applied
    rankings = get_ranking(choices_to_pass, feas_combos) 

    table_nums = []
    for key, value in rankings.items():
        row = [combo_nums.index(list(key))]
        row.extend(value)
        table_nums.append(row)
    
    while True:

        print('Choose the reasoning task to perform : \n',
        '1. Encoding \n',
        '2. Feasability \n',
        '3. Show the Table \n',
        '4. Exemplification \n',
        '5. Omni-optimization \n',
        '6. Back to previous menu\n')
        
        choice = input("You Chose: ")
        print()
        try:
            if int(choice) == 1:#------------------------------------------print combinations 
                for co in coms:
                    print('Object', coms.index(co), ' - ' + ', '.join(co))
                print()

            elif int(choice) == 2:#----------------------------------------feasible objects
                if len(feas_combos) != 0:
                    print("Yes, the total number of feasible objects is: ", int(len(feas_combos)))
                else:
                    print("No, there are no feasible objects")
                print()

            elif int(choice) == 3:#----------------------------------------show the table
                headers = choices
                headers.insert(0, "Objects")

                print(tabulate(table_nums, headers=headers, tablefmt='grid'))
                print()

            elif int(choice) == 4:#----------------------------------------rank two random objects
                random_objects = random.sample(table_nums, 2)
                rank1 = random_objects[0]
                rank2 = random_objects[1]
                
                # Compare the rankings
                if all(r1 <= r2 for r1, r2 in zip(rank1[1:], rank2[1:])):
                    print(f"{random_objects[0][0]} is strictly preferred over {random_objects[1][0]}")  # item1 is not strictly better than item2
                elif all(r1 == r2 for r1, r2 in zip(rank1[1:], rank2[1:])):  # item1 is strictly better than item2
                    print(f"{random_objects[0]} and {random_objects[1]} are equivalent")
                elif all(r1 >= r2 for r1, r2 in zip(rank1[1:], rank2[1:])):
                    print(f"{random_objects[1][0]} is strictly preferred over {random_objects[0][0]}") 
                else:  # One or both items are not in the rankings dictionary
                    print(f"{random_objects[0][0]} and {random_objects[1][0]} are incomparable")
                print()

            elif int(choice) == 5:#----------------------------------------find all optimal objects
                items_to_delete = []
                optimal = table_nums[:]
                for item1 in table_nums:
                    for item2 in table_nums:
                        if item1 != item2:  # Ensure items are different
                            if all(r1 <= r2 for r1, r2 in zip(item1[1:], item2[1:])):
                                items_to_delete.append(item2)
                            elif all(r1 == r2 for r1, r2 in zip(item1[1:], item2[1:])):
                                continue
                            elif all(r1 >= r2 for r1, r2 in zip(item1[1:], item2[1:])):
                                items_to_delete.append(item1)

                # Remove items from optimal
                for item in items_to_delete:
                    if item in optimal: 
                        optimal.remove(item)
                print("All optimal Objects: ", end = ' ')
                for o in optimal:
                    print(o[0], end = ', ')
                print()
                print()
                
            elif int(choice) == 6:
                print("Returning to preference logic menu. \n")
                break
            else:
                print("That is not a valid menu option, please select an option of 1, 2, or 3.\n")
        except ValueError as exce:
            print("That is not a valid menu option, please select an option of 1, 2, or 3.\n")
            continue