from originizer import originize
from appJar import gui
from secrets import choice
import os, os.path

AWAIT_PHRASES = [
    "I await your command...",
    "READY."
]
def awaitPhrase():
    setPTxt( choice(AWAIT_PHRASES) )

def setPTxt(p: str):
    app.setLabel("pTxt", p)

def correctSlashes(fn:str):
    if os.name == "nt":
        return fn.replace('/', '\\')

def chooseFile(b):
    app.thread(_chooseFile, b, app)

def _chooseFile(b, app):
    ifxml = app.openBox("FNF Originizer - Open", fileTypes=[('XML files', '*.xml')])
    ifpng = os.path.splitext(ifxml)[0]+".png"
    ofora = os.path.basename( os.path.splitext(ifxml)[0] )+".ora"
    if not os.path.exists(ifpng):
        app.errorBox(
            "FNF Originizer - Error",
            "No PNG is associated with the XML you selected.\n"+
            f"(I'm looking for a file called '{ifpng}'!)"
        )
        return
    originize(ifpng, ifxml, ofora, setPTxt)
    setPTxt("Finished!\nThe .ora file was placed in the application directory.")
    if app.getCheckBox("Open .ora file after processing"):
        setPTxt("Finished!\nThe .ora file should open soon.")
        os.startfile(ofora)
    app.after(1000, awaitPhrase())

app = gui("FNF Originizer", "300x300", showIcon=False)

app.addImage("logo", "logo.gif")
app.addLabel("pTxt", "random text goes here")
awaitPhrase()
app.addButton("Browse...", chooseFile)
app.addCheckBox("Open .ora file after processing")

app.go()