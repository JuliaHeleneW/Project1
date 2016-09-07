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
images=[image1,image2,image3,image4,image5,image6,image7,image8,image9]
print images
redPixelList=[]
greenPixelList=[]
bluePixelList=[]
myList=[]
for image in images:
    print(image.size)
    for x in range(0,pictureWidth):
        for y in range(0,pictureHeight):
	         for myImage in images:
                 myRed,myGreen,myBlue=myImage.getPixel((x,y))
			         return myRed,myGreen,myBlue
					 
redPixelList.append(myRed)
greenPixelList.append(myGreen)
bluePixelList.append(myBlue)
def medianOdd(myList):
    listLength=len(myList)
    sortedValues=sorted(myList)
    middleIndex=((listLength+1)/2)-1
return sortedValues[middleIndex]
medianRed=medianOdd(redPixelList)
medianGreen=medianOdd(greenPixelList)
medianBlue=medianOdd(bluePixelList)
redPixelList.remove(myRed)
greenPixelList.remove(myGreen)
bluePixelList.remove(myBlue)
for x in range(0,pictureWidth):
    for y in range(0,pictureWidth)
	     outputImage=new.image(x,y,medianRed,medianGreen,medianBlue)
		 print outputImage

		
