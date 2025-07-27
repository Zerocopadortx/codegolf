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
