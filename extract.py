import os

# Ruta de la carpeta
folder_path = r"C:\Users\A2905\OneDrive\Escritorio\hook-theme-master\assets\Obsidian\portafolio"

# Obtener los nombres de los archivos en la carpeta
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Crear rutas completas para cada archivo
file_paths = [f"assets/Obsidian/portafolio/{file_name}" for file_name in file_names]

# Generar el formato del array para JavaScript
js_array = "const images = [\n" + ",\n".join([f'    "{path}"' for path in file_paths]) + "\n];"

# Guardar en un archivo JS o imprimir en consola
output_path = os.path.join(folder_path, "images_array.js")
with open(output_path, "w", encoding="utf-8") as js_file:
    js_file.write(js_array)

print("Array de imágenes generado y guardado en:", output_path)
