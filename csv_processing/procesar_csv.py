import csv

archivo_entrada = 'datos.csv'
archivo_salida_ingresos = 'nro_ingreso.csv'
archivo_salida_dnis = 'dni.csv'

ingresos = []
dnis_pares = []

with open(archivo_entrada, mode='r', newline='', encoding='utf-8') as file:
    lector = csv.DictReader(file, delimiter=';')
    for fila in lector:
        ingresos.append(int(fila['nro_ingreso']))
        dni = int(fila['dni'])
        if dni % 2 == 0:
            dnis_pares.append(dni)

ingresos.sort()
dnis_pares.sort(reverse=True)

with open(archivo_salida_ingresos, mode='w', newline='', encoding='utf-8') as file:
    escritor = csv.writer(file)
    escritor.writerow(['nro_ingreso'])
    for ingreso in ingresos:
        escritor.writerow([ingreso])

with open(archivo_salida_dnis, mode='w', newline='', encoding='utf-8') as file:
    escritor = csv.writer(file)
    escritor.writerow(['dni_par'])
    for dni in dnis_pares:
        escritor.writerow([dni])

print("Archivos generados correctamente.")