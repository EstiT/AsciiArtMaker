#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

#Stephenson, B. "Tutorial 2: Using Images with the SimpleGraphics Library" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).


from SimpleGraphics import * 


def picture (): 
    #ask the user what picture they want to use and load the picture
    pic=loadImage(input("What picture do you want to use?: ")) 
    w=getWidth(pic) #get the width of the picture
    h=getHeight(pic) #get the height of the picture
    for x in range (0,w): #for every row in the picture
        for y in range (0,h): #and for every coloumn in the picture
            #get the colours for that pixel
            r,g,b=getPixel(pic,x,y) 
            #find the average of the red green adn blue values to get greyscale
            grey=int((r+g+b)/3) 
            #change the picture to be grey scaled
            putPixel(pic,x,y,grey,grey,grey) 
    return pic,w,h 
            
def terminal(): 
    terminal=input("Do you have a [W]hite or [B]lack background? ") 
     #while the input it not valid
    while terminal!="W" and terminal!="B":
            # display error messege
            print("Error. That is not one of the options.") 
             # and ask agian
            terminal=input("Do you have a [W]hite or [B]lack background? ")
    return terminal
    
def white(pic,w,h): 
    name=input("What would you like to call the file? :")
    file=open(name,"a")
    file.write("@ # 8 X ? / = ~ : , ."+"\n")
    for y in range (0,h): #for every row in the picture
        for x in range (0,w): #for every coloumn in the picture
            r,g,b=getPixel(pic,x,y) #get the red green and blue values for the pixtel at that position
            if r>250 and g>250 and b>250:#if it is close to or is white
                print(".",end="") #then print a period 
                file.write(".")
            elif r>245 and g>245 and b>245: #repete for all of the differnt shades (white-grey-black)
                print(",",end="") #change symbol depending on how light/dark it should be
                file.write(",")
            elif r>224 and g>224 and b>224:
                print(":",end="")
                file.write(":")
            elif r>192 and g>192 and b>192:
                print("~",end="")
                file.write("~")
            elif r>160 and g>160 and b>160:
                print("=",end="")
                file.write("=")
            elif r>128 and g>128 and b>128:
                print("/",end="")
                file.write("/")
            elif r>96 and g>96 and b>96:
                print("?",end="")
                file.write("?")
            elif r>64 and g>64 and b>64:
                print("X",end="")
                file.write("X")
            elif r>32 and g>32 and b>32:
                print("8",end="")
                file.write("8")
            elif r>15 and g>15 and b>15:
                print("#",end="")
                file.write("#")
            else: # close to or is black
                print("@",end="")
                file.write("@")
        print() #go to the next line
        file.write("\n")#go to the next line
    file.close()
        
            

def black(pic,w,h):
    name=input("What would you like to call the file? :")
    file=open(name,"a")
    #add the symbols to the first line of the file
    file.write("@ # 8 X ? / = ~ : , ."+"\n")
    
    for y in range (0,h): #for every row in the picture
        for x in range (0,w): #for every coloumn in the picture
            #get the red green and blue values for the pixel at that position
            r,g,b=getPixel(pic,x,y) 
            #if it is close to or is white
            if r>250 and g>250 and b>250:
                #then print an at symbol and add it to the file
                print("@",end="") 
                file.write("@")
            #repete for all of the differnt shades (white-grey-black)
            #change symbol depending on how light/dark it should be
            elif r>245 and g>245 and b>245: 
                print("#",end="")
                file.write("#")
            elif r>224 and g>224 and b>224:
                print("8",end="")
                file.write("8")
            elif r>192 and g>192 and b>192:
                print("X",end="")
                file.write("X")
            elif r>160 and g>160 and b>160:
                print("?",end="")
                file.write("?")
            elif r>128 and g>128 and b>128:
                print("/",end="")
                file.write("/")
            elif r>96 and g>96 and b>96:
                print("=",end="")
                file.write("=")
            elif r>64 and g>64 and b>64:
                print("~",end="")
                file.write("~")
            elif r>32 and g>32 and b>32:
                print(":",end="")
                file.write(":")
            elif r>15 and g>15 and b>15:
                print(",",end="")
                file.write(",")
            else:  #close to or is black
                print(".",end="")
                file.write(".")
        
        print()#go to the next line
        file.write("\n") #go to the next line
    file.close()

def main(): 
    t=terminal() #get input and run terminal function
    #if they have a white terminal
    pic,w,h=picture()
    if t=="W":  
        #do the white function
        white(pic,w,h) 
    #if they have a black terminal
    if t=="B": 
        #do the black function
        black(pic,w,h) 
    

main()