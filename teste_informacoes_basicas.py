import unittest
from robo import *


class TesteInformacoesBasicas(unittest.TestCase):

# INICIA CHATBOT
    def setUp(self):
        self.robo = iniciar()
# TESTA QUESTÃO SOBRE VELOCIDADE
    def testar_velocidade(self):
        mensagens = ["o que é velocidade?", "explique sobre velociade"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Velocidade é uma grandeza física que indica a rapidez com que um objeto se desloca em um determinado intervalo de tempo.", resposta.text)

# TESTA QUESTÃO SOBRE MOVIMENTO
    def testar_movimento(self):
        mensagens = [ "o que é movimento uniforme?", "explique sobre movimento uniforme" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Movimento uniforme é aquele em que um objeto se desloca com velocidade constante, ou seja, sem aceleração.", resposta.text)

# TESTA QUESTÃO SOBRE INERCIA
    def testar_inercia(self):
        mensagens = [ "o que é lei da inercia de Newton?", "o que é lei da inercia?", "explique sobre lei da inercia" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("A lei da inércia de Newton é a primeira lei do movimento, que estabelece que um objeto em repouso permanecerá em repouso e um objeto em movimento permanecerá em movimento com velocidade constante, a menos que uma força resultante seja aplicada sobre ele.", resposta.text)

# TESTA QUESTÃO SOBRE AÇÃO E REAÇÃO
    def testar_acao_reacao(self):
        mensagens = [ "o que é lei da ação e reação?", "explique sobre lei da ação e reação" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("A lei da ação e reação, também conhecida como terceira lei de Newton, estabelece que toda ação provoca uma reação igual e oposta.", resposta.text)

# TESTA QUESTÃO SOBRE CAMPO MAGNETICO
    def testar_campo_magnetico(self):
        mensagens = [ "o que é campo Magnético?", "explique sobre campo Magnético" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Um campo magnético é a região do espaço ao redor de um ímã ou de uma corrente elétrica onde uma força magnética é exercida sobre outra carga magnética ou elétrica em movimento.", resposta.text)

# INCIA OS TESTE
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoesBasicas))

    executor = unittest.TextTestRunner()
    executor.run(testes)
