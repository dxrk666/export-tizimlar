# -*- coding: utf-8 -*-
"""MD660-23.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13VFnJeFXhnUY4xtgAcCB67KNUCFABZsC
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2

def tashxis(belgi):
  if belgi == "Isitma":
    rasm = cv2.imread('paracetamol.jpg')
    cv2_imshow(rasm)
    return "Paratsetamol iching!"
  elif belgi == "Bosh og'rig'i":
    rasm = cv2.imread('bolnol.jpg')
    cv2_imshow(rasm)
    return "Bolnol iching!"
  elif belgi == "Tish og'rig'i":
    rasm = cv2.imread('qupen.jpg')
    cv2_imshow(rasm)
    return "Qupen iching!"
  elif belgi == "Burun bitishi":
    rasm = cv2.imread('rinoksil.jpg')
    cv2_imshow(rasm)
    return "Rinoksil seping!"
  else:
    rasm = cv2.imread('doctor.jpg')
    cv2_imshow(rasm)
    return "Shifokorga murojaat qiling!"
belgi = input("Kasallik belgisini kiriting: ")
natija = tashxis(belgi)
print(natija)