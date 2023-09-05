from dotenv import load_dotenv
import os
import sys
import assemblyai as aai

load_dotenv()

aai.settings.api_key = os.getenv("API_KEY_ASSEMBLYAI")

try:
    filename = sys.argv[1]
except:
    filename = "./audio/recording.wav"

transcriber = aai.Transcriber()

transcript = transcriber.transcribe(filename)

transcript_file = "transcript.txt"

if transcript.error == None:
    with open(transcript_file, "w") as f:
        f.write(transcript.text)
    print("Transcript Saved to {}!!".format(transcript_file))
else:
    print("Error: ", transcript.error)
