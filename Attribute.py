class Attribute:
    def __init__(self, aname, neg, attr_num):
        self.name = aname
        self.negation = neg
        self.attr_num = attr_num

    def assignments(attr):
        attributes = []
        itter = int(len(attr))
        pos = 1
        for i in range(int(itter/2) + 2):
            if (i % 2 != 0): continue
            attributes.append(Attribute(attr[i], attr[i+1], pos))
            pos = pos + 1

        rev_attr = attr[::-1]
        neg = -(int(itter/2))
        for k in range(int(itter/2) + 2):
            if k % 2 != 0: continue
            attributes.append(Attribute(rev_attr[k], rev_attr[k+1], neg))
            neg = neg + 1

        return attributes
    
    def get_num(attributes, name):
        for attribute in attributes:
            if attribute.name == name:
                return attribute.attr_num
    
    def generate_combinations(pairs):
        all_combinations = []
        
        def generate_recursive(current_combination, remaining_pairs):
            if not remaining_pairs:#-----------------------------------base case
                all_combinations.append(current_combination)
                return
            
            first_pair = remaining_pairs[0]

            for item in first_pair:
                generate_recursive(current_combination + [item], remaining_pairs[1:])

        generate_recursive([], pairs)

        return all_combinations
        
    