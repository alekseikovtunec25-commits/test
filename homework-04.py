#task1
var1 = "helloworld" #вариант слова
if len(var1) < 2 :
    print("") #при наличии мене двух символов выводить пустоту
elif len(var1) > 2 :
    print(var1[:2] + var1[-2:]) #при наличии болле 2 символов берем первые два символа и два последних


var2 = "my"
if len(var2) < 2 :
    print("")
elif len(var2) >= 2 :
    print(var2[:2] + var2[-2:])


var3 = "X"
if len(var3) < 2 :
    print(".")
elif len(var3) > 2 :
    print(var3[:2] + var3[-2:])
