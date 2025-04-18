from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
import ffmpeg
import openai

#faz dowload do video e envia para um repertorio especifico
url = input("Link da url aqui do video: ")
yt = YouTube(url , on_progress_callback= on_progress)
print(yt.title)
ys = yt.streams.get_audio_only()
ys.download()
caminho_audio = f"{yt.title}.m4a"


#transcriçao do audio
modelo = whisper.load_model("base")
audio = caminho_audio #caminho do audio
resposta = modelo.transcribe(audio)
print(resposta["text"])

