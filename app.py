from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def home():
    resposta = None
    if request.method == 'POST':
        link_video = request.form.get('link_video')
        #chamar funcao de transcriçao
        resposta = analisar_video(link_video)

    return render_template("index.html" , resposta=resposta)

def analisar_video(link_video):
    #logica do analizador aqui
    return f"resumo gerado {link_video}"








if __name__ == "__main__":
    app.run(debug=True)