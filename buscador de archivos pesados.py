import os

def radar_de_gigantes():
    disco_raiz = 'C:\\'
    print(f"--- 🛰️ INICIANDO RADAR EN DISCO: {disco_raiz} ---")
    print("Escaneando... Esto no moverá ningún archivo.")
    
    lista_archivos = []

    # Caminamos por todo el disco
    for carpeta_actual, subcarpetas, archivos in os.walk(disco_raiz):
        for nombre in archivos:
            try:
                ruta_completa = os.path.join(carpeta_actual, nombre)
                
                # Obtenemos el tamaño en Megabytes
                tamaño_mb = os.path.getsize(ruta_completa) / (1024 * 1024)
                
                # Solo nos interesan cosas que pesen más de 100MB
                if tamaño_mb > 100:
                    lista_archivos.append((nombre, tamaño_mb, carpeta_actual))
            except:
                # Si no tenemos permiso para ver un archivo, simplemente lo saltamos
                continue

    # Ordenamos de mayor a menor peso
    lista_archivos.sort(key=lambda x: x[1], reverse=True)

    print("\n--- 📝 REPORTE DE ARCHIVOS PESADOS ---")
    print(f"{'ARCHIVO'.ljust(30)} | {'PESO (MB)'.ljust(10)} | {'UBICACIÓN'}")
    print("-" * 80)
    
    # Mostramos los 20 más grandes
    for i, (nom, tam, carp) in enumerate(lista_archivos[:20], 1):
        print(f"{nom[:30].ljust(30)} | {str(round(tam, 2)).ljust(10)} | {carp}")

    print("-" * 80)
    print(f"\nSe encontraron {len(lista_archivos)} archivos mayores a 100MB.")
    input("\nPresiona ENTER para cerrar el radar...")

if __name__ == "__main__":
    radar_de_gigantes()
