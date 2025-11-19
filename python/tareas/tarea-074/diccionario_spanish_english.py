diccionario = {
    "hola" : "hello",
    "casa" : "house",
    "pan" : "bread",
    "agua" : "water",
    "mundo" : "world"
}
palabra = input("Ingrese una palabra: ")
if palabra in diccionario:
    print(diccionario[palabra])