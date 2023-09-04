import wave
import os.path


my_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(my_path, "./audio/baby-elephant.wav")

wave_obj = wave.open(file_path, "rb")

channels = wave_obj.getnchannels()
sampleWidth = wave_obj.getsampwidth()
frameRate = wave_obj.getframerate()

print("Number of Channels: ", channels)
print("Sample Width: ", sampleWidth)
print("Frame Rate: ", frameRate)
print("Number of Frames: ", wave_obj.getnframes())
print("parameters: ", wave_obj.getparams())

t_audio = wave_obj.getnframes() / wave_obj.getframerate()

print("Audio time: ", t_audio)

frames = wave_obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

# wave_obj.close()
duplicate_file_path = os.path.join(my_path, "./audio/duplicate.wav")

new_obj = wave.open(duplicate_file_path, "wb")

new_obj.setnchannels(channels)
new_obj.setsampwidth(sampleWidth)
new_obj.setframerate(frameRate)

new_obj.writeframes(frames)

print("Create duplicate.wav using frames from", file_path)

new_obj.close()
