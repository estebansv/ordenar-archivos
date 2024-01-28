import os

def main():
    # Obtiene la carpeta de origen
    origen = input("Ingrese la carpeta de origen: ")

    # Obtiene las extensiones de archivo a mover
    extensiones = input("Ingrese las extensiones de archivo a mover, separadas por comas: ")
    extensiones = extensiones.split(",")

    # Recorre los archivos de la carpeta de origen
    for archivo in os.listdir(origen):
        # Obtiene la extensión del archivo
        extension = archivo.split(".")[-1]

        # Si el archivo es una carpeta, lo deja intacto
        if os.path.isdir(os.path.join(origen, archivo)):
            continue

        # Si la extensión está en la lista de extensiones a mover
        if extension in extensiones:
            # Crea la carpeta de destino
            destino = os.path.join(origen, extension)
            if not os.path.exists(destino):
                os.makedirs(destino)

            # Mueve el archivo a la carpeta de destino
            os.rename(os.path.join(origen, archivo), os.path.join(destino, archivo))
        
        # Agrega el archivo a la carpeta "otros"
        else:
            
            destino = os.path.join(origen, "otros")
            if not os.path.exists(destino):
                os.makedirs(destino)

            os.rename(os.path.join(origen, archivo), os.path.join(destino, archivo))

            # Imprime un mensaje de los archivos movidos
            print(f"Archivo {archivo} movido a {destino}")

if __name__ == "__main__":
    main()
    