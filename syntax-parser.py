def ComandList(text):
    Operations = ['+', '-', '*', '/', '%', '**', '<', '>', '==', '!=', '<=', '>=', '=', '++', '--']
    Words = ['let', 'var', 'alert', 'if', 'else if', 'else', 'while', 'do', 'for', 'return']
    Separators = [' ', 's', ';', '{', '}', '[', ']', '(', ')']
    Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Dict = {}
    a = 1
    b = 1
    c = 1
    d = 1
    e = 1
    for i in Operations:
        Dict[i] = "O" + str(a)
        a += 1
    for i in Words:
        Dict[i] = "W" + str(b)
        b += 1
    for i in Separators:
        Dict[i] = "R" + str(c)
        c += 1
    for i in Digits:
        Dict[i] = "D" + str(d)
        d += 1
    for i in text:
        if not(i in Dict):
            Dict[i] = "I" + str(e)
            e += 1
    Endlist = []
    for i in text:
        if(i in Dict):
            Endlist.append(Dict[i])
    return Endlist

text = "if ( a > b ) a ++ 1 else b ++"
text = text.split()
print(ComandList(text))

