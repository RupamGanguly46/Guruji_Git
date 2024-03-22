def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(' or char == '*':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                # Replace the matching open parenthesis with an asterisk
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '(':
                        stack[i] = '*'
                        break
                else:
                    return False
    # Check if there are any open parentheses left
    open_parentheses = [char for char in stack if char == '(']
    return len(open_parentheses) <= stack.count('*')

# Test the function
test_strings = [
    "*)"
]

for test_string in test_strings:
    if is_balanced(test_string):
        print(f"{test_string}: Balanced")
    else:
        print(f"{test_string}: Not Balanced")
