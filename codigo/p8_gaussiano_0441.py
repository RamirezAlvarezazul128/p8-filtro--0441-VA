import cv2

# Cargar la imagen desde la raíz del proyecto
imagen = cv2.imread("imagenes/cisne original 0441.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen. Verifica que el archivo 'cisne original 0441.jpg' esté en la carpeta 'imagenes'.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen suavizada - Filtro Gaussiano", imagen_suavizada)

# Guardar resultado en la carpeta resultados
cv2.imwrite(
    "resultados/cisne_gaussiano.jpg",
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("resultados/cisne_gaussiano.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Programa realizado por Ramirez Azul NC 0441")