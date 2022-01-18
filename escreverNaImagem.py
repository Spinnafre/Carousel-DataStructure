# Example https://theailearner.com/tag/cv2-waitkey/

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os 

images=os.listdir('./images')
length=len(images)

# Window name in which image is displayed
window_name = 'Image'

cv2.namedWindow(window_name)
result = np.zeros((360,360,3), np.uint8) # ((coluna,items,items),data-type)

i = 1

a,b = 10,30

img = cv2.imread('./images/' + images[i])
img = cv2.resize(img, (360, 360)) # (imagem, dimensões)

# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2


while True:
    cv2.imshow(window_name, img)
    key=cv2.waitKey(0) # Espera até pressionar algum botão
     
    if key == -1:
        print('screensaver')
    elif key == 27: # Se pressionar o ESC irá sair
        break
    
    else:
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        #chr() -> irá interpretar qual tecla foi digitada e retornar o valor correspondente
        cv2.putText(img,chr(key),(a+i,b), font, fontScale,color,thickness,cv2.LINE_AA)
        # Se a + i for maior do que o width da imagem então o eixo i (x) irá voltar para o início
        # e b (eixo y) irá incrementar, resumindo, irá quebrar linha sempre que chega no fim da imagem
        if a+i >= img.shape[1]:
            b = b+25
            i = 0
        i +=18
    
cv2.destroyAllWindows()