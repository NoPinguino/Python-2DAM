letra = input("Introduce una letra o caracter: ").lower()
match(letra):
    case "a" | "e" | "i" | "o" | "u":
        print(f"{letra} es una VOCAL")
    case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | "n" | "ñ" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z":
        print(f"{letra} es una CONSONANTE")
    case _:
        print(f"{letra} es un cacter especial")
        