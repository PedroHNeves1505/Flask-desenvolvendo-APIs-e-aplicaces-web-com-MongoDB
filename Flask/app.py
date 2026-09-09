# Framework Flask
# Faz conexão com servidor WSGI
# Muito mais compacto e com menos chances de cometer erros

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello World'

app.run(debug=True)