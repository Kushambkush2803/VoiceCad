print("Program started")

import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from parser import parse_command
import json

fs = 44100
seconds = 5

print("Speak now...")

recording = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1
)

sd.wait()

write("audio.wav", fs, recording)

print("Transcribing...")

model = whisper.load_model("base")

result = model.transcribe("audio.wav")

text = result["text"]

print("You said:")
print(text)

command = parse_command(text)

if command:

    print("\nParsed Command:")
    print(command)

    with open("command.json", "w") as file:
        json.dump(command, file, indent=4)

    print("\nCommand saved to command.json")

else:

    print("No valid CAD command detected.")