from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

#colocar a primeira pagina no ar
#route - minhaprimeirapagina.com/
#função - o que voçê quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)