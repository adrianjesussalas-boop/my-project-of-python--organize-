import os
import shutil

ruta_documentos = os.getcwd()

sub_categorias = {
    "PDFs": [".pdf"],
    "EXCEL": [".xlsx", ".xls"],
    "WORD": [".docx", ".doc"],
    "POWERPOINT": [".pptx"],
    "TEXTO_NOTAS": [".txt"]
}

def sub_organizar():
    print(f"--- Sub-organizando DOCUMENTOS en: {ruta_documentos} ---")
    archivos = os.listdir(ruta_documentos)
    total = 0

    for archivo in archivos:
        if os.path.isfile(archivo) and archivo != os.path.basename(__file__):
            nombre, extension = os.path.splitext(archivo)
            extension = extension.lower()
            
            for carpeta, extensiones in sub_categorias.items():
                if extension in extensiones:
                    if not os.path.exists(carpeta):
                        os.makedirs(carpeta)
                    
                    try:
                        shutil.move(archivo, os.path.join(carpeta, archivo))
                        print(f"Clasificado: {archivo}")
                        total += 1
                    except Exception as e:
                        print(f"Error con {archivo}: {e}")

    print(f"\n--- ¡Listo! Se clasificaron {total} documentos. ---")
    print("\nPresiona ENTER para cerrar esta ventana...")
    input() # <--- Esto evita que se cierre solo

if __name__ == "__main__":
    sub_organizar()
