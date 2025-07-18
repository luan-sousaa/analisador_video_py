from flask import Flask, render_template , request
from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
import openai
import ffmpeg
import os
import re
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    resposta = None
    titulo_video = None
    if request.method == 'POST':
        link_video = request.form.get('link_video')
        if link_video:
            titulo_video, resposta = analisar_video(link_video)
        else:
            resposta = "Nenhum link foi fornecido. Por favor, cole o link do vídeo."

    return render_template("index.html", resposta=resposta, titulo_video=titulo_video)


def sanitize_filename(title: str) -> str:
    # substitui tudo que não seja letra, número, ponto ou underline por underscore
    return re.sub(r'[^\w\.-]', '_', title)


#função que ira analisar o video
def analisar_video(link_video):
    # 1) Cria pasta de áudios
    audios_dir = os.path.join(os.getcwd(), "audios")
    os.makedirs(audios_dir, exist_ok=True)

    # 2) Baixar áudio do YouTube
    yt = YouTube(link_video, on_progress_callback=on_progress)
    titulo = yt.title
    ys = yt.streams.get_audio_only()

    # 3) Gerar nome de arquivo seguro
    safe_title = sanitize_filename(titulo)
    filename = f"{safe_title}.m4a"
    audio_path = os.path.join(audios_dir, filename)

    # 4) Download para a pasta 'audios'
    ys.download(output_path=audios_dir, filename=filename)

    # 5) Transcrever o áudio com Whisper
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(audio_path)

    return titulo, resultado["text"]


#resumo com IA


if __name__ == "__main__":
    app.run(debug=True)