import cv2
import numpy as np
from matplotlib import pyplot as plt
import os 
import copy
    
class DoublyLinkedList:
    class _Node:
        def __init__(self,data) :
            self._elem=data
            # Referência para o próximo elemento
            self._next=None 
            # Elemento anterior
            self._prev=None
        
    def __init__(self):
        self._header = None
        self._trailer = None
        self._length = 0
        
    def empty(self):
           return self._length == 0
        
    def append(self, elemento):
        newNode=self._Node(elemento)
        
        if self.empty():
            self._header=newNode
        else:
           self._trailer._next=newNode
           newNode._prev=self._trailer
           
        self._trailer=newNode
        self._length+=1
    
    def _get_node(self,index):
        pointer=self._header
        for _ in range(index):
            if pointer:
                pointer=pointer._next
            else:
                raise IndexError('Índice fora do alcance')
        return pointer
    
def showInfo(name,year):
    global img
    global cache
    
    image_height=img.shape[0]
    image_width=img.shape[1]
    
    #rectangle
    start_point=(5,image_height-60)
    end_point=(image_width-5,image_height-20)
    color = (255, 0, 0)
    thickness = -1
    
    #text
    org = (8, (image_height-60)+30)
    fontScale = 0.85
    color_font = (255, 255, 255)
    thickness_font = 1
    font = cv2.FONT_HERSHEY_DUPLEX 
    
    cache=copy.deepcopy(img)
    cv2.rectangle(img, start_point, end_point, color, thickness)
    cv2.putText(img,"{name}, {year}".format(name=name,year=year),org, font, fontScale,color_font,thickness_font,cv2.LINE_AA)
    
def clearInfo():
    global img
    img = copy.deepcopy(cache)

def main():
    dll=DoublyLinkedList()
    images=os.listdir('./images')
    length=len(images)

    images_details=[
    {"name":"Imperial Dreams","year":2018},
    {"name":"Iron First","year":2019},
    {"name":"Old Guard","year":2028},
    {"name":"Stranger Things","year":2022}
    ]
    for i in range(0,length):
        dll.append({"image_url":images[i],**images_details[i]})

    
    window_name = 'Image'
    result = np.zeros((360,360,3), np.uint8)
    
    i = 0
    pointer=dll._header

    global img
    global cache

    img = cv2.imread('./images/' + pointer._elem.get("image_url"))
    img = cv2.resize(img, (460, 420))

    cache=img.copy()
    cache=cv2.resize(cache, (420, 420))

    infoCount=0
    while True:
        cv2.imshow(window_name, img)
        key=cv2.waitKey(0) # Esperar qualquer tecla
        print('KEY PRESSED {}'.format(key))
        if key == 105:
            description=pointer._elem.get("name")
            year=pointer._elem.get("year")
            print(infoCount)
            if infoCount < 1:
                showInfo(description,year)
                infoCount+=1
            else:
                clearInfo()
                infoCount=0
            
        
        if key == 100:
            infoCount=0
            i+=1
            print('TECLA D')
            if pointer._next:
                pointer=pointer._next
                
            if pointer:
                img = cv2.imread('./images/' + pointer._elem.get("image_url"))
                img = cv2.resize(img, (460, 420))
            
        if key == 97:
            infoCount=0
            i-=1
            print('TECLA A')
            if pointer._prev:
                pointer=pointer._prev
                
            if pointer:    
                img = cv2.imread('./images/' + pointer._elem.get("image_url"))
                img = cv2.resize(img, (460, 420))
        
        if key == 27:
            break
        
        # cv2.imshow(window_name, img)

    cv2.destroyAllWindows()



main()