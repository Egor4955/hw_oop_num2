import json
from pprint import pprint

with open('oop2/recipes.txt', 'r',encoding='utf-8') as file:
    cook_book = {}
    for reciepes in file:
        ingridient_count = int(file.readline())
        ingridient_list = []
        for i in range(ingridient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingridient_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[reciepes.strip()]= ingridient_list
    res = json.dumps(cook_book, indent=2, ensure_ascii=False)
    

def get_shop_list_by_dishes(dishes, person_count:int):
    total_ingridient = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                if ing['ingredient_name'] in total_ingridient :
                    total_ingridient [ing['ingredient_name']]['quantity'] += int(ing['quantity']) * person_count
                else:
                    total_ingridient [ing['ingredient_name']] = {'measure': ing['measure'],'quantity': (int(ing['quantity']) * person_count)}
   
    pprint(total_ingridient)        

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)






    



