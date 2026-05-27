idade = int( input( " digite a sua idade"))
genero = input("digite m-para masculino e f-femnino").upper()
if genero == "m" and idade>= 18:
    print("apto a se alistar")
else:
    print("não apto a se alistar")
