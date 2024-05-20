class Node:
    def __init__(self, op, val):
        self.op = op # + - * / >
        self.val = val
    
    def __repr__(self):
        return f"{self.op} {self.val}"
    
    def __str__(self):
        return f"{self.op} {self.val}"

def calculate(init, nodes):
    permutations = []
    
    def getPermutations(total, subset):
        if (len(nodes) <= 0):
            permutations.append(subset.copy())
            return (total, subset.copy())
        
        max_amt = 0
        max_path = []
        
        for i in range(len(nodes)):
            curr = nodes.pop(0)
            subset.append(curr)
            
            # perform op
            if (curr.op == "+"):
                total += curr.val
            elif (curr.op == "-"):
                total -= curr.val
            elif (curr.op == "*"):
                total *= curr.val
            elif (curr.op == "/"):
                total = total // curr.val
            elif (curr.op == ">"):
                if (total > curr.val):
                    total += curr.val
                else:
                    subset.pop()
                    nodes.append(curr)
                    return (0, [])
                
            if (total > 0):
                amt, path = getPermutations(total, subset)
                
                if (amt > max_amt):
                    max_amt = amt
                    max_path = path
                    
            
            # reverse op
            if (curr.op == "+"):
                total -= curr.val
            elif (curr.op == "-"):
                total += curr.val
            elif (curr.op == "*"):
                total = total // curr.val
            elif (curr.op == "/"):
                total *= curr.val
            elif (curr.op == ">"):
                total -= curr.val
            
            subset.pop()
            nodes.append(curr)
        
        return (max_amt, max_path)
            
    max_amt, max_path = getPermutations(init, [])
    return (permutations, max_amt, max_path)

# _, max_amt, max_path = calculate(5832, [Node(">", 1152), Node(">", 1332), Node("/", 2), Node("/", 3)])
# print(max_amt, max_path)