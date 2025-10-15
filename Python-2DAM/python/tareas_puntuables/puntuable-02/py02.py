# Aries: 21 de marzo – 20 de abril
# Tauro: 21 de abril – 20 de mayo
# Géminis: 21 de mayo – 21 de junio
# Cáncer: 22 de junio – 22 de julio
# Leo: 23 de julio – 23 de agosto
# Virgo: 24 de agosto – 22 de septiembre
# Libra: 23 de septiembre – 23 de octubre
# Escorpio: 24 de octubre – 22 de noviembre
# Sagitario: 23 de noviembre – 21 de diciembre
# Capricornio: 22 de diciembre – 20 de enero
# Acuario: 21 de enero – 19 de febrero
# Piscis: 20 de febrero – 20 de marzo

print(f"1. Enero")
print(f"2. Febrero")
print(f"3. Marzo")
print(f"4. Abril")
print(f"5. Mayo")
print(f"6. Junio")
print(f"7. Julio")
print(f"8. Agosto")
print(f"9. Septiembre")
print(f"10. Octubre")
print(f"11. Noviembre")
print(f"12. Diciembre")
mes = int(input("En qué mes has nacido:"))
dia = int(input ("Introduce el día en que naciste: "))
match(mes):
    case 1:
        if dia < 21:
            print("Eres Capricornio.")
        else:
            print("Eres Acuario")
    case 2:
        if dia < 19:
            print("Eres Acuario.")
        else:
            print("Eres Piscis")
    case 3:
        if dia < 20:
            print("Eres Piscis.")
        else:
            print("Eres Aries")
    case 4:
        if dia < 20:
            print("Eres Aries.")
        else:
            print("Eres Tauro")
    case 5:
        if dia < 20:
            print("Eres Tauro.")
        else:
            print("Eres Géminis")
    case 6:
        if dia < 21:
            print("Eres Géminis.")
        else:
            print("Eres Cáncer")
    case 7:
        if dia < 22:
            print("Eres Cáncer.")
        else:
            print("Eres Leo")
    case 8:
        if dia < 23:
            print("Eres Leo.")
        else:
            print("Eres Virgo")
    case 9:
        if dia < 22:
            print("Eres Virgo.")
        else:
            print("Eres Libra")
    case 10:
        if dia < 23:
            print("Eres Libra.")
        else:
            print("Eres Escorpio")
    case 11:
        if dia < 22:
            print("Eres Escorpio.")
        else:
            print("Eres Sagtário")
    case 12:
        if dia < 21:
            print("Eres Sagitário.")
        else:
            print("Eres Capricornio")