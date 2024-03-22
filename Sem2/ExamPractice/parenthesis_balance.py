def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':             #if open bracket, append to stack
            stack.append(char)
        elif char == ')':           #if close bracket
            if not stack:           #if stack is empty, so no open bracket, then what are we closing. False
                return False
            current = stack.pop()   #innermost open bracket must get closed first (stack works on lifo)
            if ( char == ')' and current != '(' ): #we can use \ for continuing code in next line
                return False
    return len(stack) == 0          #check if all open brackets are closed, no one is left

# Test the function
test_strings = [
    "()",
    "()()",
    "(())",
    ")()(",
    "()(",
]

for test_string in test_strings:
    if is_balanced(test_string):
        print(f"{test_string}: Balanced")
    else:
        print(f"{test_string}: Not Balanced")
