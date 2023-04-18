

from cmu_graphics import *
import math
import random
import os
import copy
import time
##################################
# Screen2
##################################

  



def screen2_onAppStart(app):
    print('In screen2_onAppStart')
    
    resetGame(app)

def resetGame(app):
    
    print([app.mode.lower()])
    app.board=loadBoard(readFile(random.choice(loadBoardPaths([app.mode.lower()]))))
    
    app.rows = 9
    app.cols = 9
    app.boardLeft = 115
    app.boardTop = 150
    app.boardWidth = 600
    app.boardHeight = 600
    app.cellBorderWidth = 0.5
    app.selection = None
    app.gameOver=False
    app.autoCandidateMode=False
    app.boxfill=rgb(255,255,204)
    app.legals=[]
    app.hightlighted=False
    app.drawErrorDot=False
    app.errors=[]
    app.getHint1=False
    app.solution=solveSudoku(app.board)
    app.userWin=False
    app.userlose=False
    
def screen2_onScreenActivate(app):
    print('In screen2_onScreenActivate')
def loadBoardPaths(filters):
        boardPaths = [ ]
        for filename in os.listdir(f'boards/'):
            if filename.endswith('.txt'):
                if hasFilters(filename, filters):
                    boardPaths.append(f'boards/{filename}')
        return boardPaths

def hasFilters(filename, filters=None):
       
        if filters == None or filters==[None]: return True
        for filter in filters:
            if filter not in filename:
                return False
        return True    




def readFile(path):
    with open(path, "rt") as f:
        return f.read()
 
def loadBoard(contents):
    
    board=[]
    for line in contents.splitlines():
        rowList=[]
        entries=line.split()
        for value in entries:
            rowList.append(int(value))
        board.append(rowList) 
    
    return board

def createLegals(board,row,col):
    legals=[]
    
    if board[row][col]!=0:
        return []
    for val in range(1,10):
        
        
        if notInCol(val,col,board) and notInRow(val,row,board) and notInBlocks(val,row,col,board):
            legals.append(val)
           
    
    return legals    


def gameOver(app):
    if app.board==app.solution:
       app.userWin=True
    elif not hasEmptyCell(board) and app.board!=app.solution:
        app.userLose=True


def hasEmptyCell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                return True
    return False



    
def screen2_onKeyPress(app, key):
    
    if key=="s":
        resetGame(app)
    if key=="1" and app.selection!=None:
        
        row,col=app.selection
        app.legals=createLegals(app.board,row,col)
        
        app.board[row][col]=1
        
        
        
        if int(key) not in app.legals:
           
           app.drawErrorDot=True
           app.errors.append(key)
          
        else:
           removeLegals(app.board,row,col,key)
        
        

    if key=="2" and app.selection!=None:
      
       row,col=app.selection
       app.legals=createLegals(app.board,row,col)
       app.board[row][col]=2
       
       if int(key) not in app.legals:
           app.drawErrorDot=True
           app.errors.append(key)
       else:
           removeLegals(app.board,row,col,key)
        
       
    if key=="3" and app.selection!=None:
      
       row,col=app.selection
       app.legals=createLegals(app.board,row,col)
       app.board[row][col]=3
       
       if int(key) not in app.legals:
          app.drawErrorDot=True
          app.errors.append(key)
       else:
           removeLegals(app.board,row,col,key)
        
       
       
    if key=="4" and app.selection!=None:
      
       row,col=app.selection
       app.legals=createLegals(app.board,row,col)
       app.board[row][col]=4
       
       if int(key) not in app.legals:
           app.drawErrorDot=True
           app.errors.append(key)
       else:
           removeLegals(app.board,row,col,key)
        
       
    if key=="5" and app.selection!=None:
      
       row,col=app.selection
       app.legals=createLegals(app.board,row,col)
       app.board[row][col]=5
       
       if int(key) not in app.legals:
           app.drawErrorDot=True
           app.errors.append(key)
       else:
           removeLegals(app.board,row,col,key)
        
       app.drawErrorDot=False
    if key=="6" and app.selection!=None:
       
       row,col=app.selection
       app.legals=createLegals(app.board,row,col)
       app.board[row][col]=6
       
       if int(key) not in app.legals:
          app.drawErrorDot=True
          app.errors.append(key)
       else:
           removeLegals(app.board,row,col,key)
        
       
    if key=="7" and app.selection!=None:
       
       row,col=app.selection
       app.legals=createLegals(app.board,row,col)
       app.board[row][col]=7
       
       if int(key) not in app.legals:
          app.drawErrorDot=True
          app.errors.append(key)
       else:
           removeLegals(app.board,row,col,key)
       
      
            
    if key=="8" and app.selection!=None:
       
       row,col=app.selection
       app.legals=createLegals(app.board,row,col)
       app.board[row][col]=8
       
       if int(key) not in app.legals:
          app.drawErrorDot=True
          app.errors.append(key)
       else:
           removeLegals(app.board,row,col,key)
        
       
       
       
    if key=="9" and app.selection!=None:
      
       row,col=app.selection
       app.legals=createLegals(app.board,row,col)
       app.board[row][col]=9
       
       if int(key) not in app.legals:
          app.drawErrorDot=True
          app.errors.append(key)
           
       else:
           removeLegals(app.board,row,col,key)
       
       
       
    elif key=="backspace" and app.selection!=None:
         row,col=app.selection
         app.board[row][col]=0
         app.selection=None
    
            
            
    print(app.errors)         



           
                 
            
            

def drawErrorDot(app,cellLeft,cellWidth,cellTop,cellHeight):
    
    drawCircle(cellLeft+cellWidth-5,cellTop+cellHeight-5,4,fill="red") 
def notInBlocks(val,row,col,board):
    
    x0=row//3*3
    y0=col//3*3

    for x in range(x0,x0+3):
        for y in range(y0,y0+3):
            
            if board[x][y]==val:
               
               return False
    return True

def notInRow(val,row,board)  :
    
    rowList=board[row]
        
    if val in rowList:
        return False
    return True

def notInCol(val,colNum,board):
    colL=[]
    for col in range(9):
        colList=[]
        for row in range(9):

            num=board[row][col]
            colList.append(num)
        colL.append(colList)  
    
    if val in colL[colNum]:
        return False
    return True  



def repr2dList(L):
    if (L == []): return '[]'
    output = [ ]
    rows = len(L)
    cols = max([len(L[row]) for row in range(rows)])
    M = [['']*cols for row in range(rows)]
    for row in range(rows):
        for col in range(len(L[row])):
            M[row][col] = repr(L[row][col])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(M[row][col]) for row in range(rows)])
    output.append('[\n')
    for row in range(rows):
        output.append(' [ ')
        for col in range(cols):
            if (col > 0):
                output.append(', ' if col < len(L[row]) else '  ')
            output.append(M[row][col].rjust(colWidths[col]))
        output.append((' ],' if row < rows-1 else ' ]') + '\n')
    output.append(']')
    return ''.join(output)

def print2dList(L):
    print(repr2dList(L))


def printLegals(self):
        colWidth = 4
        for col in range(9):
            colWidth = max(colWidth, 1+max([len(self.legals[row][col]) for row in range(9)]))
        for row in range(9):
            for col in range(9):
                label = ''.join([str(v) for v in sorted(self.legals[row][col])])
                if label == '': label = '-'
                print(f"{' '*(colWidth - len(label))}{label}", end='')
            print()

            

def screen2_drawCandidates(app,board):
    for row in range(app.rows):
        for col in range(app.cols):
            cellLeft, cellTop = screen2_getCellLeftTop(app, row, col)
            cellWidth, cellHeight = screen2_getCellSize(app)
            
            
        
            position=(row,col)
            candidates=createLegals(board,row,col)
            for num in candidates:
                drawLabel(f"{num}",cellLeft+math.floor(cellWidth/9)*2*(1+num%4),cellTop+math.floor(cellHeight/9)*2*(1+num//4),size=10,fill="green")
def removeLegals(board,row,col,val):
    for m in range(9):
        if val in createLegals(board,m,col):
           app.legals.remove(val) 
    for n in range(9):
        if val in createLegals(board,row,n):
            app.legals.remove(val)


def screen2_onMousePress(app, mouseX, mouseY):
    
    selectedCell = screen2_getCell(app, mouseX, mouseY)
    
    if selectedCell != None:
       app.drawErrorDot=False
      
       app.selection = selectedCell
          
    if (mouseX<(760+15) and mouseX>(760-15)) and (mouseY<(400+15) and mouseY>(400-15)):
        app.autoCandidateMode = not app.autoCandidateMode
        if app.boxfill==rgb(255,255,204):
           app.boxfill=rgb(51,255,51)
        else:
            app.boxfill=rgb(255,255,204)
    if (mouseX<850 and mouseX>800) and (mouseY<225 and mouseY>200):
        app.getHint1=not app.getHint1
    if (mouseX<130 and mouseX>50) and (mouseY<120 and mouseY>80):
        setActiveScreen('screen1')
        drawScreen1Features(app)




def  screen2_redrawAll(app):
    drawLabel('Screen 2', app.width/2, 30, size=16)
    
    drawLabel('Press s to change the screen to screen1', app.width/2, 70, size=16)
   
    drawLabel("Sudoku", app.width/2, 100, size=25,bold=True,fill="orange")
    screen2_drawBoard(app)
    screen2_drawBoardBorder(app)
    screen2_drawValue(app,app.board)
    screen2_drawBlockBorder(app)
    
    drawRect(800,200,50,25,border="black",fill=rgb(238,223,223))
    drawLabel("Hint 1",825,215,size=16)
    drawHint1(app)
    screen2_drawHintBox(app)
    drawRect(50,100,80,40,border="black",fill=rgb(238,223,223))
    drawLabel("Back",90,120,size=20)

    if app.autoCandidateMode:
        
        screen2_drawCandidates(app,app.board)
    if app.drawErrorDot:
       row,col=app.selection
       cellLeft, cellTop = screen2_getCellLeftTop(app, row, col)
       cellWidth, cellHeight = screen2_getCellSize(app)
       drawErrorDot(app,cellLeft,cellWidth,cellTop,cellHeight)
       
    if app.userWin:
        drawLabel("YOU WIN!",400,400,bold=True,size=40)
    elif app.userlose:
        drawLabel("SORRY,YOU LOSE!",400,400,bold=True,size=40)


def screen2_drawHintBox(app):
    drawRect(760,400,15,15,border="black",fill=app.boxfill)
    drawLabel("Auto Candidate Mode",845,405,size=13)
def screen2_drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            screen2_drawCell(app,row,col,app.board)

def screen2_drawBoardBorder(app):
    # draw the board outline (with double-thickness):
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def screen2_drawBlockBorder(app):
    cellWidth, cellHeight = screen2_getCellSize(app)
    print(cellWidth,cellHeight)
    for row in range(0,app.rows,3):
       
        
        drawLine(app.boardLeft,app.boardTop+row*(cellHeight),app.boardLeft+app.boardWidth,app.boardTop+row*(cellHeight),fill="black",lineWidth=4)
    for col in range(0,app.cols,3):
        
        drawLine(app.boardLeft+col*(cellWidth),app.boardTop,app.boardLeft+col*(cellWidth),app.boardTop+app.boardHeight,fill="black",lineWidth=4)
    drawLine(app.boardLeft,app.boardTop+app.boardHeight,app.boardLeft+app.boardWidth,app.boardTop+app.boardHeight,fill="black",lineWidth=4)
    drawLine(app.boardLeft+app.boardWidth,app.boardTop,app.boardLeft+app.boardWidth,app.boardTop+app.boardHeight,fill="black",lineWidth=4)
def screen2_drawValue(app,board):
            
    
    for row in range(app.rows):
        for col in range(app.cols):
            cellLeft, cellTop = screen2_getCellLeftTop(app, row, col)
            cellWidth, cellHeight = screen2_getCellSize(app)
            
            centerX,centerY=cellLeft+cellWidth//2,cellTop+cellHeight//2
            if board[row][col]!=0:

               drawLabel(f"{board[row][col]}",centerX,centerY,size=25,bold=True)

def screen2_getCell(app, x, y):
    dx = x - app.boardLeft
    dy = y - app.boardTop
    cellWidth, cellHeight = screen2_getCellSize(app)
    row = math.floor(dy / cellHeight)
    col = math.floor(dx / cellWidth)
    if (0 <= row < app.rows) and (0 <= col < app.cols):
      return (row, col)
    else:
      return None
def screen2_drawCell(app, row, col,board):
    cellLeft, cellTop = screen2_getCellLeftTop(app, row, col)
    cellWidth, cellHeight = screen2_getCellSize(app)
    value=board[row][col]
    if (row, col) == app.selection:
        fillColor = rgb(153,255,255)
    elif value!=0 and not app.drawErrorDot:
        fillColor=rgb(192,192,192)
    

    else:
        fillColor=None
    
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=fillColor, border='black',
             borderWidth=app.cellBorderWidth)

def screen2_getCellLeftTop(app, row, col):
    cellWidth, cellHeight = screen2_getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def screen2_getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows

    return (cellWidth, cellHeight)



def solveSudoku(board):
    newboard=copy.deepcopy(board)
    
    row,col=findEmptyCellWithLeastLegals(newboard)
    
    return solve(newboard,row,col)

def findEmptyCellWithLeastLegals(newboard):
    rows,cols=len(newboard),len(newboard[0])
    bestLegals=9
    bestPosition=(0,0)
    for i in range(rows):
        for j in range(cols):
            legals=createLegals(newboard,i,j)
            if newboard[i][j]==0 and len(legals)<bestLegals:
                bestLegals=len(legals)
                bestPosition=(i,j)
    
    return bestPosition
    
def solve(newboard,row,col):
    print(row,col)
    rows,cols=len(newboard),len(newboard[0])
    if (row==rows-1) and (col==cols-1):
        return newboard
    
    
       
    legals=createLegals(newboard,row,col)
   
    for num in legals:
        
        newboard[row][col]=num
        print(newboard)
        if newboard[row][col]!=0:
            
           solution=solve(newboard,row,col+1)
        
           if solution!=None:
               
               return solution
           
            
               
        newboard[row][col]=0
    
    return None
    
    

            
def getHint1(board):
    leastLegals=9
    bestPos=(0,0)

    for row in range(9):
        for col in range(9):
            legals=createLegals(app.board,row,col)
            
            if len(legals)!=0 and len(legals)<leastLegals:
                leastLegals=len(legals)
                bestPos=(row,col)

   
    return bestPos


def drawHint1(app):
    
    highlightedx,highlightedy=getHint1(app.board)
    
    cellLeft, cellTop = screen2_getCellLeftTop(app,highlightedx,highlightedy)
    cellWidth, cellHeight = screen2_getCellSize(app)
    if app.getHint1:
       drawStar(cellLeft+cellWidth//2, cellTop+cellHeight//2, 15, 5, fill='pink', border='black',
             roundness=20)
    


 
