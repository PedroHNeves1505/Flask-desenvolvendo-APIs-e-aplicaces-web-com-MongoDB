# Framework Flask
# Faz conexão com servidor WSGI
# Muito mais compacto e com menos chances de cometer erros

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)