import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import time
from colorama import init, Fore, Back, Style
import datetime
import random
from mutagen.mp3 import MP3

init(convert=True)
print(f"{Back.YELLOW}{Fore.BLACK}")
os.system(f"title 🐝 Bumblebee MP3 🐝")
os.system('cls')
cmd = 'mode 110,30'
os.system(cmd)
logo = f"""
    ██████{Fore.RED}╗{Fore.BLACK} ██{Fore.RED}╗{Fore.BLACK}   ██{Fore.RED}╗{Fore.BLACK}███{Fore.RED}╗  {Fore.BLACK} ███{Fore.RED}╗{Fore.BLACK}██████{Fore.RED}╗{Fore.BLACK} ██{Fore.RED}╗   {Fore.BLACK}  ███████{Fore.RED}╗{Fore.BLACK}██████{Fore.RED}╗{Fore.BLACK} ███████{Fore.RED}╗{Fore.BLACK}███████{Fore.RED}╗{Fore.BLACK}    
    ██{Fore.RED}╔══{Fore.BLACK}██{Fore.RED}╗{Fore.BLACK}██{Fore.RED}║  {Fore.BLACK} ██{Fore.RED}║{Fore.BLACK}████{Fore.RED}╗{Fore.BLACK} ████{Fore.RED}║{Fore.BLACK}██{Fore.RED}╔══{Fore.BLACK}██{Fore.RED}╗{Fore.BLACK}██{Fore.RED}║    {Fore.BLACK} ██{Fore.RED}╔════╝{Fore.BLACK}██{Fore.RED}╔══{Fore.BLACK}██{Fore.RED}╗{Fore.BLACK}██{Fore.RED}╔════╝{Fore.BLACK}██{Fore.RED}╔════╝ {Fore.BLACK}   
    ██████{Fore.RED}╔╝{Fore.BLACK}██{Fore.RED}║  {Fore.BLACK} ██{Fore.RED}║{Fore.BLACK}██{Fore.RED}╔{Fore.BLACK}████{Fore.RED}╔{Fore.BLACK}██{Fore.RED}║{Fore.BLACK}██████{Fore.RED}╔╝{Fore.BLACK}██{Fore.RED}║   {Fore.BLACK}  █████{Fore.RED}╗{Fore.BLACK}  ██████{Fore.RED}╔╝{Fore.BLACK}█████{Fore.RED}╗{Fore.BLACK}  █████{Fore.RED}╗{Fore.BLACK}      
    ██{Fore.RED}╔══{Fore.BLACK}██{Fore.RED}╗{Fore.BLACK}██{Fore.RED}║ {Fore.BLACK}  ██║██{Fore.RED}║╚{Fore.BLACK}██{Fore.RED}╔╝{Fore.BLACK}██║██{Fore.RED}╔══{Fore.BLACK}██{Fore.RED}╗{Fore.BLACK}██{Fore.RED}║ {Fore.BLACK}    ██{Fore.RED}╔══╝{Fore.BLACK}  ██{Fore.RED}╔══{Fore.BLACK}██{Fore.RED}╗{Fore.BLACK}██{Fore.RED}╔══╝ {Fore.BLACK} ██{Fore.RED}╔══╝ {Fore.BLACK}     
    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗███████╗██████╔╝███████╗███████{Fore.RED}╗    
    {Fore.RED}╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚══════╝╚═════╝ ╚══════╝╚══════╝    {Fore.BLACK}
                                                                                
                            ███{Fore.RED}╗{Fore.BLACK}   ███{Fore.RED}╗{Fore.BLACK}██████{Fore.RED}╗{Fore.BLACK} ██████{Fore.RED}╗{Fore.BLACK}                                                      
                            ████{Fore.RED}╗ {Fore.BLACK}████║██{Fore.RED}╔══{Fore.BLACK}██{Fore.RED}╗╚════{Fore.BLACK}██{Fore.RED}╗    {Fore.BLACK}                                                 
                            ██{Fore.RED}╔{Fore.BLACK}████{Fore.RED}╔{Fore.BLACK}██{Fore.RED}║{Fore.BLACK}██████{Fore.RED}╔╝{Fore.BLACK} █████{Fore.RED}╔╝ {Fore.BLACK}                                                    
                            ██{Fore.RED}║╚{Fore.BLACK}██{Fore.RED}╔╝{Fore.BLACK}██║██{Fore.RED}╔═══╝  ╚═══{Fore.BLACK}██{Fore.RED}╗ {Fore.BLACK}                                                    
                            ██║ ╚═╝ ██║██║     ██████{Fore.RED}╔╝                                                   
                            ╚═╝     ╚═╝╚═╝     ╚═════╝{Fore.BLACK}"""                                                                                



#pygame.mixer.init()
mixer.init()
mixer.music.load('opening.mp3')
mixer.music.play()





print(logo)
print("""


      .-.         .--''-.
    .'   '.     /'       `.
    '.     '. ,'          |
 o    '.o   ,'        _.-'
  \.--./'. /.:. :._:.'
 .'    '._-': ': ': ': ':
:(#) (#) :  ': ': ': ': ':>-
 ' ____ .'_.:' :' :' :' :'
  '\__/'/ | | :' :' :'
        \  \ \
""")


time.sleep (0.1)
os.system('cls')
print(logo)
print("""

      .-.         .--''-.
    .'   '.     /'       `.
    '.     '. ,'          |
 o    '.o   ,'        _.-'
  \.--./'. /.:. :._:.'
 .'    '._-': ': ': ': ':
:(#) (#) :  ': ': ': ': ':>-
 ' ____ .'_.:' :' :' :' :'
  '\__/'/ | | :' :' :'
        \  \ \
""")


time.sleep (0.1)
os.system('cls')
print(logo)
print("""
      .-.         .--''-.
    .'   '.     /'       `.
    '.     '. ,'          |
 o    '.o   ,'        _.-'
  \.--./'. /.:. :._:.'
 .'    '._-': ': ': ': ':
:(#) (#) :  ': ': ': ': ':>-
 ' ____ .'_.:' :' :' :' :'
  '\__/'/ | | :' :' :'
        \  \ \
""")

time.sleep (0.1)
os.system('cls')
print(logo)
print("""

      .-.         .--''-.
    .'   '.     /'       `.
    '.     '. ,'          |
 o    '.o   ,'        _.-'
  \.--./'. /.:. :._:.'
 .'    '._-': ': ': ': ':
:(#) (#) :  ': ': ': ': ':>-
 ' ____ .'_.:' :' :' :' :'
  '\__/'/ | | :' :' :'
        \  \ \
""")

time.sleep (0.1)
os.system('cls')
print(logo)
print("""


      .-.         .--''-.
    .'   '.     /'       `.
    '.     '. ,'          |
 o    '.o   ,'        _.-'
  \.--./'. /.:. :._:.'
 .'    '._-': ': ': ': ':
:(#) (#) :  ': ': ': ': ':>-
 ' ____ .'_.:' :' :' :' :'
  '\__/'/ | | :' :' :'
        \  \ \
""")


time.sleep (0.06)
os.system('cls')
print(logo)
print("""


    .-.         .--''-.
  .'   '.     /'       `.
  '.     '. ,'          |
    '.o   ,'        _.-'
\.--./'. /.:. :._:.'
'    '._-': ': ': ': ':
#) (#) :  ': ': ': ': ':>-
 ____ .'_.:' :' :' :' :'
'\__/'/ | | :' :' :'
     \  \ \
""")



time.sleep (0.06)
os.system('cls')
print(logo)
print("""


  .-.         .--''-.
.'   '.     /'       `.
'.     '. ,'          |
  '.o   ,'        _.-'
--./'. /.:. :._:.'
   '._-': ': ': ': ':
 (#) :  ': ': ': ': ':>-
___ .'_.:' :' :' :' :'
__/'/ | | :' :' :'
   \  \ \
""")





time.sleep (0.04)
os.system('cls')
print(logo)
print("""


.-.         .--''-.
   '.     /'       `.
     '. ,'          |
'.o   ,'        _.-'
./'. /.:. :._:.'
 '._-': ': ': ': ':
#) :  ': ': ': ': ':>-
_ .'_.:' :' :' :' :'
/'/ | | :' :' :'
 \  \ \
""")

time.sleep (0.03)
os.system('cls')
print(logo)
print("""


         .--''-.
'.     /'       `.
  '. ,'          |
   ,'        _.-'
. /.:. :._:.'
_-': ': ': ': ':
:  ': ': ': ': ':>-
'_.:' :' :' :' :'
| | :' :' :'
 \ \
""")

time.sleep (0.03)
os.system('cls')
print(logo)
print("""

        .--''-.
.     /'       `.
 '. ,'          |
  ,'        _.-'
 /.:. :._:.'
-': ': ': ': ':
  ': ': ': ': ':>-
_.:' :' :' :' :'
 | :' :' :'
\ \
""")


time.sleep (0.03)
os.system('cls')
print(logo)
print("""
       .--''-.
     /'       `.
'. ,'          |
 ,'        _.-'
/.:. :._:.'
': ': ': ': ':
 ': ': ': ': ':>-
.:' :' :' :' :'
| :' :' :'
 \
""")

time.sleep (0.01)
os.system('cls')
print(logo)
print("""
      .--''-.
    /'       `.
. ,'          |
,'        _.-'
.:. :._:.'
: ': ': ': ':
': ': ': ': ':>-
:' :' :' :' :'
 :' :' :'
\
""")



time.sleep (0.01)
os.system('cls')
print(logo)
print("""
     .--''-.
   /'       `.
 ,'          |
'        _.-'
:. :._:.'
 ': ': ': ':
: ': ': ': ':>-
' :' :' :' :'
:' :' :'

""")


time.sleep (0.01)
os.system('cls')
print(logo)
print("""
    .--''-.
  /'       `.
,'          |
        _.-'
. :._:.'
': ': ': ':
 ': ': ': ':>-
 :' :' :' :'
' :' :'
""")



time.sleep (0.01)
os.system('cls')
print(logo)
print("""
   .--''-.
 /'       `.
'          |
       _.-'
 :._:.'
: ': ': ':
': ': ': ':>-
:' :' :' :'
 :' :'
""")



time.sleep (0.01)
os.system('cls')
print(logo)
print("""
  .--''-.
/'       `.
          |
      _.-'
:._:.'
 ': ': ':
: ': ': ':>-
' :' :' :'
:' :'
""")

time.sleep (0.01)
os.system('cls')
print(logo)
print("""
 .--''-.
'       `.
         |
     _.-'
._:.'
': ': ':
 ': ': ':>-
 :' :' :'
' :'
""")
time.sleep (0.01)
os.system('cls')
print(logo)
print("""
.--''-.
       `.
        |
    _.-'
_:.'
: ': ':
': ': ':>-
:' :' :'
 :'
""")


time.sleep (0.01)
os.system('cls')
print(logo)
print("""
-''-.
     `.
      |
  _.-'
.'
': ':
 ': ':>-
 :' :'
'
""")





time.sleep (0.03)
os.system('cls')
print(logo)
print("""

''-.
    `.
     |
 _.-'
'
: ':
': ':>-
:' :'

""")





time.sleep (0.03)
os.system('cls')
print(logo)
print("""

.
 `.
  |
-'

:
':>-
:'

""")


























time.sleep (0.03)

while True: 
    os.system('cls')
    print(logo)





    os.system(f"title 🐝 Bumblebee MP3 - Option Select 🐝 ")
    print("                Type your option: // Repeat // Shuffle // Singular //")
    option = input("                >")
    finaloption = option.lower()
    if finaloption == "repeat":
        os.system(f"title 🐝 Bumblebee MP3 - Repeating 🐝")
        songname = input("                Song name?\n                >")
        #print(songname)
        #print(songname[-4:])
        songnameextension = songname[-4:]
        if songnameextension == ".mp3": #detecting if the full file name has been inputted..
            helloyall = "hi!"
        else:
            songname = songname+".mp3"
            #print("Fixed!")
            #print(songname)
        os.system(f"title 🐝 Bumblebee MP3 - Playing {songname} 🐝")
        repeatcount = int(input("                How many times do you want your song repeated?\n                >"))
        os.system(f"title 🐝 Bumblebee MP3 - Playing {songname} {str(repeatcount)} Times🐝")
        song = MP3(songname)
        songLength = song.info.length
        looptime = int(songLength)+1
        titlecount = repeatcount
        os.system('cls')
        print(logo)
        for keyroneiaahhh in range(repeatcount):
            mixer.init()
            mixer.music.load(songname)
            mixer.music.play()
            titlecount = titlecount - 1
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            print(f"                            {Fore.RED}[{Fore.BLACK}{hour}:{minute}:{second}{Fore.RED}]{Fore.BLACK} Played {Fore.RED}[{Fore.BLACK}{songname}{Fore.RED}]{Fore.BLACK}")
            os.system(f"title 🐝 Bumblebee MP3 - Playing {songname} {str(titlecount)} More Times🐝")
            time.sleep(looptime)
        os.system(f"title 🐝 Bumblebee MP3 - Finished Playing {songname} 🐝")  
        time.sleep(1)


    elif finaloption == "shuffle":
        os.system('cls')
        print("                            Shuffling!")  
        print(logo)
        while True:
                randomfile = (random.choice(os.listdir()))
                #print(randomfile)
                fileending = randomfile[-3:]
                #print(fileending)
                if randomfile == "opening.mp3":
                    thiswillreselect = "as its the opening sound track , not an mp3 youd wanna listen too"
                elif fileending == "mp3":
                    #print("Valid!")
                    mixer.init()
                    mixer.music.load(randomfile)
                    mixer.music.play()
                    song = MP3(randomfile)
                    os.system(f"title 🐝 Bumblebee MP3 - Playing {randomfile} 🐝")
                    songLength = song.info.length
                    shuffletime = int(songLength)+1
                    currentDT = datetime.datetime.now()
                    hour = str(currentDT.hour)
                    minute = str(currentDT.minute)
                    second = str(currentDT.second)
                    print(f"                            {Fore.RED}[{Fore.BLACK}{hour}:{minute}:{second}{Fore.RED}]{Fore.BLACK} Playing {Fore.RED}[{Fore.BLACK}{randomfile}{Fore.RED}]{Fore.BLACK}")
                    time.sleep(shuffletime)
                else:
                    anothereselct = "as its an invalid file type!"
    














    elif finaloption == "singular":
        singlesong = input("                Song name?\n                >")
        if singlesong == ".mp3": #detecting if the full file name has been inputted..
            helloyall = "hi!"
        else:
            songdet = singlesong+".mp3"
        os.system(f"title 🐝 Bumblebee MP3 - Playing {songdet} 🐝")
        song = MP3(songdet)
        songLength = song.info.length
        aprodelay = int(songLength)+1
        currentDT = datetime.datetime.now()
        hour = str(currentDT.hour)
        minute = str(currentDT.minute)
        second = str(currentDT.second)
        os.system('cls')
        print(logo)
        print(f"                            {Fore.RED}[{Fore.BLACK}{hour}:{minute}:{second}{Fore.RED}]{Fore.BLACK} Playing {Fore.RED}[{Fore.BLACK}{songdet}{Fore.RED}]{Fore.BLACK}")
        mixer.init()
        mixer.music.load(songdet)
        mixer.music.play()    
        time.sleep(aprodelay)
    else:
        print("                Invalid Option - Your options include REPEAT | SHUFFLE | SINGULAR")
        time.sleep(1)



