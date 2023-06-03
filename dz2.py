# Задача 3 
import os 
from pprint import pprint 


res = []
res2 = []
for filename in os.listdir('oop2/dz_2/'):
    with open(os.path.join('oop2/dz_2', filename), 'r', encoding='utf-8') as f:
        text = f.readlines()
        len_ = len(text)
        dict_ = {filename: len_}
        res_1 =[]
        for key in dict_.keys():
            res_1.append(key)
            
        for value in dict_.values():
            res_1.append(value)
        
        for line in text:
            res_1.append(line)

        res.append(res_1)
        del res_1[3:]

res_2 = sorted(res, key=lambda x: x[1])


with open("oop2/res.txt","w",encoding='utf-8') as result:
    for element in res_2:
        for el in element:
            result.writelines(str(el))
            result.writelines('\n')




    



    
        

