def js_to_rpn(code):

    priority_table = {
        "[": 0, "{": 0, "if": 0,
        "]": 1, "}": 1, ",": 1, ";": 1,
        "=": 2,
        ">": 3, ">=": 3, "<": 3, "<=": 3, "==": 3, "+=": 3, "-=": 3,
        "+": 4, "-": 4,
        "*": 5, "/": 5,
        "**": 6
    }

    token = code.split()
    postfix = []
    stack = []

    # Создание списка из букв и цифр
    str = string.ascii_letters
    alnum = []
    for i in str:
        alnum.append(i)

    ifcount = 0
    if2 = 0
    cic = 0
    ciccount = 0
    otrc = 0
    fco = 0
    cicend = 0
    masc = 0
    for i in range(len(token)):

        if token[i] in alnum or token[i].isdigit():
            postfix.append(token[i])

        elif token[i] in priority_table:
            while stack and stack[-1] in priority_table and priority_table[token[i]] <= priority_table[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(token[i])
        elif token[i] == '(':
            stack.append(token[i])
        elif token[i] == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

        # Массивы
        if len(token[i]) > 1 and token[i][0] in alnum and token[i][1] == '[':
            masc = 1
            postfix.append(token[i][0])
            stack.append('[')
            countmass = 2
            while token[i] != ']':
                if token[i] == ',':
                    countmass += 1
                i += 1
            str = "{}".format(countmass)
        elif token[i] == ']' and masc > 0:
            postfix.append(str + "АЭМ")

        # Функции
        k = 0
        if token[i] == 'f(':
            fco += 1
            stack.append('(')
            postfix.append('f')
            countfun = 2
            while token[i] != ')':
                k += 1
                if token[i] == ',':
                    countfun += 1
                i += 1
            str = "{}".format(countfun)
        elif token[i] == ')' and fco > 0:
            if k == 1:
                str = "1"
            postfix.append(str + "Ф")

        # Условный оператор
        if token[i] == 'if(':
            if2 += 1
            for j in code:
                if j == '{':
                    otrc += 1
            stack.append('(')
        if token[i] == ')' and if2 > 0:
            qwer = "{}".format(if2)
            postfix.append("М" + qwer + " УПЛ")
        if token[i] == '{' and if2 > 0:
            ifcount += 1
        if token[i] == '}' and if2 > 0:
            str2 = "{}".format(ifcount)
            if ifcount != otrc:
                str3 = "{}".format(ifcount + 1)
                postfix.append("M" + str3 + "БП")
            postfix.append("М" + str2 + ":")


        # Циклы
        if token[i] == 'while(':
            stack.append('(')
            cic += 1
        if token[i] == ')' and cic > 0 and cicend == 0:
            postfix.append('МЦ1УПЛ')
            cicend = 1
        if token[i] == '{' and cic > 0:
            ciccount += 1
        if token[i] == '}' and cic > 0:
            str5 = "{}".format(ciccount)
            postfix.append("МЦ" + str5 + ":")

    while stack:
        postfix.append(stack.pop())

    while '[' in postfix:
        postfix.remove('[')
    while ']' in postfix:
        postfix.remove(']')
    while 'function' in postfix:
        postfix.remove('function')
    while ',' in postfix:
        postfix.remove(',')
    while ';' in postfix:
        postfix.remove(';')
    while '{' in postfix:
        postfix.remove('{')
    while '}' in postfix:
        postfix.remove('}')

    return ' '.join(postfix)

ф
