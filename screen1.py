from cmu_graphics import *

##################################
# Screen1
##################################

from PIL import Image






def screen1_onAppStart(app):
    print('In screen1_onAppStart')
    app.printBoard=False
    app.enterGame=False
    app.chooseDifficulty=False
    app.mode="Easy"
    app.activatedCounter1 = 0
    app.image1 = Image.open('sudoku poster.png')

    app.imageFlipped = app.image1.transpose(Image.FLIP_LEFT_RIGHT)
    # Convert each PIL image to a CMUImage for drawing
    app.image1 = CMUImage(app.image1)
    app.image2=Image.open("cartoon character.jpeg")
    app.image2=CMUImage(app.image2)
    app.imageFlipped = CMUImage(app.imageFlipped)
    app.image3=Image.open("conversation box.png")
    app.image3=CMUImage(app.image3)

def screen1_onScreenActivate(app):
    print('In screen1_onScreenActivate')
    app.activatedCounter1 += 1

def screen1_onKeyPress(app, key):
    if key == 's': setActiveScreen('screen2')
   
def screen1_onMousePress(app,mouseX,mouseY):
    
    if (mouseX>400 and mouseX<580) and (mouseY>600 and mouseY<740):
        app.chooseDifficulty=True
        app.enterGame=True
    if (mouseX<550 and mouseX>450) and (mouseY>500 and mouseY<600):
        app.mode="Evil"
        app.printBoard=True
        setActiveScreen('screen2')

    elif (mouseX<550 and mouseX>450) and (mouseY>200 and mouseY<300):
        app.mode="Easy"
        app.printBoard=True
        setActiveScreen('screen2')
    elif (mouseX<550 and mouseX>450) and (mouseY>350 and mouseY<450):
        app.mode="Medium"
        app.printBoard=True
        setActiveScreen('screen2')
    
    print(app.mode)


def screen1_redrawAll(app):
    
    if not app.enterGame:
        pilImage = app.image1.image
        drawImage(app.image1, 500, 400, align='center',
                
                width=pilImage.width*1.75,
                height=pilImage.height*1.75)
        drawRect(400,600,180,140,fill=rgb(255,255,0),border=rgb(51,102,0),borderWidth=20)
        drawLabel("Play",490,670,fill=rgb(0,25,51),size=40,bold=True,border="white")
    else:
        if app.chooseDifficulty and not app.printBoard:
           drawScreen1Features(app)
def drawScreen1Features(app) :
    pilImage = app.image1.image
    drawImage(app.image2,10,400,width=pilImage.width//1.5,height=pilImage.height//1.5)
    drawImage(app.image3,10,0,width=pilImage.width//1.2,height=pilImage.height//1.2)
    drawRect(450,200,180,100,fill=rgb(229,204,255),border=rgb(102,178,255),borderWidth=10)
    drawRect(450,350,180,100,fill=rgb(229,204,255),border=rgb(102,178,255),borderWidth=10)
    drawRect(450,500,180,100,fill=rgb(229,204,255),border=rgb(102,178,255),borderWidth=10)
    drawLabel("We have three levels in total.",220,160,size=17,bold=True)
    drawLabel("Easy has the most existing values,",220,190,size=17,bold=True)
    drawLabel("evil is the most difficult one.",220,220,size=17,bold=True)
    drawLabel("Easy",540,250,size=20,bold=True,fill=rgb(0,51,102))
    drawLabel("Medium",540,400,size=20,bold=True,fill=rgb(0,51,102))
    drawLabel("Evil",540,550,size=20,bold=True,fill=rgb(0,51,102))       
if __name__ == '__main__':
    main()
