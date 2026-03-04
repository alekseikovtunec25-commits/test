#Task1
var1 = input("Please enter a word:") #рпросим ввести желаемое слово
if len(var1) < 1: #проверяем на длинну строки
    print("please another word") #просим ввести другое слово так как слишком коротко
elif len(var1) > 2:
    print(var1[:2] + var1[-2:])