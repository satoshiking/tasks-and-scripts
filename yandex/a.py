meal_d = {
    #'meal' : [people, ing_num, [ [ингридиент, кол-во, ед-ца измерения], [], ..., [] ]],
}

ingr_cat = {
    #'масло' : [стоймость, кол-во в 1 упакоке, ед-ца измерения],
}

ingr_kal = {
    #'название' : [кол-во для расчета, ед-ца измерения, белки, жиры, углеводы, kal],
}

ingr_buy = {
    #'название' : [кол-во для покупки, кол-во упаковок для покупки],
}

price = 0

import sys
sys.stdin = open("input2.txt", "r")

meal_num = int(input())
for i in range(meal_num):
    # парсим первую строку с названием, количеством людей, кол-во ингридиентов
    s = input().split()
    meal_d[s[0]] = [int(s[1]), int(s[2]), []]

    # парсим описание ингридиентов
    for i in range(int(s[2])):
        s2 = input().split()
        
        new_ingr = [s2[0], int(s2[1]), s2[2]]
        cur_ingr = meal_d[s[0]][2]
        all_ingr = []
        all_ingr.extend(cur_ingr)
        all_ingr.append(new_ingr)
        meal_d[s[0]] = [ meal_d[s[0]][0], meal_d[s[0]][1], all_ingr ]

# парсим каталог ингридиентов
for i in range(int(input())):
    s = input().split()
    ingr_cat[s[0]] = [int(s[1]), int(s[2]), s[3]]

# парсим количество ингредиентов в каталоге еды.
for i in range(int(input())):
    s = input().split()
    ingr_kal[s[0]] = [int(s[1]), s[2], float(s[3]), float(s[4]), float(s[5]), float(s[6])]

# вычисляем необходмое кол-во ингридиентов для каждого блюда ingr_buy[] = {}
for meal in meal_d:
    ingridients = meal_d[meal][2]
    for ingr in ingridients:
        mlty = 1
        izm = ingr[2]

        if izm == 'kg' or izm == 'l':
            mlty = 1000
        if izm == 'tens':
            mlty = 10

        if ingr_buy.get(ingr[0]) is None:
            ingr_num = ingr[1]*meal_d[meal][0] * mlty
            ingr_buy[ingr[0]] = [ingr_num, 0]
        else:
            ingr_num = ingr[1]*meal_d[meal][0] * mlty
            ingr_buy[ingr[0]] = [ingr_buy[ingr[0]][0] + ingr_num ,0]


for ingr in ingr_buy:
    need_to_buy = ingr_buy[ingr][0]
    in_pack = ingr_cat[ingr][1]
    
    izm = ingr_cat[ingr][2]

    if izm == 'kg':
        need_to_buy /= 1000
    if izm == 'l':
        need_to_buy /= 1000
    if izm == 'tens':
        need_to_buy /= 10

    if need_to_buy % in_pack == 0:
        ingr_cnt = int(need_to_buy / in_pack)
    else:
        ingr_cnt = int(need_to_buy / in_pack) + 1


    ingr_buy[ingr] = [ingr_buy[ingr][0], ingr_cnt]

    ingr_price = ingr_cnt * ingr_cat[ingr][0]
    price += ingr_price

    #print('  ',ingr, 'to_buy=', need_to_buy, 'in_pack=', in_pack, 'ingr_cnt=',ingr_cnt, 'ingr_price=',ingr_price )

print(price)
"""
for ingr in ingr_buy:
    print(ingr, ingr_buy[ingr])
print()
"""

for ingr in ingr_cat:
    if ingr in ingr_buy:
        print(ingr, ingr_buy[ingr][1])
    else:
        print(ingr, 0)


for meal in meal_d:
    b = 0
    g = 0
    u = 0
    kal = 0
    
    ingridients = meal_d[meal][2]
    for ingr in ingridients:
        #ingr = [ингридиент, кол-во, ед-ца измерения]
        # [кол-во для расчета, ед-ца измерения, белки, жиры, углеводы, kal],
        mlty = 1
        bel = ingr_kal[ingr[0]][2]
        bel_num = ingr_kal[ingr[0]][0]

        gir = ingr_kal[ingr[0]][3]
        gir_num = ingr_kal[ingr[0]][0]

        ugl = ingr_kal[ingr[0]][4]
        ugl_num = ingr_kal[ingr[0]][0]

        kk = ingr_kal[ingr[0]][5]
        kk_num = ingr_kal[ingr[0]][0]

        izm = ingr_kal[ingr[0]][1]
        if izm == 'kg' or izm == 'l':
            mlty = 1000
        if izm == 'tens':
            mlty = 10


        b_ingr = (ingr[1] * bel) / (bel_num*mlty)
        b += b_ingr

        g_ingr = (ingr[1] * gir) / (gir_num*mlty)
        g += g_ingr

        u_ingr = (ingr[1] * ugl) / (ugl_num*mlty)
        u += u_ingr

        kk_ingr = (ingr[1] * kk) / (kk_num*mlty)
        kal += kk_ingr
        
    print (meal , round(b,3), round(g,3), round(u,3), round(kal,3))
        

"""
print('meal_dictionary:')
for meal in meal_d:
    print(meal, meal_d[meal])
print()

print('ingr_catalog')
for ingr in ingr_cat:
    print(ingr, ingr_cat[ingr])
print()


print('ingr_kal_catalog')
for ingr in ingr_kal:
    print(ingr, ingr_kal[ingr])
print()

print('ingr_buy_catalog')
for ingr in ingr_buy:
    print(ingr, ingr_buy[ingr])
print()
"""