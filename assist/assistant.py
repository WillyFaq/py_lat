import pyttsx3
import speech_recognition as sr

def take_commands():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening")
		r.pause_threshold = 0.7
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recongnize_google(audio, language='en-in')
			print(f"This query is printed '{query}'")
		except Exception as e:
			print(e)
			print("Say again!")
			return "None"
	return Query

def speak(audio):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(audio)
	engine.runAndWait()

if __name__ == '__main__':
	speak("hallo sir!")
	while True:
		command = take_commands()
		if "exit" in command:
			speak("Sure sir! as your wish, bai")
			print("Sure sir! as your wish, bai")
			break
