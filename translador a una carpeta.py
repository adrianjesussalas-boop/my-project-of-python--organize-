import os
import shutil

# 1. Solo escribe el nombre, ej: Respaldo_Final_VAIO
nombre_carpeta = input("Escribe el nombre para tu carpeta de respaldo: ")

# 2. Ruta de tu usuario
ruta_usuario = os.path.expanduser("~")
destino_final = os.path.join(ruta_usuario, nombre_carpeta)

if not os.path.exists(destino_final):
    os.makedirs(destino_final)

# LISTA MAESTRA
extensiones_validas = [
    ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".pdf", ".txt",
    ".jpg", ".png", ".jpeg", ".avif", ".mp4", ".mov",
    ".sfc", ".smc", ".fig", ".swc", ".gba", ".gbc", ".gb",
    ".nds", ".n64", ".z64", ".v64", ".nes", ".iso", ".bin",
    ".sav", ".srm", ".state"
]

print(f"\n--- ORGANIZANDO TODO EN: {destino_final} ---")

for raiz, carpetas, archivos in os.walk(ruta_usuario):
    # SEGURIDAD: No entrar en la carpeta que estamos creando
    if nombre_carpeta in raiz or "AppData" in raiz or "Local Settings" in raiz:
        continue

    for archivo in archivos:
        nombre, extension = os.path.splitext(archivo)
        if extension.lower() in extensiones_validas:
            ruta_origen = os.path.join(raiz, archivo)
            ruta_destino = os.path.join(destino_final, archivo)
            
            try:
                print(f"📦 Movido: {archivo}")
                shutil.move(ruta_origen, ruta_destino)
            except:
                continue

print("\n--- ¡TERMINADO! ---")
input("Presiona ENTER para cerrar...")
