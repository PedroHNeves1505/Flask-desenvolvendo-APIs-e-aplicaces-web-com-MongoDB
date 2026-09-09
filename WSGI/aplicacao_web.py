# Desenvolver um servidor WSGI
# Responsavel por fazer a comunicação entre servidor web e python 
# Desenvolve linha por linha
# Muito trabalho manual e muito facíl cometer erros

from wsgiref.simple_server import make_server


def aplicacao(environ, start_response):
    produtos = [
        {'nome': 'Meia', 'valor': 49.99},
        {'nome': 'Camisa', 'valor': 139.99},
        {'nome': 'Calça', 'valor': 129.99},
        {'nome': 'Blusa', 'valor': 149.99}
    ]

    linhas_html = ''
    for produto in produtos:
        linhas_html += f'<li>{produto["nome"]} - R$ {produto["valor"]}</li>'

    start_response('200 OK', [('Content-type', 'text/html;charset=utf-8')])
    with open('WSGI/index.html', 'r', encoding='utf-8') as file:
        html = file.read()

    html_final = html.replace('{{PRODUTOS}}', linhas_html)
    return [html_final.encode('utf-8')]

print('Servidor rodando em http://localhost:5000')
make_server('', 5000, aplicacao).serve_forever()
