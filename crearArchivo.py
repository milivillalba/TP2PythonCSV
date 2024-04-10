import csv
#datos a escribir en el archivos 

datos=[
    ["Localidad","Provincia"],
    ["Ingeniero Juarez","Formosa"],
    ["Piranè","Formosa"],
    ["Las Lomitas","Formosa"],
    ["Laguna Blanca","Formosa"],
    ["Morillo","Salta"],
    ["Pichanal","Salta"],
    ["San Ramon De La Nueva Oran","Salta"],
    ["Tartagal","Salta"],
]
#lista de las provincias

lista_de_provincias=["Formosa","Salta"]

for provincia in lista_de_provincias:
    #abrir el archivo csv en modo escritura
    nombre_archivo= provincia+".CSV"
    with open(nombre_archivo, mode="w",newline="", encoding="utf-8") as file:
        #crea un escritorio csvs
        writer= csv.writer(file)
        #escribir los datos en el archivo
        writer.writerows(datos)

