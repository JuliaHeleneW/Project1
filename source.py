from PIL import Image
image1=Image.open("1.png")
image2=Image.open("2.png")
image3=Image.open("3.png")
image4=Image.open("4.png")
image5=Image.open("5.png")
image6=Image.open("6.png")
image7=Image.open("7.png")
image8=Image.open("8.png")
image9=Image.open("9.png")
image10=Image.new("RGB",(495,557),"white")
images=[image1,image2,image3,image4,image5,image6,image7,image8,image9]
redPixelList=[]
greenPixelList=[]
bluePixelList=[]
for Image in images:
    width,height=Image.size
    for x in range(0,width):
        for y in range(0,height):
	         for Image in images:
                  red, green, blue = Image.getpixel((x,y))
                  redPixelList.append(red)
                  greenPixelList.append(green)
                  bluePixelList.append(blue)
                  redPixelList.sort()
                  greenPixelList.sort()
                  bluePixelList.sort()
                  from statistics import median
                  medianRed=median(redPixelList)
                  medianGreen=median(greenPixelList)
                  medianBlue=median(bluePixelList)
                  redPixelList.remove(red)
                  greenPixelList.remove(green)
                  bluePixelList.remove(blue)
                  pix=image10.load()
                  for x in range(0,width):
                      for y in range(0,height):
                          pix[x,y]=medianRed,medianGreen,medianBlue
                          image10=Image.save("D://Image/outputImage.png")
