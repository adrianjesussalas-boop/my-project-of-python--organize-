import os
from datetime import datetime

ruta_raiz = 'C:/'

def escaneo_total():
    
    print("---Iniciando scaneo de todo el pc---")
    
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nombre_reporte = f"reporte_completo_{fecha}.txt"
    archivos_encontrados = 0
    
    try:
        with open(nombre_reporte, "w", encoding="utf-8") as f:
            f.write(f"-Analisis del almacenamiento\n")
            f.write(f"ADRIAN SALAS\n")
            f.write(f"FECHA: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            f.write("-" * 60 + "\n\n")

            # Corregido: carpeta_actual con "a"
            for carpeta_actual, subcarpetas, archivos in os.walk(ruta_raiz):
                for archivo in archivos:
                    try:
                        ruta_completa = os.path.join(carpeta_actual, archivo)
                        tamano_mb = os.path.getsize(ruta_completa) / (1024 * 1024)
                        
                        if tamano_mb > 500:
                            f.write(f"ARCHIVO: {archivo}\n")
                            f.write(f"TAMAÑO: {tamano_mb:.2f} MB\n")
                            f.write(f"RUTA: {carpeta_actual}\n")
                            f.write("-" * 40 + "\n")
                            archivos_encontrados += 1
                    except:
                        continue
            
                        f.write(f"\nFIN DEL REPORTE. SE ENCONTRARON {archivos_encontrados} ARCHIVOS PESADOS.")
            
        print(f"\n✅ ¡LISTO! Escaneo terminado.")
        print(f"Se encontraron {archivos_encontrados} archivos de más de 500MB.")
        print(f"Todo quedó guardado en: {nombre_reporte}")

    except Exception as e:
        print(f"❌ Error al crear el reporte: {e}")

if __name__ == "__main__":
    
    escaneo_total()
