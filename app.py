from flask import Flask

app = Flask(__name__)

@app.run("/")
def pagina_principal():
    return "ola"

app.run(debug=True)