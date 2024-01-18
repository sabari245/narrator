from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"

with open(Path(__file__).parent / "input.txt") as f:
    inp = f.read()
    print(inp)
    response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=inp
    )

    response.stream_to_file(speech_file_path)