import pyaudio
import wave
import os.path

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER,
)

print("Start Recording")

seconds = 5
frames = []

for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    frames.append(stream.read(FRAMES_PER_BUFFER))

stream.stop_stream()
stream.close()
p.terminate()

my_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(my_path, "./audio/recording.wav")

file_obj = wave.open(file_path, "wb")

file_obj.setnchannels(CHANNELS)
file_obj.setsampwidth(p.get_sample_size(FORMAT))
file_obj.setframerate(RATE)

file_obj.writeframes(b"".join(frames))

file_obj.close()
