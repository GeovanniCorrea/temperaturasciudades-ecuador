# Escritura de Archivo de Texto
# Creamos y abrimos el archivo "my_notes.txt" en modo escritura
with open("my_notes.txt", "w") as file:
    file.write("Estas son mis notas personales.\n")
    file.write("Estoy aprendiendo a manejar archivos en Python.\n")
    file.write("GeoGebra es útil para visualizar integrales.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo "my_notes.txt" en modo lectura
with open("my_notes.txt", "r") as file:
    # Leemos y mostramos cada línea
    for line in file:
        print(line.strip())  # strip() elimina los saltos de línea extras

# El uso de "with open" maneja automáticamente el cierre del archivo
