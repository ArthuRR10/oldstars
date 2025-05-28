from flask import Flask, jsonify
from threading import Thread
import random

app = Flask(__name__)

idades = [24, 25, 26, 27, 28]

posicoes = [
    "Goleiro", "Zagueiro", "Lateral Direito", "Lateral Esquerdo",
    "Volante", "Meia Central", "Meia Ofensivo", "Ponta Direita",
    "Ponta Esquerda", "Centroavante", "Falso 9"
]

historicos_aposentadoria = [
    "Sumiu após lesionar o mindinho jogando truco",
    "Foi ser pastor e largou os gramados",
    "Abandonou tudo para virar streamer de Farming Simulator",
    "Se dedicou ao universo da sinuca profissional",
    "Foi tentar carreira no MMA e levou um nocaute na estreia",
    "Desapareceu após uma aposta mal-sucedida com um cavalo",
    "Assumiu um boteco na esquina da vila",
    "Largou tudo para ser dublê de novelas mexicanas",
    "Foi estudar teologia na Patagônia",
    "Prometeu que só voltaria se o Palmeiras ganhasse o Mundial",
    "Sumiu no mato tentando pegar um tatu à unha",
    "Decidiu morar num barco e pescar tilápia por 2 anos"
]

motivos_retorno = [
    "O time da quebrada implorou pelo seu retorno",
    "Quer mostrar que ainda dá um caldo",
    "Recebeu uma revelação espiritual durante o churrasco",
    "Descobriu que o joelho estava bom o tempo todo",
    "Voltou por pura teimosia",
    "Voltar à ativa era aposta perdida com o sogro",
    "Ouviu um 'você é o cara' e se emocionou",
    "Sonhou que fazia 3 gols no rival e acordou suando",
    "Quer se aposentar de verdade em grande estilo",
    "Aceitou o desafio de jogar uma última Copa da Várzea"
]

def gerar_atributos():
    return {
        "ritmo": random.randint(30, 85),
        "finalizacao": random.randint(30, 90),
        "passe": random.randint(35, 90),
        "drible": random.randint(40, 95),
        "defesa": random.randint(20, 75),
        "fisico": random.randint(50, 95)
    }

@app.route('/old-star', methods=['GET'])
def gerar_old_star():
    idade = random.choice(idades)
    posicao_antiga = random.choice(posicoes)
    posicao_atual = random.choice(posicoes)
    while posicao_atual == posicao_antiga:
        posicao_atual = random.choice(posicoes)

    historico = random.choice(historicos_aposentadoria)
    retorno = random.choice(motivos_retorno)
    atributos = gerar_atributos()

    return jsonify({
        "idade": idade,
        "posicao_antiga": posicao_antiga,
        "posicao_atual": posicao_atual,
        "historico_aposentadoria": historico,
        "motivo_retorno": retorno,
        "atributos": atributos
    })

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
