""" [App.py Documentation]
    
    Southern Utah University
    CS-4800-01-S23

    Drisinski, Riley
    Larm, Dayna Mitty
    Small, Hannah """

import ctypes
import os

from src.CodeMatch import CodeMatch
from src.const.DIR import DIR


def app():
    """ Runs the CodeMatch Program """
    DIR.app_directory = os.path.dirname(__file__) + "\\"
    myappid = "CapstoneS23-SUU"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    codematch = CodeMatch()
    codematch.run()


# Run the program
app()
