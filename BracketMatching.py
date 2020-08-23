def Match(values) -> bool:
    stack = []
    mapping = {
        "(":")",
        "[":"]",
        "{":"}"
    }

    for i in range(0, len(values)):
        if(values[i] in ["(", "[","{"]):
            stack.append(values[i])
        else:
            test = stack.pop()
            if values[i] != mapping.get(test):
                return False
    
    if len(stack) == 0:
        return True

    return False


if __name__ == "__main__":
    tests = ["()[]{}","[{)]","([{}])" ]
    for i in tests:
        print(Match(i))