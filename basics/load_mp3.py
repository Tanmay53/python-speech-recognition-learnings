from pydub import AudioSegment

audio = AudioSegment.from_wav("baby-elephant.wav")

audio = audio + 6  # Increase the volume by 6dB

audio = audio * 2  # Repeat the audio

audio = audio.fade_in(2000)  # 2 secs fade in

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")

print("Done!")
