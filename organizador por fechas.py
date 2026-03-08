import os
import shutil
from datetime import datetime

# El script trabajará en la carpeta donde lo pongas
ruta_actual = os.getcwd()

def organizar_por_año():
    print(f"--- Iniciando organización cronológica en: {ruta_actual} ---")
    archivos = os.listdir(ruta_actual)
    total = 0

    for archivo in archivos:
        # No mover el propio script
        if os.path.isfile(archivo) and archivo != os.path.basename(__file__):
            try:
                # Obtener la fecha de última modificación (es la más precisa en Windows)
                mtime = os.path.getmtime(archivo)
                fecha = datetime.fromtimestamp(mtime)
                año = str(fecha.year) # Extraemos el año (ej: "2021")

                # Crear la carpeta del año si no existe
                if not os.path.exists(año):
                    os.makedirs(año)
                
                # Mover el archivo a su carpeta de año
                shutil.move(archivo, os.path.join(año, archivo))
                total += 1
                if total % 100 == 0:
                    print(f"Procesados {total} archivos...")
            
            except Exception as e:
                print(f"Error con {archivo}: {e}")

    print(f"\n--- ¡Magia completada! {total} archivos organizados por años. ---")
    print("Presiona ENTER para salir...")
    input()

if __name__ == "__main__":
    organizar_por_año()
