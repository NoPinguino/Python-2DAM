palabra = input("Introduce una palabra: ")
vocales = 0
for i in palabra:
    i = i.lower()
    if (i == "a" or i== "e" or i == "i" or i == "o" or i =="u"):
        vocales+=1
print(vocales) 