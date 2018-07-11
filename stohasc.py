import csv
from decimal import * #Включаем тип данных Decimal

#Фйнкция Стохастического Асциллятора
def StohAsc(ct,minlt,maxht):
    kt = ((ct-minlt)/(maxht-minlt)) * 100
    return kt

FILENAME = "USD000UTSTOM_170101_171213.csv" #файл с данными по дням за год

lt = [] #список минимумов за период
ht = [] #список максимумов за период
period = 7 #период в днях
sost = 0 # 0-ожид.итерп k; 1-ожид.ком; 2-ож.ком.прод; 3-ком.прод,стоп; 4-ож.ком.пок; 5-ком.пок,стоп

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        
        ct = Decimal(row[5]) #цена закрытия

        #Вычисляем минимальный минимум в рамках периода
        lt.append(Decimal(row[4]))
        if len(lt) > period:
            lt.pop(0)
        minlt = min(lt)

        #Вычисляем максимальный максимум в рамках периода
        ht.append(Decimal(row[3]))
        if len(ht) > period:
            ht.pop(0)
        maxht = max(ht)
        
        kt = StohAsc(ct,minlt,maxht)
        #print(row[2], "-", row[3], "-", row[4], "-", row[5])
        print(kt)

        if sost == 0:
            if 20 <= kt <= 80:
                sost = 1
        elif sost == 1:
            if kt > 80:
                sost = 2
            elif kt < 20:
                sost = 4
        elif sost == 2:
            if 20 <= kt <= 80:
                print("Sell")
                sost = 1
            elif kt < 20:
                sost = 0
        elif sost == 4:
            if 20 <= kt <= 80:
                print("Buy")
                sost = 1
            elif kt > 80:
                sost = 0
        
            

