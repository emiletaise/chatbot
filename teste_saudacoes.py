import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

# INICIA O CHATBOT
    def setUp(self):
        self.robo = iniciar()

    def testar_oi_ola(self):
        saudacoes = [ "oi", "olá" ]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá, sou o robô de atendimento Maria", 
                resposta.text
            )

# TESTA SAUDAÇÕES
    def testar_bom_dia_boa_tarde_boa_noite(self):
        saudacoes = ["Bom dia", "Boa tarde", "Boa noite"]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                saudacao + ", sou o robô de atendimento Maria",
                resposta.text
            )

    def testar_variabilidades_saudacoes(self):
        saudacoes = [ "Bom dia", "Boa tarde", "Boa noite" ]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response("oi, " + saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                saudacao + ", sou o robô de atendimento Maria. Tire sua dúvida sobre física basica!",
                resposta.text
            )



if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)