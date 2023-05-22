# Chatbot Maria 

Robô de atendimento que responde questões sobre física basica.

## Como executar

```bash
# Clone o repositório
$ git clone https://github.com/emiletaise/chatbot.git

# Entre na pasta do projeto
$ cd chatbot

# Instale as dependências
$ pip3 install -r requirements.txt

# Execute o treinamento
$ python3 treinamento.py

# Execute o serviço web
$ python3 servico.py

# Entre na pasta do servidor em um segundo terminal
$ cd chat

# Execute a aplicação 
$ yarn start
```

Por fim, o robô estará disponível para acesso no seu navegador em: http://localhost:3000/

## Para executar os testes

```bash
# Execute os testes de saudação
$ python teste_saudacoes.py
# Execute os testes das perguntas
$ python3 teste_informacoes_basicas.py
```