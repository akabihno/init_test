import random
from time import time
from functools import reduce
before = time()
chess_letters = "abcdefgh"
chess_letters_rev = "hgfedcba"
chess_numbers = "12345678"
chess_numbers_rev = "87654321"
sum_list_a = list()
sum_list = list()
trick_list = list()
result_list = list()
conv_sum_list = list()
conv_trick_list = list()
n = 0
#l = 0
m = 1
p = 0
moves = 0
while 1:
    while moves < 9:
        while n < 8:
            for q in chess_numbers:
                def kopa(array_a, n):
                    return([i + str(n) for i in array_a])
            n += 1
            a = kopa(chess_letters, n)
            sum_list_a.append(a)
        sum_list = sum_list_a[::-1]
        if moves == 0:
            alef = random.choice(sum_list)
            bet = random.choice(alef)
        else:
            bet = random.choice(result_list)
        for row in sum_list:
            for elem in row:
                if elem == (bet):
                    print(elem+"*", end=' ')
                    if elem.find("*") != "-1":
                        bad_letter = elem[0] #мы - за повторное
                        semi_bad_number = elem[1]
                        bad_elem = list(elem)
                        bad_row = alef
                        index = chess_letters.find(bad_letter)
                        chess_letters_I = chess_letters[(index+1):]
                        right = chess_letters_I #right
                        index_num = chess_numbers.find(semi_bad_number)
                        chess_numbers_I = chess_numbers[(index_num+1):]
                        up = chess_numbers_I #up
                        if len(chess_letters_I) < len(chess_numbers_I):
                            chess_numbers_I = chess_numbers_I[:len(chess_letters_I)]
                        elif len(chess_letters_I) > len(chess_numbers_I):
                            chess_letters_I = chess_letters_I[:len(chess_numbers_I)]
                        chess_letters_IV = chess_letters[(index+1):]
                        index_num = chess_numbers_rev.find(semi_bad_number)
                        chess_numbers_IV = chess_numbers_rev[(index_num+1):]
                        down = chess_numbers_IV #down
                        if len(chess_letters_IV) < len(chess_numbers_IV):
                            chess_numbers_IV = chess_numbers_IV[:len(chess_letters_IV)]
                        elif len(chess_letters_IV) > len(chess_numbers_IV):
                            chess_letters_IV = chess_letters_IV[:len(chess_numbers_IV)]
                        index = chess_letters_rev.find(bad_letter)
                        chess_letters_III = chess_letters_rev[(index+1):]
                        left = chess_letters_III #left
                        chess_numbers_III = chess_numbers_rev[(index_num+1):]
                        if len(chess_letters_III) < len(chess_numbers_III):
                            chess_numbers_III = chess_numbers_III[:len(chess_letters_III)]
                        elif len(chess_letters_III) > len(chess_numbers_III):
                            chess_letters_III = chess_letters_III[:len(chess_numbers_III)]
                        index_num = chess_numbers.find(semi_bad_number)
                        chess_letters_II = chess_letters_rev[(index+1):]
                        chess_numbers_II = chess_numbers[(index_num+1):]
                        if len(chess_letters_II) < len(chess_numbers_II):
                            chess_numbers_II = chess_numbers_II[:len(chess_letters_II)]
                        elif len(chess_letters_II) > len(chess_numbers_II):
                            chess_letters_II = chess_letters_II[:len(chess_numbers_II)]

                    else:
                         print(0)
                else:
                    print(elem, end=' ')

            print()
        print()
        for wI in chess_letters_I:
            deltI = (chess_letters_I[p:len(chess_letters_I) - (len(chess_letters_I)-m)],\
                     chess_numbers_I[p:len(chess_numbers_I) - (len(chess_numbers_I)-m)])
            #print(deltI)
            trick_list.append(deltI)
            m += 1
            p += 1
        m = 1
        p = 0
        for wIV in chess_letters_IV:
            deltIV = (chess_letters_IV[p:len(chess_letters_IV) - (len(chess_letters_IV)-m)],\
                      chess_numbers_IV[p:len(chess_numbers_IV) - (len(chess_numbers_IV)-m)])
            #print(deltIV)
            trick_list.append(deltIV)
            m += 1
            p += 1
        m = 1
        p = 0
        for wIII in chess_letters_III:
            deltIII = (chess_letters_III[p:len(chess_letters_III) - (len(chess_letters_III)-m)],\
                      chess_numbers_III[p:len(chess_numbers_III) - (len(chess_numbers_III)-m)])
            #print(deltIII)
            trick_list.append(deltIII)
            m += 1
            p += 1
        m = 1
        p = 0
        for wII in chess_letters_II:
            deltII = (chess_letters_II[p:len(chess_letters_II) - (len(chess_letters_II)-m)],\
                      chess_numbers_II[p:len(chess_numbers_II) - (len(chess_numbers_II)-m)])
            #print(deltII)
            trick_list.append(deltII)
            m += 1
            p += 1
        for r in right:
            delt_r = (r, semi_bad_number)
            #print(delt_r)
            trick_list.append(delt_r)
        for l in left:
            delt_l = (l, semi_bad_number)
            #print(delt_l)
            trick_list.append(delt_l)
        for d in down:
            delt_b = (bad_letter, d) #использование
            #print(delt_b)
            trick_list.append(delt_b)
        for u in up:
            delt_u = (bad_letter, u) #переменных
            #print(delt_u)
            trick_list.append(delt_u)
        #print(trick_list)

        def rm_duplex(entities):
            sub_list = list()
            for entity in entities:
                if entity not in sub_list:
                    sub_list.append(entity)
            return sub_list


        for cd in sum_list:
            for cn in cd:
                part = cn[0] + cn[1]
                conv_sum_list = conv_sum_list+[part]
        ##print(conv_sum_list)
        print() ###

        conv_sum_list = rm_duplex(conv_sum_list)

        for au in trick_list:
            cu = au[0] + au[1]
            conv_trick_list = conv_trick_list+[cu]
        ##print(conv_trick_list)

        conv_trick_list = rm_duplex(conv_trick_list)

        for pi in bad_letter: #ахаха
                def magic(array_magic, semi_bad_number): #?! Харе Rama, Харе Delma
                    return([pi + semi_bad_number for pi in array_magic]) #wtf вообще
        piu = magic(bad_letter, semi_bad_number)
        print(piu) #о чудо, оно работает o_o
        conv_trick_list = conv_trick_list+piu


        result_list = (list(set(conv_sum_list).difference(conv_trick_list)))
        result_list = sorted(result_list)
        #result_list = list(set(result_list).difference(piu))
        result_list = sorted(result_list)
        result_list = rm_duplex(result_list)
        print("sum list: ", conv_sum_list, "; ", len(conv_sum_list))
        print()
        print("trick list: ", conv_trick_list, "; ", len(conv_trick_list))
        print()
        print("trick list sorted: ", sorted(conv_trick_list), "; ", len(conv_trick_list))
        print()
        print("result list: ", result_list, "; ", len(result_list))
        after = time()
        print()
        moves += 1
        print("Pondering time:", after - before, "seconds")
        if result_list == []:
            break
    if result_list == []:
        break
        
