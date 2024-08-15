from Attribute import Attribute
from Logic_help import *
from tabulate import tabulate
import random
def penalty(attributes, attr_pairs, constraints):
    print("You have chosen Penalty Logic \n")


    preference_file = input("Please enter the Preferences File Name: ")

    preferences = prefer_parse(preference_file)
    
    #get the penalty sentences and penalty associated with it
    logic_penalty = []
    penalty_applied = []

    for preference in preferences:
        parts = preference.split(', ')
        logic_penalty.append(parts[0])
        penalty_applied.append(parts[1])

    combos = Attribute.generate_combinations(attr_pairs) #get all combinations posstible with the given attributes
    coms = combos[::-1]
    combo_nums = translate_to_nums(combos, attributes) #translate cominations to numerical equivalents and reverse them so all negations is first combo
    feas_combos = get_feas_combos(combo_nums, constraints) #get the feasible combos once the constraints are applied 
    preferences_to_pass = prefer_translate(logic_penalty, attributes) #translate preferences to numerical equivalent statements 
    table_coord = penalty_check(feas_combos, preferences_to_pass, penalty_applied) #calculate the penalties of each object when compared with each constraint 
    #create a list of all objects with their penalties and totals 
    key_list = []
    for key, value in table_coord.items():
        total = 0
        for val in value:
            total = total + int(val)
        row = [combo_nums.index(list(key))]
        row.extend(value)
        row.append(total)
        key_list.append(row)
    
    print()


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
            if int(choice) == 1: #--------------------------------------------------encoding
                for co in coms:
                    print('Object', coms.index(co), ' - ' + ', '.join(co))
                print()

            elif int(choice) == 2: #------------------------------------------------feasibility checking

                if len(feas_combos) != 0:
                    print("Yes, the total number of feasible objects is: ", int(len(feas_combos)))
                else:
                    print("No, there are no feasible objects")
                print()

            elif int(choice) == 3: #------------------------------------------------print the table
                headers = preferences
                headers.insert(0, "Objects")
                headers.insert(len(headers), "Total")

                print(tabulate(key_list, headers=headers, tablefmt='grid'))
                print()


                
            elif int(choice) == 4:#-------------------------------------------------select two random objects and state their preference when compared
                random_objects = random.sample(key_list, 2)
                object = random_objects[0][0]
                object2 = random_objects[1][0]

                
                if random_objects[0][len(random_objects[0]) - 1] < random_objects[1][len(random_objects[1]) - 1]:
                    print('Object', object, " is strictly better than Object ", object2)

                elif random_objects[0][len(random_objects[0]) - 1] > random_objects[1][len(random_objects[1]) - 1]:
                    
                    print('Object', object2, " is strictly better than Object ", object)

                else:
                    
                    print('Object', object2, " is equivalent to Object ", object)
                print()

            elif int(choice) == 5:#-------------------------------------------------Output the optimal ovjects if there are any
                sorted_list = sorted(key_list, key = lambda x : x[len(x) - 1])
                optimal = []
                for i in range(len(sorted_list) - 1):
                    s = sorted_list[i]
                    next_s = sorted_list[i + 1]

                    if s[-1] < next_s[-1]:
                        if s[0] not in optimal:
                            optimal.append(s[0])
                        print("Optimal object(s):", end = ' ')
                        print(*optimal, sep = ', ')
                        break

                    elif s[-1] == next_s[-1]:
                        if s[0] not in optimal:
                            optimal.append(s[0])
                        optimal.append(next_s[0])

                if len(optimal) == len(sorted_list):
                    print("All objects are equal, no optimal exists.\n")
                print()

            elif int(choice) == 6:#-------------------------------------------------back to logic choice menu
                print("Returning to preference logic menu. \n")
                break
            else:
                print("That is not a valid menu option, please select an option of 1 to 6.\n")
        except ValueError as exce:
            print("That is not a valid menu option, please select an option of 1 to 6.\n")
            continue