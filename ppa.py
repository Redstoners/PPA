# Setup
import time
import webbrowser
import md5
import sys
import hashlib
from urllib2 import urlopen

# Makes the webbrowser command
def open_link(link):
    webbrowser.open(link)
    speak("Opening web browser")
    pause(2)

# Makes the pause command
def pause(seconds):
    time.sleep(seconds)

# Makes the speak command
def speak(text):
    print(text)

# Makes the sha1 encrypter command
def encrypt_sha1(textsha1):
    hash_objectsha1 = hashlib.sha1(textsha1)
    hex_digsha1 = hash_objectsha1.hexdigest()
    speak("Proccesing...")
    speak(hex_digsha1)

# Makes the sha224 encrypter command
def encrypt_sha224(textsha224):
    hash_objectsha224 = hashlib.sha224(textsha224)
    hex_digsha224 = hash_objectsha224.hexdigest()
    speak("Proccesing...")
    speak(hex_digsha224)

# Makes the sha256 encrypter command
def encrypt_sha256(textsha256):
    hash_objectsha256 = hashlib.sha256(textsha256)
    hex_digsha256 = hash_objectsha256.hexdigest()
    speak("Proccesing...")
    speak(hex_digsha256)

# Initializes the time and date
time.ctime()
current_time = time.strftime('%H:%M')
current_date = time.strftime('%d %B %Y')

speak("Hello! i am PAI, your owm personal assistant")

# Main program
var = 1
while var == 1:
    input = raw_input(">>>")
    if input in {"help", "help me", }:
        file = open('bin/commands.txt', 'r')
        file_contents = file.read()
        print (file_contents)
        file.close()
    elif input in {"exit", "kill", "escape"}:
        speak("Killing PPA...")
        sys.exit()
    elif input in {"time", "the current time", "current time"}:
        speak("The current time is " + current_time)
    elif input in {"search", "google"}:
        speak("What do you want to Google?")
        google = raw_input(">>>")
        google.replace(" ", "+")
        open_link('https://www.google.nl/#q=' + google.replace(" ", "+"))
    elif input == "hello":
        print("Hello human!")
    elif input in {"date", "the current date", "current date"}:
        print("The current date is " + current_date)
    elif input in {"what is your favorite song?", "favorite song"}:
        speak("I really like human music!")
        pause(1)
        speak("Let me show it to you!")
        open_link('https://www.youtube.com/watch?v=q4k1IK_o59M')
    elif input in {"im hungry", "i want to eat", "restaurant"}:
        speak("What do you want to eat?")
        eat = raw_input(">>>")
        open_link('https://www.google.nl/maps/search/' + eat.replace(" ", "+"))
    elif input in {"what is my ip?", "my ip", "ip", "what's my ip?", "whats my ip?", "whats my ip", "what is my ip"}:
        ip = urlopen('http://ip.42.pl/raw').read()
        speak(ip)
    elif input in {"md5"}:
        speak("What do you want to hash to MD5?")
        md5_string = raw_input('>>>')
        speak("proccesing...")
        speak( md5.md5(md5_string).hexdigest() )
    elif input in {"sha1"}:
        speak("What do you want to encrypt?")
        sha1_input = raw_input('>>>')
        encrypt_sha1(sha1_input)
    elif input in {"sha1"}:
        speak("What do you want to encrypt?")
        sha1_input = raw_input('>>>')
        encrypt_sha1(sha1_input)
    elif input in {"sha224"}:
        speak("What do you want to encrypt?")
        sha224_input = raw_input('>>>')
        encrypt_sha224(sha224_input)
    elif input in {"sha256"}:
        speak("What do you want to encrypt?")
        sha256_input = raw_input('>>>')
        encrypt_sha256(sha256_input)
    elif input in {"what is per?"}:
        speak("A huge dumbass...")
        pause(2)
        speak("Take my word for it")
    else:
        print("That is not a valid command")
