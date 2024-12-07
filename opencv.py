import cv2

#cargamos la image
imagen =cv2.imread('IA1.jpg')

#mostramos la imagen en una ventana
cv2.imshow('imagen',imagen)

#obtenemos el tamaño de la imagen
alto, ancho=(imagen.shape) [:2]

#calculamos el centro de la imagen
centro= (ancho // 2, alto // 2)

#rotamos la imagen 
angulo=45
matriz=cv2.getRotationMatrix2D(centro,angulo,1.0)

imagen_rotada=cv2.warpAffine(imagen,matriz,(ancho,alto))

#mostramos la imagen rotada en una ventana
cv2.imshow('imagen rotada',imagen_rotada)

#Espere hasta que presione una tecla
cv2.waitKey(0)

#Destruye todas las ventanas
cv2.destroyAllWindows()

