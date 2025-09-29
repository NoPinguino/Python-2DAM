lista = ["q","a","w","e","s","d","u","v","j","o","i","p","n"]
vocales = ["a","e","i","o","u"]
contador = 0
for i in lista:
    if i in vocales:
        contador+=1
print(f"Se han encontrado {contador} vocales.")