# LuAnalyzer

## Visão Geral

O **LuAnalyzer** é uma aplicação web desenvolvida em Python com o framework Flask, projetada para extrair, transcrever e resumir o conteúdo de vídeos da plataforma YouTube.

A ferramenta é voltada para usuários que necessitam processar informações de vídeos de forma eficiente, como estudantes, pesquisadores e criadores de conteúdo, facilitando tarefas de estudo, elaboração de relatórios e acessibilidade.

---

## Recursos Principais

-   **Entrada de Dados via URL:** Recebe um link de vídeo do YouTube através de um formulário na interface web.
-   **Extração de Áudio:** Realiza o download exclusivo do áudio do vídeo para otimizar o processamento.
-   **Transcrição Automática:** Utiliza o modelo **Whisper AI** da OpenAI para converter o áudio em texto.
-   **Geração de Resumos:** Emprega o modelo **gemini-1.5-flash** da Google para criar um resumo automático e coeso da transcrição.
-   **Visualização e Exportação:** Exibe o título do vídeo e a transcrição completa na interface e permite a exportação do conteúdo para um arquivo PDF.

---

## Pilha Tecnológica

-   **Framework Backend:** [Flask](https://flask.palletsprojects.com/)
-   **Processamento de Vídeo:** [Pytubefix](https://github.com/pytubefix/pytubefix)
-   **Modelo de Transcrição:** [OpenAI Whisper](https://github.com/openai/whisper)
-   **Modelo de Linguagem (LLM):** [Google Generative AI (Gemini)](https.ai.google.dev/)
-   **Geração de Documentos:** [FPDF2](https://pyfpdf.github.io/fpdf2/)
-   **Dependência de Mídia:** [FFmpeg](https://ffmpeg.org/)

---

## Guia de Instalação

Para executar este projeto localmente, siga os passos detalhados abaixo.

### Pré-requisitos

Certifique-se de que os seguintes componentes estão instalados e configurados em seu sistema:

-   **Python 3.8** ou superior.
-   **FFmpeg:** Dependência fundamental para o processamento de áudio.
    -   **macOS (via Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    -   **Ubuntu/Debian:**
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
    -   **Windows:**
        Realize o download a partir do [site oficial](https://ffmpeg.org/download.html) e adicione o diretório `bin` às variáveis de ambiente do sistema.

### Configuração e Execução

1.  **Clone o Repositório**
    ```bash
    git clone [https://github.com/](https://github.com/)<seu-usuario>/<seu-repositorio>.git
    cd <seu-repositorio>
    ```
    *Lembre-se de substituir `<seu-usuario>` e `<seu-repositorio>` pelos seus dados.*

2.  **Crie e Ative um Ambiente Virtual**
    É altamente recomendado utilizar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    python -m venv venv
    ```
    Ative o ambiente de acordo com o seu sistema operacional:
    ```bash
    # Para Windows
    .\venv\Scripts\activate

    # Para macOS e Linux
    source venv/bin/activate
    ```

3.  **Instale as Dependências**
    Instale todos os pacotes Python necessários a partir do arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Google Gemini ou coloque diretamente a chave api no seu codigo.
    ```ini
    GEMINI_API_KEY="SUA_CHAVE_DE_API_AQUI"
    ```

5.  **Execute a Aplicação**
    Inicie o servidor de desenvolvimento do Flask.
    ```bash
    flask run
    ```
    A aplicação estará disponível em seu navegador no seguinte endereço:
    `http://127.0.0.1:5000`

---

## Contribuições

Contribuições são bem-vindas. Para sugestões, melhorias ou correções de bugs, por favor, abra uma *issue* ou submeta um *pull request* neste repositório.
