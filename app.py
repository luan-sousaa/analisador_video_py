from flask import Flask, render_template , request
from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
import openai
import ffmpeg
import os
import re
from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask import request, send_file
from fpdf import FPDF
import tempfile
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
# Carregar API Key do .env
#load_dotenv()
#API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key="")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/resumir", methods=["POST"])
def resumir():
    try:
        transcricao = request.form.get("transcricao")

        if not transcricao:
            return render_template("index.html", resposta="Erro: nenhuma transcrição foi recebida.")

        prompt = f"""
        Resuma a seguinte transcrição de um vídeo do YouTube de forma concisa, focando nos pontos principais e benefícios. O resumo deve ter no máximo 3 parágrafos.

        --- Transcrição do Vídeo ---
        {transcricao}
        """

        response = model.generate_content(prompt)
        resumo = response.text if response.text else "Erro ao gerar resumo."

        return render_template("index.html", titulo_video="Resumo IA", resposta=resumo)

    except Exception as e:
        return render_template("index.html", resposta=f"Erro ao gerar resumo: {e}")

#gerar pdf
@app.route("/gerar_pdf", methods=["POST"])
def gerar_pdf():
    texto = request.form.get("transcricao")

    if not texto:
        return "Nenhum conteúdo encontrado para gerar o PDF", 400

    # Cria o PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    # Divide o texto em linhas para não estourar no PDF
    linhas = texto.split('\n')
    for linha in linhas:
        pdf.multi_cell(0, 10, linha)

    # Salva em arquivo temporário
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        caminho_pdf = tmp.name
        pdf.output(caminho_pdf)

    # Retorna o PDF para download
    return send_file(caminho_pdf, as_attachment=True, download_name="transcricao.pdf")
if __name__ == "__main__":
    app.run(debug=True)