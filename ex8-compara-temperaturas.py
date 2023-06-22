file_path = 'C:\\Users\\fmta2\\Desktop\\code\\python\\cap17\\ex8\\temperaturas.txt'
with open(file_path, 'r') as file:
    matrix_data = file.readlines()
matrix = [line.split() for line in matrix_data]
hora = int(input("informe o horario?: "))

maior_temp = 0.0
indice_maior_temp = 0
dia = ["SEG","TER","QUA","QUI","SEX","SAB","DOM"]
i = 0
while(0 <= hora <= 24):
    for row in matrix:
        if (float(row[hora]) > maior_temp):
            maior_temp = float(row[hora]) 
            indice_maior_temp = i
        i = i + 1
    print(hora,"-",dia[indice_maior_temp])
    print("================================")
    hora = int(input("informe o horario?: "))
            