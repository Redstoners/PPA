# Setup
import time


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
    if input == "help":
        file = open('bin/commands.txt', 'r')
        file_contents = file.read()
        print (file_contents)
        file.close()
    elif input == "time":
        speak("The current time is " + current_time)
    elif input == "hello":
        print("Hello human!")
    elif input == "date":
        print("The current date is " + current_date)
    else:
        print("That is not a valid command")
