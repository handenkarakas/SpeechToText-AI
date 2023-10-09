import speech_recognition as sr

recognizer = sr.Recognizer()

aud_file = "C:\\Users\\Hande\Desktop\\speecToText_ai\\test.wav" #descript the file path

#opn audio file
with sr.AudioFile(aud_file) as source:
    try:
        audio = recognizer.record(source) #read the audio file
        text = recognizer.recognize_google(audio, language="tr-TR") #convert audio file to text
        print("Metin: \n" + text)
    except sr.UnknownValueError:
        print("Ses anlaşılamadı.")
    except sr.RequestError as e:
        print("Ses tanıma hizmeti hatası: {0}".format(e))