from robo import *
from flask import Flask

VERSAO = "0.2"

# INCIA O CHATBOT NO ARQUIVO robo.py
robo = iniciar()
servico_robo = Flask(__name__)

@servico_robo.route("/versao")
def get_versao():
    return VERSAO

# COLETA A MENSAGEM PARA EXECUÇÃO
@servico_robo.route("/resposta/<mensagem>")
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem)

    return resposta.text

if __name__ == "__main__":
    servico_robo.run()