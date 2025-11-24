dic1 = {
    "a": 9,
    "b": 8,
    "c": 7,
}
dic2 = {
    "a": 9,
    "b": 8,
    "c": 7,
    "d": 8,
}
dic3 = {}
for i in dic1.keys() | dic2.keys():
    dic3[i] = dic1.get(i, 0) + dic2.get(i, 0)

print(dic3)