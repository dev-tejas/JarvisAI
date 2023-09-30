import Functions as func
import wikipedia
import datetime

if __name__ == "__main__":
    func.greet()
    while True:
        query = func.takeCommand().lower()

        if 'wikipedia' in query:
                func.speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                func.speak("According to Wikipedia")
                print(results)
                func.speak(results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            func.speak(f"Sir, the time is {strTime}")