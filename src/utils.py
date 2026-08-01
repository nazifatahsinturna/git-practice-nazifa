def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Both a and b must be numbers"
    return a+b

def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Both a and b must be numbers"
    return a-b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Both a and b must be numbers"
    return a*b