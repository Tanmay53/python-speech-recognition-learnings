import wave
import matplotlib.pyplot as plt
import numpy as np

file_obj = wave.open("baby-elephant.wav", "rb")

sample_frequency = file_obj.getframerate()
n_samples = file_obj.getnframes()
frames = file_obj.readframes(-1)

file_obj.close()

t_audio = n_samples / sample_frequency

signal_array = np.frombuffer(frames, dtype=np.int16)

times = np.linspace(0, t_audio, n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()
