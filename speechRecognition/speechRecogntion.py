import speech_recognition as sr
import webbrowser as wb


def read_soundfile(wav_file):
    """
    listens to a .wav file and prints out what is said in the audio
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        print("Listening to audiofile...")
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text


def recognize_speech():
    """
    Uses microphone to listen, and returns a string of what was heard
    :return text (string): text format of what was said in the microphone
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Speak now: \n")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(text)
        except LookupError:
            print("Unintelligible")
    return text

def youtube_search():
    """
    Uses microphone to listen for a search word, then searches for it on youtube
    """
    recognizer = sr.Recognizer()
    url = "https://www.youtube.com/results?search_query="
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("What would you wish to search for on youtube?")
        audio = recognizer.listen(source)
        try:
            get = recognizer.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("failed".format(e))


