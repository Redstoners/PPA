# Setup
import time
import webbrowser

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
    else:
        print("That is not a valid command")
