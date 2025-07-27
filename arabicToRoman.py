"""""
romanString = ""

def arabicToRoman(x):
    global romanString
    arabicNumbers = [1,5,10,50,100,500,1000]
    romanNumbers = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    for i in range(1, x + 1):
        if i in romanNumbers:
           romanString += romanNumbers[i]       

numero_seleccionado = int(input("select a number from 1 to 4000: "))
arabicToRoman(numero_seleccionado)

print(romanString)

"""

romanString = ""

def arabicToRoman(x):
    global romanString
    arabicNumbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romanNumbers = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    i = 0
    while x > 0:
        if x >= arabicNumbers[i]:
            romanString += romanNumbers[i]
            x -= arabicNumbers[i]
        else:
            i+=1


numero_seleccionado = int(input("select a number from 1 to 4000: "))
arabicToRoman(numero_seleccionado)

print(romanString)
