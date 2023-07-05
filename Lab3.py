def rpn_to_infix(expression):
    operations = {"=", "+=", "-=", "*=", "+", "-", "*", "/", "**"}
    stack = []
    infix = []
    func = 0
    ifka = 0
    cic = 0
    totalcic = 0
    totalifka = 0
    for token in expression.split():
        if token.isalnum() and not 'АЭМ' in token and not 'Ф' in token and not 'УПЛ' in token and not 'БП' in token and not 'МЦ' in token:
            if not "М" in token:
                stack.append(token)
        elif 'АЭМ' in token:
            r = int(token[0])
            arr = []
            newarr = []
            while r != 0:
                arr.append(stack.pop())
                r -= 1
            arr = arr[::-1]
            for i in range(len(arr)):
                if i == 0:
                    newarr.append(arr[i])
                    newarr.append('[')
                else:
                    newarr.append(arr[i])
                    if i + 1 < len(arr):
                        newarr.append(',')
            newarr.append(']')
            stack.append(''.join(newarr))

        elif 'Ф' in token:
            func = 1
            r = int(token[0])
            arr = []
            newarr = []
            while r != 0:
                arr.append(stack.pop())
                r -= 1
            arr = arr[::-1]
            for i in range(len(arr)):
                if i == 0:
                    newarr.append(arr[i])
                    newarr.append('(')
                else:
                    newarr.append(arr[i])
                    if i + 1 < len(arr):
                        newarr.append(',')
            newarr.append(')')
            stack.append(''.join(newarr))
        elif token == 'УПЛ':
            infix = list("if " + infix[0] + ":\n    ")
            ifka = 1
            totalifka = 1
        elif 'БП' in token:
            infix.append("\nelse:\n    ")
            ifka = 1
        elif 'МЦ1УПЛ' in token:
            infix.append("while " + infix.pop() + ":\n    ")
            cic = 1
            totalcic = 1
        elif len(stack) != 0:
            if len(stack) == 1:
                infix.append(stack.pop())
                break
            else:
                b = stack.pop()
                a = stack.pop()
                op = " ".join([a, token, b])
            if func == 1:
                infix.append(op)
                func -= 1
            elif ifka == 1:
                stack.append(op)
                ifka = 0
            elif cic == 1:
                infix.append(op)
                cic = 0
            else:
                infix.append("(" + op + ")")
            if token in operations and totalifka == 0:
                infix.append('\n')
            if token in operations and totalcic == 1:
                infix.append('    ')
    infix = ''.join(infix)
    if not 'Ф' in expression:
        infix = infix.replace("(", "")
        infix = infix.replace(")", "")

    return infix
#print(rpn_to_infix("s i j 3АЭМ 10 += "))
#print(rpn_to_infix("y f x y 3Ф = "))
#print(rpn_to_infix("a b > М1 УПЛ a x y - = "))
#print(rpn_to_infix("a b > М1 УПЛ a x y - += M2БП М1: a b += М2:"))
#print(rpn_to_infix("a 10 = b 20 = a b < МЦ1УПЛ b 5 -= a 1 += МЦ1:"))

