
# Importing necessary libraries
import psutil  # type: ignore # Library for system monitoring
import pyttsx3  # type: ignore # Library for text-to-speech conversion
import speech_recognition as sr  # type: ignore # Library for speech recognition
import wikipedia  # type: ignore # Library for accessing Wikipedia articles
import webbrowser as wb  # Library for web browsing
import os  # Library for interacting with the operating system
import random  # Library for generating random numbers
import pyautogui  # type: ignore # Library for GUI automation
import time  # Library for time-related functions
import datetime  # Library for date and time functions


# Initializing text-to-speech engine
engine = pyttsx3.init()


def speak(audio):
    """
    Function to vocalize the provided audio string.

    Args:
    audio (str): The string to be vocalized.
    """
    engine.say(audio)
    engine.runAndWait()


def time():
    """Function to tell the current time."""
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)


def date():
    """Function to tell the current date."""
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))


def wishme():
    """Function to greet the user."""
    print("Welcome back !")
    speak("Welcome back !")

    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning !")
        print("Good Morning !")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon !")
        print("Good Afternoon !")
    elif hour >= 16 and hour < 24:
        speak("Good Evening !")
        print("Good Evening !")
    else:
        speak("Good Night Sir, See You Tomorrow")

    speak("I'm Aadi, your AI Desktop Assistant. Please tell me how may I help you.")
    print("I'm Aadi, your AI Desktop Assistant. Please tell me how may I help you.")


# Function to create a new file
def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("")  # Writing an empty string to create the file
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Failed to create file '{file_name}'. Error: {str(e)}")


# Function to delete a file
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to delete file '{file_name}'.")
    except Exception as e:
        print(f"Failed to delete file '{file_name}'. Error: {str(e)}")


# Function to rename a file
def rename_file(old_name, new_name):
    import os
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
    except PermissionError:
        print(f"Permission denied to rename file '{old_name}'.")
    except Exception as e:
        print(f"Failed to rename file '{old_name}'. Error: {str(e)}")


# Function to recognize user speech input
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  # Recognizing speech using Google Speech Recognition API
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")  # Asking the user to repeat if speech recognition fails
        return "Try Again"

    return query


if __name__ == "__main__":
    # Call the wishme function to greet the user
    wishme()
    while True:

        # Listen for user input through speech and convert it to lowercase
        query = takecommand().lower()
        # Check for specific commands in the user's query
        

        if "time" in query:
            time()  # Call the time function to get and speak the current time


        elif "date" in query:
            date()  # Call the date function to get and speak the current date


        elif "who are you" in query:
            # Speak and print a response to introduce the assistant
            speak("I'm AADI created by Harshada and I'm a desktop voice assistant.")
            print("I'm AADI created by Harshada and I'm a desktop voice assistant.")


        elif "how are you" in query:
            # Respond to the inquiry about the assistant's well-being
            speak("I'm fine, What about you?")
            print("I'm fine, What about you?")


        elif "fine" in query:
            # Respond to the user's positive statement
            speak("Glad to hear that!")
            print("Glad to hear that!")


        elif "good" in query:
            # Respond to the user's positive statement
            speak("Glad to hear that!")
            print("Glad to hear that!")


        elif 'thank you' in query:
            # Respond to the user's gratitude
            speak("You're welcome!")


        elif "wikipedia" in query:
            try:
                # Search Wikipedia for the query and speak a summary of the result
                speak("I'm searching...")
                query = query.replace("wikipedia", "")  # Remove "wikipedia" from the query
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                # Notify the user if the requested page cannot be found
                speak("Can't find this page, please ask something else")
        

        elif "open youtube" in query:
            wb.open("youtube.com")  # Open the YouTube website in the default web browser


        elif "open google" in query:
            wb.open("google.com")  # Open the Google website in the default web browser


        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")  # Open the Stack Overflow website in the default web browser


        elif "open facebook" in query:
            wb.open("https://www.facebook.com/")  # Open the Facebook website in the default web browser


        elif "open instagram" in query:
            wb.open("https://www.instagram.com/")  # Open the Instagram website in the default web browser


        elif "open whatsapp" in query:
            wb.open("https://web.whatsapp.com/")  # Open the WhatsApp web version in the default web browser


        elif "play music" in query:
            # Play a random music file from the user's music directory
            song_dir = os.path.expanduser("~\\Music")  # Get the path to the user's music directory
            songs = os.listdir(song_dir)  # Get a list of all files in the music directory
            print(songs)  # Print the list of music files
            x = len(songs)  # Get the number of music files
            y = random.randint(0, x)  # Generate a random index within the range of the number of music files
            os.startfile(os.path.join(song_dir, songs[3]))  # Play the selected music file


        elif "open weather" in query:
            # Open the AccuWeather forecast page for Lonavala, India, in the default web browser
            wb.open("https://www.accuweather.com/en/in/lonavala/189345/weather-forecast/189345")


        elif "open vscode" in query:
            os.system("code")  # Open Visual Studio Code (if installed) using the system command


        elif "open notepad" in query:
            os.system("notepad")  # Open Notepad using the system command


        elif "open chrome" in query:
            # Open Google Chrome using the system command
            chromePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(chromePath)


        elif "search on chrome" in query:
            try:
                # Ask the user for the search query
                speak("What should I search?")
                print("What should I search?")
                # Get the path to Google Chrome's shortcut
                chromePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
                # Get the user's search query through speech recognition
                search = takecommand()
                # Open a new tab in Google Chrome with the search query
                wb.get(chromePath).open_new_tab(search)
                print(search)  # Print the search query

            except Exception as e:
                # Notify the user if Google Chrome cannot be opened
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")


        elif 'file management' in query:
            # Ask the user what file management action they want to perform
            speak("What would you like to do with files?")
            file_action = takecommand().lower()
            if 'create file' in file_action:
                # If the user wants to create a file, ask for the file name and create the file
                speak("Please specify the file name.")
                file_name = takecommand()
                create_file(file_name)
            elif 'delete file' in file_action:
                # If the user wants to delete a file, ask for the file name and delete the file
                speak("Please specify the file name to delete.")
                file_name = takecommand()
                delete_file(file_name)
            elif 'rename file' in file_action:
                # If the user wants to rename a file, ask for the old and new file names and rename the file
                speak("Please specify the old and new file names.")
                old_name = takecommand()
                new_name = takecommand()
                rename_file(old_name, new_name)


        elif 'news' in query:
            # Open the Hindustan Times website to show the latest headlines
            speak("Here are the latest headlines:")
            wb.open("https://www.hindustantimes.com/")


        elif "remember that" in query:
            # Ask the user what they want to remember and save it to a file
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()


        elif "do you remember anything" in query:
            # Read and speak the content stored in the 'data.txt' file
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))


        elif "joke" in query:
            # Tell a random joke from the list of jokes
            jokes = [
                "Why was the math book sad? Because it had too many problems.",
                "Why don't scientists trust atoms? Because they make up everything!",
                "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                "Why don't skeletons fight each other? They don't have the guts.",
                "I told my wife she was drawing her eyebrows too high. She looked surprised."
            ]
            speak(random.choice(jokes))


        elif "random facts" in query:
            # Tell a random interesting fact from the list of facts
            random_facts = [
                "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
                "A group of flamingos is called a flamboyance.",
                "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
                "The unicorn is the national animal of Scotland.",
                "The world's largest desert is not the Sahara, but Antarctica."
            ]
            speak(random.choice(random_facts))


        elif "search" in query:
            # Extract the search term from the query and open a Google search page with the search term
            search_term = query.replace("search ", "")
            wb.open(f"https://www.google.com/search?q={search_term}")


        elif "screenshot" in query:
            # Take a screenshot and save it as 'screenshot.png'
            speak("Sure, I'll take a screenshot now.")
            try:
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                speak("Screenshot saved successfully.")
            except Exception as e:
                speak(f"Sorry, an error occurred while taking the screenshot: {str(e)}")


        elif "calculate" in query:
            # Evaluate a mathematical expression and speak the result
            try:
                expression = query.replace("calculate ", "")
                result = eval(expression)
                speak(f"The result is {result}")
                print(f"The result is {result}")
            except Exception as e:
                speak("Sorry, I couldn't calculate that.")


        elif "system info" in query:
            # Retrieve and speak system information such as CPU usage and memory usage
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                total_memory = round(memory.total / (1024 * 1024 * 1024), 2)
                available_memory = round(memory.available / (1024 * 1024 * 1024), 2)
                speak(f"CPU Usage: {cpu_usage}%")
                print(f"CPU Usage: {cpu_usage}%")
                speak(f"Total Memory: {total_memory} GB")
                print(f"Total Memory: {total_memory} GB")
                speak(f"Available Memory: {available_memory} GB")
                print(f"Available Memory: {available_memory} GB")
            except Exception as e:
                speak(f"An error occurred: {str(e)}")


        elif "shutdown" in query:
            # Shutdown the system
            speak("Shutting down...")
            os.system("shutdown /s /t 1")


        elif "restart" in query:
            # Restart the system
            speak("Restarting...")
            os.system("shutdown /r /t 1")    


        elif 'sleep' in query:
            # Put the system to sleep
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


        elif "offline" in query or "stop" in query or "exit" in query:
            # End the program and say goodbye
            speak("Goodbye! See you soon!")
            quit()

