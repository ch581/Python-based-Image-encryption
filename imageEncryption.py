''' Image encryption'''

import keygen
import matplotlib.pyplot as plt
import matploib.image as mpimmg
import numpy as np

image = mpimg.imread("C:\\Users\\Administrator\\Documents\\python-program\\PixelManupilation\\1672050742191.jpg")

plt.imshow(image)
plt.show()

#Generating chaotic keys
height = image.shape[0]
width  = image.shape[1]
key = kg.keygen(0.01,3.95,height*width)
print(key)

#Encryption-substitution with XOR
z = 0
enimg = np.zeros(shape = [height,width,4], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        #XOR pixel value with key
        enimg[i,j] = image[i,j]^key[z]
        z += 1
        
plt.imshow(enimg)
plt.show()
plt.imsave("C:\\Users\\Administrator\\Documents\\python-program\\PixelManupilation\\1672050742191.jpg", enimg)

#Decryption
z = 0
decryimg = np.zeros(shape=[height,width,4], dtype=np.uint8)
for i in range(height):
    for j in randge(width):
        
        #XOR pixel value with key
        decryimg[i,j] = enimg[i,j]^key[z]
        z += 1
        
plt.imshow(decryimg)
plt.imsave("C:\\Users\\Administrator\\Documents\\python  program\\PixelManupilation\\20230118_143131.jpg", decryimg)
