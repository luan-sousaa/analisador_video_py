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

import google.generativeai as genai
import os # Biblioteca para interagir com o sistema operacional, útil para variáveis de ambiente
from dotenv import load_dotenv # Para carregar variáveis de ambiente de um arquivo .env

# --- 1. Carregar a Chave da API (MELHOR PRÁTICA DE SEGURANÇA) ---
# Instale: pip install python-dotenv
# Crie um arquivo chamado '.env' na mesma pasta do seu script com o conteúdo:
# GEMINI_API_KEY='SUA_CHAVE_AQUI' (substitua pela sua chave real)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("ERRO: A chave da API 'GEMINI_API_KEY' não foi encontrada nas variáveis de ambiente.")
    print("Por favor, crie um arquivo .env na mesma pasta do seu script com o conteúdo: GEMINI_API_KEY='SUA_CHAVE_AQUI'")
    # Se a chave não for encontrada, o script não pode continuar
    exit()

# Define a chave da API para a biblioteca google-generativeai
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

#Definir o Prompt
resumo_video = resposta["text"]

prompt_para_gemini = f"""
Resuma a seguinte transcrição de um vídeo do YouTube de forma concisa, focando nos pontos principais e benefícios. O resumo deve ter no máximo 3 parágrafos.

--- Transcrição do Vídeo ---
{resumo_video}
"""

# --- 5. Gerar Conteúdo com o Modelo ---
try:
    print("Enviando solicitação ao modelo Gemini...")
    # generate_content envia o prompt para a API e recebe a resposta
    response = model.generate_content(prompt_para_gemini)

    # --- 6. Processar a Resposta ---
    # A resposta da API pode vir de diferentes formas, dependendo do conteúdo.
    # É comum que o texto esteja em 'response.text' ou em 'response.parts'
    if response.text: # Para respostas diretas de texto
        print("\n--- Resumo Gerado pela IA ---")
        print(response.text)
    elif response.parts: # Para respostas que vêm em múltiplas partes (como em prompts mais complexos)
        print("\n--- Resumo Gerado pela IA (Partes) ---")
        for part in response.parts:
            print(part.text)
    else:
        print("\n--- Resposta da API ---")
        print("Não foi possível extrair texto diretamente da resposta. Detalhes:")
        # Imprime a estrutura completa da resposta para depuração
        print(response)

except Exception as e:
    # Captura possíveis erros, como problemas de rede, chave API inválida, etc.
    print(f"\nOcorreu um erro ao interagir com a API Gemini: {e}")

print("\nProcessamento concluído.")

