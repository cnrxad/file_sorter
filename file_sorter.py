import os
import glob
import shutil

os.chdir("") # <-- insert the path for the program to work

while(True):

    if os.path.exists("documents") == True:
        pass
    else:
        os.mkdir("documents")
        continue
    
    if os.path.exists("images") == True:
        pass
    else:
        os.mkdir("images")
        continue
    
    if os.path.exists("videos") == True:
        pass
    else:
        os.mkdir("videos")
        continue
    
    if os.path.exists("music") == True:
        pass
    else:
        os.mkdir("music")
        continue

    if os.path.exists("multimedia") == True:
        pass
    else:
        os.mkdir("multimedia")
        continue
    break


# documents:

pdf = glob.glob("*.pdf")
doc = glob.glob("*.doc")
docx = glob.glob("*.docx")
odt = glob.glob("*.odt")
txt = glob.glob("*.txt")

# images:

png = glob.glob("*.png")
jpg = glob.glob("*.jpg")
jpeg = glob.glob("*.jpeg")

# videos:

mp4 = glob.glob("*.mp4")
mkv = glob.glob("*.mkv")

# music: 

wav = glob.glob("*.wav")
mp3 = glob.glob("*.mp3")

# multimedia:

py = glob.glob("*.py")
html = glob.glob("*.html")
css = glob.glob("*.css")
js = glob.glob("*.js")
exe = glob.glob("*.exe")
rar = glob.glob("*.rar")
zip = glob.glob("*.zip")

for i in (png):
    shutil.move(i, "images")
for i in (jpg):
    shutil.move(i, "images")
for i in (jpeg):
    shutil.move(i, "images")

for i in (mp4):
    shutil.move(i, "videos")
for i in (mkv):
    shutil.move(i, "videos")

for i in (pdf):
    shutil.move(i, "documents")
for i in (doc):
    shutil.move(i, "documents")
for i in (docx):
    shutil.move(i, "documents")
for i in (odt):
    shutil.move(i, "documents")
for i in (txt):
    shutil.move(i, "documents")


for i in (wav):
    shutil.move(i, "music")
for i in (mp3):
    shutil.move(i, "music")

for i in (py):
    shutil.move(i, "multimedia")
for i in (html):
    shutil.move(i, "multimedia")
for i in (css):
    shutil.move(i, "multimedia")
for i in (js):
    shutil.move(i, "multimedia")
for i in (exe):
    shutil.move(i, "multimedia")
for i in (rar):
    shutil.move(i, "multimedia")
for i in (zip):
    shutil.move(i, "multimedia")
