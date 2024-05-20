# Initial program code, which uses nonlocals
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
    
    subset = []
    total = init
    
    max_amt = 0
    max_path = []
    
    def getPermutations():
        nonlocal total
        nonlocal max_amt
        nonlocal max_path
        
        if (len(nodes) <= 0):
            permutations.append(subset.copy())
            
            if total > max_amt:
                max_amt = total
                max_path = subset.copy()
            
            return
        
        for _ in range(len(nodes)):
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
                    return
                
            if (total > 0):
                getPermutations()
            
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
            
    getPermutations()
    return (permutations, max_amt, max_path)

# _, max_amt, max_path = calculate(5832, [Node(">", 1152), Node(">", 1332), Node("/", 2), Node("/", 3)])
# print(max_amt, max_path)