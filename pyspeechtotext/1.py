import speech_recognition as sr

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("say")
        audio = r.listen(source)

        print("recog now")

        try:
            print("input: \n"+r.recognize_google_cloud(audio))
            print(" audio recorded \n")

        except Exception as e:
            print("error : " + str(e))

        with open("recordaudio.wav", "wb") as f:
            f.write(audio.get_wav_data())
if __name__ == "__main__":
    main()