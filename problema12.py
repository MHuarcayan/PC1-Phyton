def obtener_tipo_mime(archivo):
    # Obtener la extensión del archivo
    extension = archivo.lower().split('.')[-1]

    # Definir el diccionario de extensiones y tipos MIME
    extensiones_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    # Verificar si la extensión está en el diccionario
    if extension in extensiones_mime:
        return extensiones_mime[extension]

    # Si la extensión no está en la lista, devolver 'application/octet-stream'
    return 'application/octet-stream'

# Solicitar al usuario el nombre del archivo
archivo = input("Ingrese el nombre del archivo: ")

# Obtener el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(archivo)

# Imprimir el resultado
print(f"Tipo MIME del archivo '{archivo}': {tipo_mime}")