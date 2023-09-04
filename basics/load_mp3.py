from pydub import AudioSegment
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(my_path, "./audio/baby-elephant.wav")

audio = AudioSegment.from_wav(file_path)

audio = audio + 6  # Increase the volume by 6dB

audio = audio * 2  # Repeat the audio

audio = audio.fade_in(2000)  # 2 secs fade in

mashup_path = os.path.join(my_path, "./audio/mashup.mp3")

audio.export(mashup_path, format="mp3")

audio2 = AudioSegment.from_mp3(mashup_path)

print("Done!")
