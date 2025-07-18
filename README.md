# LuAnalyzer

**LuAnalyzer** é uma aplicação web desenvolvida com **Flask** que permite extrair e processar automaticamente o conteúdo falado de vídeos do YouTube, oferecendo funcionalidades como transcrição, geração de resumo com inteligência artificial e exportação para PDF.

Ideal para quem precisa obter e manipular rapidamente a informação presente em vídeos — seja para estudos, relatórios, acessibilidade ou organização de conteúdo.

---

## 🔧 Funcionalidades

- Recebe um link de vídeo do YouTube via formulário.
- Faz download apenas do áudio do vídeo.
- Transcreve o áudio utilizando o modelo **Whisper AI**.
- Exibe o título do vídeo e a transcrição diretamente na interface web.
- Permite gerar um **PDF da transcrição** automaticamente.
- Gera um **resumo automático da transcrição** utilizando o modelo **Gemini Pro** da Google (via API).
- Efeito visual com confetes ao enviar o link do vídeo (opcional, configurado no frontend).

---

## 💻 Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) – Framework web em Python
- [Pytubefix](https://pytube.io/) – Para download de vídeos do YouTube
- [Whisper](https://github.com/openai/whisper) – Modelo de transcrição automática
- [FFmpeg](https://ffmpeg.org/) – Necessário para processar áudio
- [FPDF](https://pyfpdf.github.io/) – Para gerar arquivos PDF
- [Google Generative AI (Gemini)](https://ai.google.dev/) – Para geração de resumos com IA

---

## Como Executar o Projeto Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
'''
2. Crie um ambiente virtual (recomendado)
bash
Copiar
Editar
python -m venv venv

Ative o ambiente virtual:

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
⚠️ É necessário ter o FFmpeg instalado para que o Whisper funcione corretamente.

Instalação do FFmpeg:
macOS (via Homebrew):

bash
Copiar
Editar
brew install ffmpeg
Ubuntu:

bash
Copiar
Editar
sudo apt update
sudo apt install ffmpeg
Windows:
Baixe e configure o FFmpeg através do site oficial: https://ffmpeg.org/download.html

4. Configure a variável de ambiente da API Gemini
Crie um arquivo .env com o seguinte conteúdo:

ini
Copiar
Editar
GEMINI_API_KEY=sua_chave_aqui
5. Execute a aplicação
bash
Copiar
Editar
python app.py
Acesse a aplicação no navegador:

cpp
Copiar
Editar
http://127.0.0.1:5000
