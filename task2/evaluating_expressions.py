from PIL import Image
import pytesseract
img = Image.open('/home/ashish/Pictures/Screenshots/ash.png')
text = pytesseract.image_to_string(img) 
print(text)
expression=text.strip()
answer= eval(expression) 
print(answer)



    

