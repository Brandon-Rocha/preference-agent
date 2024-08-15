from Attribute import Attribute

#parse to get preference sentences
def prefer_parse(preference_file):
    try:
        with open(preference_file, "r") as cf:
            preferences = []
            for line in cf:
                line = line.strip()
                preferences.append(line)
    except FileNotFoundError as exce:
        print("Wrong file name, please enter a valid file name to continue.")
        return
    
    return preferences

#translate preferences to sentences in the form attr# disjunction/conjunction attr#
def prefer_translate(logic_penalty, attributes):
    negation = False
    pass_logic = []
    temp_logic = []
    for log in logic_penalty:
        words = log.split(' ')
        temp_logic = []
        for word in words:
            if word == 'NOT':
                negation = True
                continue
            elif word == 'OR':
                temp_logic.append('disjunction')
                continue
            elif word == 'AND':
                temp_logic.append('conjunction')
                continue
            else:
                if negation == True:
                    cnf_num = Attribute.get_num(attributes, word) * -1
                    temp_logic.append(cnf_num)
                    negation = False
                else:
                    cnf_num = Attribute.get_num(attributes, word)
                    temp_logic.append(cnf_num)
        pass_logic.append(temp_logic)
    return pass_logic

#get list of feasible combinations given the attributes tranlated to number equivalents and the constraints
def get_feas_combos(combo_nums, constraints):
    feasible_combos = []
    for num in combo_nums:
        for constraint in constraints:
            for k in range(len(num)):
                if num[k] == constraint[0] or num[k] == constraint[1]:
                    feasible_combos.append(num)
                    break
    return feasible_combos

#translate all combinations to their number equivalents 
def translate_to_nums(combinations, attributes):
    combo_nums = []
    for combination in combinations:
        combo_temps = []
        for i in range(len(combination)):
            combo_temps.append(Attribute.get_num(attributes, combination[i]))
        combo_nums.append(combo_temps)
    combo_nums = combo_nums[::-1]
    return combo_nums

#paree constraint file and return the constraints in number pairs i.e, (-1,2)
def con_parse(constraint_file, attributes):
    #parse constaint file
    with open(constraint_file, "r") as cf:
        constraints = []
        for line in cf:
            line = line.strip()
            constraints.append(line)

    negation = False
    cnf_nums = []
    negation = False
    for constraint in constraints:
        words = constraint.split(' ')
        for word in words:
            if word == 'NOT':
                negation = True
                continue
            elif word == 'OR' or word == 'AND':
                continue
            else:
                if negation == True:
                    cnf_num = Attribute.get_num(attributes, word) * -1
                    negation = False
                else:
                    cnf_num = Attribute.get_num(attributes, word)
            cnf_nums.append(cnf_num)

    pair_list = [(cnf_nums[i], cnf_nums[i+1]) for i in range(0, len(cnf_nums), 2)]
    return pair_list

#parse attribute file to get list of all attributes
def attribute_parse(attribute_file):
    attr = []
    with open(attribute_file, "r") as af:
        for line in af:
            items = line.strip().split(': ')[1].split(', ')
            attr.extend(items)
    return attr

#get all attributes in pair format to assign negations
def get_pairs(attribute_file):
    pairs = []
    with open(attribute_file, 'r') as af2:
        for line in af2:
            pair = line.strip().split(': ')[1].split(', ')
            pairs.append(pair)
    return pairs


def choice_translate(choices, attr, attributes):
    choices_to_pass = []
    for choice in choices:
        choice_nums = []
        words = choice.split(' ')
        for word in words:
            if word in attr:
                cnf_num = Attribute.get_num(attributes, word)
                choice_nums.append(cnf_num)
            elif word == 'BT' or word == 'IF':
                choice_nums.append(word)
        choices_to_pass.append(choice_nums)
    return choices_to_pass

#check and assign feasible combinations with a penalty
def penalty_check(feasible_combinations, preference_to_pass, penalty_applied):
    preference_penalties = {tuple(combo): combo for combo in feasible_combinations}
    penalty = -1

    for combo in feasible_combinations:
        penalties = []
        for preference in preference_to_pass:
            for c in combo:
                if 'disjunction' in preference:
                    if preference[0] in combo or preference[2] in combo:
                        penalty = 0
                        break
                    else:
                        penalty = penalty_applied[preference_to_pass.index(preference)]
                elif 'conjunction' in preference:
                    if preference[0] in combo and preference[2] in combo:
                        penalty = 0
                    else:
                        penalty = penalty_applied[preference_to_pass.index(preference)]
            penalties.append(penalty)
        preference_penalties[tuple(combo)] = penalties
    return preference_penalties

def get_ranking(choices_to_pass, feas_combos):
    rankings = {tuple(combo): combo for combo in feas_combos}
    for combo in feas_combos:
        rank = []
        for choice in choices_to_pass:
            if choice.index('IF') == len(choice) - 1:#-----------no condition
                for ch in choice:
                    if ch in combo:#----------------------if it falls into a group
                        group = (choice.index(ch) / 2) + 1
                        break
                    else:#--------------------------------------does not fall into a group
                        group = float('infinity')
            else:#--------------------------------------------------condition must be met
                if choice[len(choice) - 1] in combo:#-----condition met
                    for ch in choice:
                        if ch in combo:#----------------------if it falls into a group
                            group = (choice.index(ch) / 2) + 1
                            break
                        else:#--------------------------------------does not fall into a group
                            group = float('infinity')
                else:#-----------------------------------------------condition not met
                    group = float('infinity')
            rank.append(group)
        rankings[tuple(combo)] = rank
    return rankings
                    


