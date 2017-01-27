# Setup
import time


def pause(seconds):
    time.sleep(seconds)


def speak(text):
    print(text)

time.ctime()
current_time = time.strftime('%H:%M')
current_date = time.strftime('%d %B %Y')

speak("Hello! i am PAI, your owm personal assistant")

# Main program
var = 1
while var == 1:
    input = raw_input(">>>")
    if input == "time":
        speak("The current time is " + current_time)
    elif input == "hello":
        print("Hello human!")
    elif input == "date":
        print("The current date is " + current_date)
    else:
        print("That is not a valid command")
