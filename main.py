
import os
import copy

def removeTempFiles(path, suffix='.DS_Store'):
    if path.endswith(suffix):
        print(f'Removing file: {path}')
        os.remove(path)
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            removeTempFiles(path + '/' + filename, suffix)

removeTempFiles('sampleFiles')
import sys, os
def runPipCommand(pipCommand, pipPackage=None):
    # get quoted executable path
    quote = '"' if 'win' in sys.platform else "'"
    executablePath = f'{quote}{sys.executable}{quote}'
    # first upgrade pip:
    command = f'{executablePath} -m pip -q install --upgrade pip'
    os.system(command)
    # input the package from the user if it's not supplied in the call:
    if pipPackage == None:
        pipPackage = input(f'Enter the pip package for {pipCommand} --> ')
    # then run pip command:
    command = f'{executablePath} -m pip {pipCommand} {pipPackage}'
    os.system(command)

runPipCommand('install --upgrade', 'cmu_graphics')




import math
from cmu_graphics import *

from screen1 import *
from screen2 import *

##################################
# App
##################################

def onAppStart(app):
    print('In onAppStart')

def onAppStop(app):
    print('In onAppStop')



##################################
# main
##################################

def main():
    runAppWithScreens(initialScreen='screen1', width=1000,height=1000)

main()
 




 