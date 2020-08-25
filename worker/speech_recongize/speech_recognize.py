import speech_recognition as sr


r = sr.Recognizer()
harvard = sr.AudioFile('./audio_files/harvard.wav')
with harvard as source:
    audio = r.record(source)
    print(r.recognize_google(audio))

jackhammer = sr.AudioFile('./audio_files/jackhammer.wav')
with jackhammer as source:
    audio = r.record(source)
    print(r.recognize_google(audio))

with jackhammer as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    print(r.recognize_google(audio))
