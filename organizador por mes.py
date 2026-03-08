import os
import shutil
from datetime import datetime

# Carpeta de trabajo
ruta_actual = os.getcwd()

# Diccionario para que los meses salgan con nombre y no solo número
nombres_meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

def organizar_por_año_y_mes():
    print(f"--- Iniciando Organización PROFESIONAL en: {ruta_actual} ---")
    archivos = os.listdir(ruta_actual)
    total = 0

    for archivo in archivos:
        # Ignoramos carpetas y el propio script
        if os.path.isfile(archivo) and archivo != os.path.basename(__file__):
            try:
                # Obtenemos la fecha de modificación
                mtime = os.path.getmtime(archivo)
                fecha = datetime.fromtimestamp(mtime)
                
                año = str(fecha.year)
                mes_num = fecha.month
                nombre_mes = f"{mes_num:02d} {nombres_meses[mes_num]}" # Ejemplo: "05 Mayo"

                # Creamos la ruta: Año / Mes
                ruta_destino = os.path.join(año, nombre_mes)

                # Si no existe la estructura de carpetas, Python la crea
                if not os.path.exists(ruta_destino):
                    os.makedirs(ruta_destino)
                
                # Movemos el archivo
                shutil.move(archivo, os.path.join(ruta_destino, archivo))
                total += 1
                
            except Exception as e:
                print(f"No se pudo mover {archivo}: {e}")

    print(f"\n--- ¡Misión cumplida! {total} archivos organizados perfectamente. ---")
    print("Presiona ENTER para cerrar la ventana y disfrutar el orden...")
    input()

if __name__ == "__main__":
    organizar_por_año_y_mes()
