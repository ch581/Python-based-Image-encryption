#Python code for encrypting images

#take path of image as input
path = r"C:\Users\Administrator\Documents\python  program\PixelManupilation\3b976c28e0cc444da9db3f7972ec923e.jpg"

#taking encryption key as input
key = int(input('Enter encryption key of image : '))

#print image path and key
print("The path of the file is : " + path)
print(key)

#open file for reading purpose 
Fil = open(path, 'rb')

#Storing image data in a variable
image = Fil.read()
Fil.close()

#converting image into bytearray to perfom easy encryption on numeric data
image = bytearray(image)

#performing XOR operation on each value of bytearray
for index, values in enumerate(image):
    image[index] = values ^ key
    
#opening file for writing
Fil = open(path, "wb")

#writing encrypted data in image
Fil.write(image)
Fil.close()
print('Image is Encryted....')