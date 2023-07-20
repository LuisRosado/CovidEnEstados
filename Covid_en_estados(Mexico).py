import os

def NorOeste(pais):
    op = int(input('''Estados
1)Baja California
2)Baja California Sur
3)Chihuahua
4)Durango
5)Sinaloa
6)Sonora
'''))
    if op == 1:
        print("Baja California:",pais["Baja California"],"casos confirmados")
    elif op == 2:
        print("Baja California Sur:",pais["Baja California Sur"],"casos confirmados")
    elif op == 3:
        print("Chihuahua:",pais["Chihuahua"],"casos confirmados")
    elif op == 4:
        print("Durango:",pais["Durango"],"casos confirmados")
    elif op == 5:
        print("Sinaloa:",pais["Sinaloa"],"casos confirmados")
    elif op == 6:
        print("Sonora:",pais["Sonora"],"casos confirmados")
    else:
        print("Valor Invalido...")

def NorEste(pais):
    op = int(input('''Estados
1)Coahuila
2)Nuevo Leon
3)Tamaulipas
'''))
    if op == 1:
        print("Coahuila:",pais["Coahuila"],"casos confirmados")
    elif op == 2:
        print("Nuevo Leon:",pais["Nuevo Leon"],"casos confirmados")
    elif op == 3:
        print("Tamaulipas:",pais["Tamaulipas"],"casos confirmados")
    else:
        print("Valor Invalido...")

def Occidente(pais):
    op = int(input('''Estados
1)Nayarit
2)Jalisco
3)Colima
4)Michoacan
'''))
    if op == 1:
        print("Nayarit:",pais["Nayarit"],"casos confirmados")
    elif op == 2:
        print("Jalisco:",pais["Jalisco"],"casos confirmados")
    elif op == 3:
        print("Colima:",pais["Colima"],"casos confirmados")
    elif op == 4:
        print("Michoacan:",pais["Michoacan"],"casos confirmados")
    else:
        print("Valor Invalido...")

def Oriente(pais):
    op = int(input('''Estados
1)Puebla
2)Veracruz
3)Tlaxcala
4)Hidalgo
'''))
    if op == 1:
        print("Puebla:",pais["Puebla"],"casos confirmados")
    elif op == 2:
        print("Veracruz:",pais["Veracruz"],"casos confirmados")
    elif op == 3:
        print("Tlaxcala:",pais["Tlaxcala"],"casos confirmados")
    elif op == 4:
        print("Hidalgo:",pais["Hidalgo"],"casos confirmados")
    else:
        print("Valor Invalido...")

def CentroNorte(pais):
    op = int(input('''Estados
1)Aguascalientes
2)Guanajuato
3)San Luis Potosi
4)Zacatecas
5)Queretaro
'''))
    if op == 1:
        print("Aguascalientes:",pais["Aguascalientes"],"casos confirmados")
    elif op == 2:
        print("Guanajuato:",pais["Guanajuato"],"casos confirmados")
    elif op == 3:
        print("San Luis Potosi:",pais["San Luis Potosi"],"casos confirmados")
    elif op == 4:
        print("Zacatecas:",pais["Zacatecas"],"casos confirmados")
    elif op == 5:
        print("Queretaro:",pais["Queretaro"],"casos confirmados")
    else:
        print("Valor Invalido...")

def CentroSur(pais):
    op = int(input('''Estados
1)Morelos
2)Estado de Mexico
3)Ciudad de Mexico
'''))
    if op == 1:
        print("Morelos:",pais["Morelos"],"casos confirmados")
    elif op == 2:
        print("Estado de Mexico:",pais["Estado de Mexico"],"casos confirmados")
    elif op == 3:
        print("Ciudad de Mexico:",pais["Ciudad de Mexico"],"casos confirmados")
    else:
        print("Valor Invalido...")

def SurOeste(pais):
    op = int(input('''Estados
1)Guerrero
2)Oaxaca
3)Chiapas
'''))
    if op == 1:
        print("Guerrero:",pais["Guerrero"],"casos confirmados")
    elif op == 2:
        print("Oaxaca:",pais["Oaxaca"],"casos confirmados")
    elif op == 3:
        print("Chiapas:",pais["Chiapas"],"casos confirmados")
    else:
        print("Valor Invalido...")

def SurEste(pais):
    op = int(input('''Estados
1)Tabasco
2)Campeche
3)Quintana Roo
4)Yucatan
'''))
    if op == 1:
        print("Tabasco:",pais["Tabasco"],"casos confirmados")
    elif op == 2:
        print("Campeche:",pais["Campeche"],"casos confirmados")
    elif op == 3:
        print("Quintana Roo:",pais["Quintana Roo"],"casos confirmados")
    elif op == 4:
        print("Yucatan:",pais["Yucatan"],"casos confirmados")
    else:
        print("Valor Invalido...")

def Menu(pais):
    opcion = int(input('''Regiones de la Republica:
1)NorOeste
2)NorEste
3)Occidente
4)Oriente
5)CentroNorte
6)CentroSur
7)SurOeste
8)SurEste
'''));

    if opcion == 1:
        os.system("cls")
        NorOeste(pais)
    elif opcion == 2:
        os.system("cls")
        NorEste(pais)
    elif opcion == 3:
        os.system("cls")
        Occidente(pais)
    elif opcion == 4:
        os.system("cls")
        Oriente(pais)
    elif opcion == 5:
        os.system("cls")
        CentroNorte(pais)
    elif opcion == 6:
        os.system("cls")
        CentroSur(pais)
    elif opcion == 7:
        os.system("cls")
        SurOeste(pais)
    elif opcion == 8:
        os.system("cls")
        SurEste(pais)
    else:
        print('Opcion no valida...')

pais = {"Baja California":28,"Baja California Sur":7,"Chihuahua":6,"Durango":21,"Sinaloa":1,"Sonora":44,
"Coahuila":39,"Nuevo Leon":31,"Tamaulipas":3,
"Nayarit":1,"Jalisco":18,"Colima":0,"Michoacan":3,
"Puebla":26,"Veracruz":1,"Tlaxcala":1,"Hidalgo":10,
"Aguascalientes":2,"Guanajuato":17,"San Luis Potosi":4,"Zacatecas":33,"Queretaro":19,
"Morelos":5,"Estado de Mexico":322,"Ciudad de Mexico":69,
"Guerrero":4,"Oaxaca":4,"Chiapas":0,
"Tabasco":2,"Campeche":0,"Quintana Roo":0,"Yucatan":7}

Menu(pais)
