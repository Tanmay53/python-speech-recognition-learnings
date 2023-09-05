# Python Speech Recognition

A repo to record learnings about speech recognition using python.

- [Python Speech Recognition](#python-speech-recognition)
  - [Basics](#basics)
    - [Reading Wave files](#reading-wave-files)
    - [Plotiing Wave file data into a graph](#plotiing-wave-file-data-into-a-graph)
    - [Recording from Mic](#recording-from-mic)
    - [Loading and creating Mp3 files](#loading-and-creating-mp3-files)
  - [Speech Recognition](#speech-recognition)

## Basics

### [Reading Wave files](./basics/wave_example.py)

```bash
python basics/wave_example.py
```

Check if [basics/audio/duplicate.wav](./basics/audio/duplicate.wav) got created.

### [Plotiing Wave file data into a graph](./basics/plot_audio.py)

Install dependencies
```bash
pip install matplotlib numpy
```

Run

```bash
python basics/plot_audio.py
```

### [Recording from Mic](./basics/record_mic.py)

Check Pyaudio installation steps at https://pypi.org/project/PyAudio/

Run
```bash
python basics/record_mic.py
```

Check if your voice got recorded in [basics/audio/recording.wav](./basics/audio/recording.wav) 

### [Loading and creating Mp3 files](./basics/load_mp3.py)

Install dependencies
```bash
pip install pydub
```

Run

```bash
python basics/load_mp3.py
```

Check if [basics/audio/mashup.mp3](./basics/audio/mashup.mp3) got created.

## Speech Recognition

Copy *.env.example* to *.env* and add the API_KEY for [Assembly AI](https://assemblyai.com)

Install Dependencies

```bash
pip install -U python-dotenv assemblyai
```

Run
```bash
python speech_recognition/main.py
```
OR
```bash
python speech_recognition/main.py [path_to_a_audio_file]
```

Check if [speech_recognition/transcript.txt](./speech_recognition/transcript.txt) contains the transcriptions for [speech_recognition/audio/recording.wav](./speech_recognition/audio/recording.wav) or for the audio file supplied to the command.

