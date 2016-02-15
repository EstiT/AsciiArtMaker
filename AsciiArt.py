#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

#Stephenson, B. "Tutorial 2: Using Images with the SimpleGraphics Library" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).


from SimpleGraphics import *  


def picture (): 
    #get and load picture 
    pic=loadImage(input("What picture do you want to use?: ")) 
    #get the width and height of picture
    w=getWidth(pic) 
    h=getHeight(pic)
    #get red green blue values of each pizel in picture, change picture to be grey scaled
    for x in range (0,w): 
        for y in range (0,h): 
            r,g,b=getPixel(pic,x,y) 
            grey=int((r+g+b)/3) 
            putPixel(pic,x,y,grey,grey,grey) 
    return pic,w,h #return values
            
def terminal(): 
    #ask what colour terminal the user has
    terminal=input("Do you have a [W]hite or [B]lack background? ") 
    #run through as long as the input is not valid
    while terminal!="W" and terminal!="B": 
        print("Error. That is not one of the options.") #if not valid, display error messege
        terminal=input("Do you have a [W]hite or [B]lack background? ") #and ask agian
    return terminal

def white():
    #get the values from the picture function
    pic,w,h=picture() 
    #for every pixel in picture, get the r,g,b values at that position
    #print corrisponding symbol
    for y in range (0,h): 
        for x in range (0,w): 
            r,g,b=getPixel(pic,x,y) 
            if r>250 and g>250 and b>250:#if it is close to or is white
                print(".",end="") #then print a period 
            elif r>245 and g>245 and b>245: #repete for all of the differnt shades (white-grey-black)
                print(",",end="") #change symbol depending on how light/dark it should be
            elif r>224 and g>224 and b>224:
                print(":",end="")
            elif r>192 and g>192 and b>192:
                print("~",end="")
            elif r>160 and g>160 and b>160:
                print("=",end="")
            elif r>128 and g>128 and b>128:
                print("/",end="")
            elif r>96 and g>96 and b>96:
                print("?",end="")
            elif r>64 and g>64 and b>64:
                print("X",end="")
            elif r>32 and g>32 and b>32:
                print("8",end="")
            elif r>15 and g>15 and b>15:
                print("#",end="")
            else: # close to or is black
                print("@",end="")
        print()
          

def black(): #define the black function
    #get values from the picture function
    pic,w,h=picture() 
    #for every pixel in picture, get the r,g,b values at that position
    #print corrisponding symbol
    for y in range (0,h): 
        for x in range (0,w): 
            r,g,b=getPixel(pic,x,y) 
            if r>250 and g>250 and b>250:#if it is close to or is white
                print("@",end="") #then print an '@' symbol
            elif r>245 and g>245 and b>245: #repeat for all of the differnt shades (white-grey-black)
                print("#",end="")#change symbol depending on how light/dark it should be
            elif r>224 and g>224 and b>224:
                print("8",end="")
            elif r>192 and g>192 and b>192:
                print("X",end="")
            elif r>160 and g>160 and b>160:
                print("?",end="")
            elif r>128 and g>128 and b>128:
                print("/",end="")
            elif r>96 and g>96 and b>96:
                print("=",end="")
            elif r>64 and g>64 and b>64:
                print("~",end="")
            elif r>32 and g>32 and b>32:
                print(":",end="")
            elif r>15 and g>15 and b>15:
                print(",",end="")
            else:  #close to or is black
                print(".",end="")
        print()

def main(): 
    t=terminal() #get input and run terminal function
    #if they have a white terminal
    if t=="W":  
        white() #run white function
    #otherwise t=="B" they have a black terminal
    else : 
        black() #run black function
    

main() 

