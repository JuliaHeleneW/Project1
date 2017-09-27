#import image stuff from Pillow
from PIL import Image
#open the 9 images
image1=Image.open("1.png")
image2=Image.open("2.png")
image3=Image.open("3.png")
image4=Image.open("4.png")
image5=Image.open("5.png")
image6=Image.open("6.png")
image7=Image.open("7.png")
image8=Image.open("8.png")
image9=Image.open("9.png")
#store the 9 images in a list
images=[image1,image2,image3,image4,image5,image6,image7,image8,image9]
#create pixel lists to store the pixel data
redPixelList=[]
greenPixelList=[]
bluePixelList=[]
#create a new empty image with the size of the other images
outputImage=Image.new("RGB",(495,557))
#load the empty image
outputImagePX=outputImage.load()
#define a function to set the output pixels
def pixelForOutput(image):
    #3 global variables to store the RGB values
    global medianRed,medianGreen,medianBlue
    #load the image
    pix=image.load()
    #for each pixel
    for x in range(0,495):
        for y in range(0,557):
               #set the medians as RGB values
               pix[x,y]=medianRed,medianGreen,medianBlue
#determine the size of the images
width,height=(495,557)
#loop going through the width
for x in range(0,width):
    #and the height of the images
    for y in range(0,height):
        #for every image
        for Image in images:
                #get the RGB values of every pixel
                red, green, blue = Image.getpixel((x,y))
                #store the RGB values of the pixels in 3 lists, one for each value of each pixel
                redPixelList.append(red)
                greenPixelList.append(green)
                bluePixelList.append(blue)
                #define the median of a list
                def median(list):
                #sort the list
                    srtd = sorted(list)
                    #get the length of the list
                    alen = len(srtd)
                    #return the int of the median
                    return int(0.5*( srtd[(alen-1)//2] + srtd[alen//2]))
        #get the median values for the pixel lists
        medianRed=median(redPixelList)
        medianGreen=median(greenPixelList)
        medianBlue=median(bluePixelList)
        rgbVal=(medianRed,medianGreen,medianBlue)
        #remove the data from the pixel lists so the median for the next pixel can be defined
        redPixelList.clear()
        greenPixelList.clear()
        bluePixelList.clear()
        #set the pixel
        outputImagePX[x,y]=rgbVal
        #use the function on the empty image we created
        pixelForOutput(image10)
#show the image
outputImage.save("result.png")
outputImage.show()
#image10.show()
