LuAnalyzer 🎥✨
LuAnalyzer é uma aplicação web simples feita com Flask, que permite:

Receber o link de um vídeo do YouTube.

Baixar o áudio do vídeo.

Utilizar o modelo Whisper para gerar uma transcrição automática.

Ideal para quem quer obter rapidamente o conteúdo falado de vídeos!

🚀 Funcionalidades
🔗 Recebe um link de vídeo do YouTube via formulário.

🎵 Faz download apenas do áudio.

🧠 Transcreve o áudio usando Whisper AI.

📝 Exibe o título do vídeo e a transcrição na tela.

🛠️ Tecnologias usadas
Flask

Pytubefix (para download dos vídeos)

Whisper (para transcrição)

FFmpeg (dependência para Whisper)

🖥️ Como rodar o projeto localmente
1. Clone o repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Crie um ambiente virtual (recomendado)
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
Importante: você precisa ter o FFmpeg instalado no seu computador para o Whisper funcionar corretamente.
Para instalar no MacOS:

bash
Copiar
Editar
brew install ffmpeg
Para instalar no Ubuntu:

bash
Copiar
Editar
sudo apt update
sudo apt install ffmpeg
Para Windows: Baixar FFmpeg

4. Execute a aplicação
bash
Copiar
Editar
python app.py
Acesse no navegador:
http://127.0.0.1:5000

📋 Requisitos
Python 3.8+

FFmpeg instalado e configurado

📸 Demonstração 
 ![img.png](img.png)

📬 Contato
Feito com 💙 por Luan Bispo.

GitHub: luan-sousaa

Email: luanbispo.sousa263@gmail.com

📢 Observação
O Whisper é uma tecnologia pesada para alguns dispositivos!
Rodar a transcrição pode demorar dependendo do tamanho do áudio e da capacidade da sua máquina.

