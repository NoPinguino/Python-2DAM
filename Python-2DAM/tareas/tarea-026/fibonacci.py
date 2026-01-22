num = int(input("Número para fibonacci: "))
a, b = 0, 1
for i in range(num):
    print(a,end=" ")
    a, b = b, a + b
    #a = b
    #b = a + b