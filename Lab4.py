from Lab1 import *

def char_init(arr, in_arr, iterator):
    flag = 0
    iter = iterator
    while iter < len(arr) and flag != 1:
        for el in in_arr:
            if el == arr[iter]:
                flag = 1
        if(flag == 0):
            iter += 1
    return iter

def multp(multip):
    iter = 0
    if len(multip)>1:
        left_rart = multip[0:len(multip)]
        if len(left_rart) > 1:
            if (["R7"] in left_rart or ["R8"] in left_rart):
                if "I" in multip[0][0]:
                    open_bracket = char_init(multip, ["R7"], 0)
                    close_bracket = char_init(multip, ["R7"], 0)
                    if open_bracket == len(multip) or close_bracket == len(multip):
                        return False
                    if(open_bracket - close_bracket == 1):
                        print("При обращении к массиву не задали параметры")
                        return False
                    perem = open_bracket+1
                    while close_bracket - perem>=1:

                        end_perem = char_init(multip, ["R11"], perem)
                        if(multip[end_perem] != ["R11"]):
                            if not Expression(left_rart[perem:close_bracket]):
                                return False
                        if not Expression(left_rart[perem:end_perem]):
                            return False
                        perem = end_perem+1
                    return True
            elif (["R3"] in left_rart and ["R2"] in left_rart):
                if "I" in multip[0][0]:
                    open_bracket = char_init(multip, ["R7"], 0)
                    close_bracket = char_init(multip, ["R7"], 0)
                    if (open_bracket - close_bracket == 1):
                        print("При обращении к массиву не задали параметры")
                        return False
                    perem = open_bracket + 1
                    while close_bracket - perem >= 1:

                        end_perem = char_init(multip, ["R11"], perem)
                        if (multip[end_perem] != ["R11"]):
                            if not Expression(left_rart[perem:close_bracket]):
                                return False
                        if not Expression(left_rart[perem:end_perem]):
                            return False
                        perem = end_perem + 1
                    return True

    if "N" in multip[iter][0] or "C" in multip[iter][0]:
        return True
    elif "I" in multip[iter][0]:
        return True
    elif ['R3'] == multip[iter]:
        new_iter = char_init(multip, ["R2"], iter)
        if multip[new_iter] == ['R2']:
            if Expression(multip[iter + 1:new_iter - 1]):
                return True
        return False
    return False

def sums(sums):
    # если выражение не нулевое
    # (нулевое выражение не считается за ошибку)
    if (len(sums) != 0):
        iter = 0
        new_iter = char_init(sums, [['O3'], ['O4']], iter)
        if (multp(sums[iter:new_iter])):
            iter = new_iter+1
            while (iter < len(sums)):
                new_iter = char_init(sums, [['O3'], ['O4']], iter)
                if (multp(sums[iter:new_iter])):
                    iter = new_iter + 1
                else:
                    return False
        else:
            return False
    return True

def Expression(in_expr):
    #если выражение не нулевое
    # (нулевое выражение не считается за ошибку)
    if(len(in_expr)!=0):
        iter = 0
        new_iter = char_init(in_expr, [['O1'], ['O2']], iter)
        if (sums(in_expr[iter:new_iter])):
            iter = new_iter+1
        else:
            return False

        while(iter<len(in_expr)):
            new_iter = char_init(in_expr, [['O1'], ['O2']], iter)
            if(sums(in_expr[iter:new_iter])):
                iter = new_iter+1
            else:
                return False
    return True
#Оператор присваивания
def equals(in_assig):
    iter = char_init(in_assig, [["O12"]], 0)
    if iter == len(in_assig):
        return False
    else:
        #  Проверяем левую чать оператора на обращение к элементу массива
        left_rart = in_assig[0:iter]
        if len(left_rart) > 1:
            if(["R7"] in left_rart and ["R8"] in left_rart):
                if("I" in in_assig[0][0] and Expression(left_rart[2:len(left_rart)-1]) and Expression(in_assig[iter+1:len(in_assig)])):
                    return True
            return False
        param = char_init(in_assig, [["R4"]], 0)
        if param - iter == 1:
            return False
        if("I" in in_assig[0][0] and Expression(in_assig[iter+1:len(in_assig)])):
            return True
        return False


#Условие
def condition(in_cond):
    iter = char_init(in_cond, [['06'], ['07'], ['O8'], ['O9'], ['O10'], ["O11"]], 0)
    if(iter == len(in_cond)):
        return False
    else:
        if Expression(in_cond[0:iter]) and Expression(in_cond[iter+1:len(in_cond)]):
            return True
        else:
            return False

# Условный оператор
def cond_operator(in_if):
    if(["W2"] in in_if):
        open_cond = char_init(in_if, [["R3"]], 1)
        close_cond = char_init(in_if, [["R2"]], 1)
        if(open_cond == close_cond-1):
            print("Условие не задано")
            return False
        elif close_cond == len(in_if):
            print("Условие. Не нашли закрывающую скобку")
            return False
        else:
            if(condition(in_if[open_cond + 1:close_cond])):
                open_oper = char_init(in_if, [["R12"]], 1)
                close_oper = char_init(in_if, [["R13"]], 1)
                if (close_oper == len(in_if)):
                    print("Условный оператор: не нашли ,},")
                    return False
                if (open_oper == close_oper - 1):
                    print("Операторы в if не заданы")
                    return False
                else:
                    open_oper = char_init(in_if, [["R4"]], open_oper) + 1
                    if(syntax_analizer(in_if[open_oper:close_oper])):
                        # Проверим наличие else
                        if(close_oper != len(in_if) and ["W3"] in in_if):
                            open_oper = char_init(in_if, [["R12"]], close_oper)
                            close_oper = char_init(in_if, [["R13"]], close_oper + 1)
                            if(close_oper == len(in_if)):
                                return False
                            if (open_oper == close_oper - 1):
                                return False
                            else:
                                return True
                        return True
                    else:
                        return False
            else:
                return False
    else:
        return False

def function(in_f):
        open_cond = char_init(in_f, [["R3"]], 1)
        close_cond = char_init(in_f, [["R2"]], 1)
        if open_cond == len(in_f) or close_cond == len(in_f):
            print("Круглые скобки в функции")
            return False
        #Проверка параметров функции
        param = open_cond + 1
        while close_cond - param >= 1:
            if "I" in in_f[param][0]:
                if(close_cond - param == 1):
                    param +=1
                else:
                    if ["R11"] == in_f[param+1]:
                        param +=2
                    else:
                        return False
            else:
                return False
        open_cond = char_init(in_f, [["R12"]], 1)
        close_cond = char_init(in_f, [["W9"]], 1)
        #Проверяем наличие return
        if close_cond == len(in_f):
            return False
        #проверка параметров функции
        if not syntax_analizer(in_f[open_cond + 2:close_cond]):
            print("Операторы функции не прошли проверку")
            return False
        open_cond = char_init(in_f, [["R3"]], close_cond)
        close_cond = char_init(in_f, [["R2"]], open_cond)
        if open_cond == len(in_f) or close_cond == len(in_f):
            print("Круглые скобки в функции в return")
            return False
        if(close_cond - open_cond == 1):
            print("return не имеет выражения")
            return False
        if(Expression(in_f[open_cond+1:close_cond])):
            return True
        return False
def cicle(in_w):
    if (["W4"] in in_w):
        open_cond = char_init(in_w, [["R3"]], 1)
        close_cond = char_init(in_w, [["R2"]], 1)
        if (open_cond == close_cond - 1):
            print("Условие не задано(while)")
            return False
        else:
            if (condition(in_w[open_cond + 1:close_cond])):
                open_oper = char_init(in_w, [["R12"]], 1)
                close_oper = char_init(in_w, [["R13"]], 1)
                if (close_oper == len(in_w)):
                    print("Условный оператор: не нашли ,},")
                    return False
                if (open_oper == close_oper - 1):
                    print("Операторы в while не заданы")
                    return False
                else:
                    open_oper = char_init(in_w, [["R4"]], open_oper)
                    if (syntax_analizer(in_w[open_oper + 1:close_oper])):
                        return True
                    else:
                        return False
            else:
                return False
    else:
        print("while не найден")
        return False
def oper_in(s, n):
    if n == 1:
        return cicle(s)
    if n == 2:
        return function(s)
    if n == 3:
        return cond_operator(s)
    if n == 4:
        return equals(s)
    print("Ошибка")
    return False

def syntax_analizer(text):
    iter = 0
    if text == []:
        return False
    else:
        while(iter < len(text)):
            new_iter = char_init(text, [["R4"]], iter)
            #Проверка на условный оператор
            if ["W2"] in text[iter:new_iter]:
                #Ищем закрывающую фигурную скобку
                new_iter = char_init(text, [["R13"]], new_iter)
                #Если мы её не нашли и упёрлись в конец программы
                if(new_iter == len(text)):
                    return False
                #Проверка на потерянную }
                prov = char_init(text, [["R12"]], iter)
                if ['W2']in text[prov + 1:new_iter] or ['W3'] in text[prov + 1:new_iter] or ['W4'] in text[prov + 1:new_iter]:
                    print('Потеряна фигурная скобка')
                    return False
                #проанализируем следующую строчку

                start_next_str = char_init(text, [["R4"]], new_iter) + 1
                end_next_str = char_init(text, [["R4"]], start_next_str)
                #Есди в этой строчке есть else записываем и его
                if(['W3'] in text[start_next_str:end_next_str]):
                    new_iter = char_init(text, [["R13"]], start_next_str + 1)
                    prov = char_init(text, [["R12"]], end_next_str)
                    if ['W2'] in text[prov + 1:new_iter] or ['W3'] in text[prov + 1:new_iter] or [
                        'W4'] in text[
                                 prov + 1:new_iter]:
                        print('Потеряна фигурная скобка')
                        return False
                    if oper_in(text[iter:new_iter + 1], 3):
                        iter = char_init(text, [["R4"]], new_iter) + 1
                    else:
                        return False
                #Если еслз не нашли, то проверяем if
                else:
                    if oper_in(text[iter:new_iter + 1], 3):
                        iter = char_init(text, [["R4"]], new_iter) + 1
                    else:
                        return False
            #Если обнаружили while
            elif ["W4"] in text[iter:new_iter]:
                # Ищем закрывающую фигурную скобку
                new_iter = char_init(text, [["R13"]], new_iter)
                # Если мы её не нашли и упёрлись в конец программы
                if (new_iter == len(text)):
                    return False
                # }
                prov = char_init(text, [["R12"]], iter)
                if ['W2'] in text[prov + 1:new_iter] or ['W3'] in text[prov + 1:new_iter] or ['W4'] in text[prov + 1:new_iter]:
                    print('Потеряна фигурная скобка')
                    return False

                if oper_in(text[iter:new_iter + 1], 1):
                    iter = char_init(text, [["R4"]], new_iter) + 1
                else:
                    return False

            # Если обнаружили function
            elif ["W8"] in text[iter:new_iter]:
                # Ищем закрывающую фигурную скобку
                new_iter = char_init(text, [["R13"]], new_iter)
                # Если мы её не нашли и упёрлись в конец программы
                if (new_iter == len(text)):
                    return False
                prov = char_init(text, [["R12"]], iter)
                if ['W2'] in text[prov + 1:new_iter] or ['W3'] in text[prov + 1:new_iter] or ['W4'] in text[prov + 1:new_iter]:
                    print('Потеряна фигурная скобка')
                    return False
                if oper_in(text[iter:new_iter + 1], 2):
                    iter = char_init(text, [["R4"]], new_iter) + 1
                else:
                    return False

            #Если обнаружили оператор присваивания
            elif ["O12"] in text[iter:new_iter]:
                if oper_in(text[iter:new_iter], 4):
                    iter = char_init(text, [["R4"]], new_iter) + 1
                else:
                    return False
            else:
                print("Не обнаружен оператор")
                return False
        return True

def get_array(arr):
    new_arr = []
    for i in arr:
        for j in i:
            new_arr.append(j)
    return new_arr

syntax = get_array(lexical_analize)

if syntax_analizer(syntax):
    print('Программа прошла синтаксический анализ!')
else:
    print('Программа не прошла синтаксический анализ!')

