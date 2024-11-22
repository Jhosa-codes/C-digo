import matplotlib.pyplot as plt

# Frequência estimada dos sintomas em casos confirmados de COVID
frequencia_covid_estimada = {
    "febre": 0.8,
    "tosse": 0.6,
    "cansaço": 0.7,
    "falta de ar": 0.5,
    "perda de paladar/olfato": 0.9,
    "dor de garganta": 0.3,
    "dores no corpo": 0.5,
    "dor de cabeça": 0.4,
    "calafrios": 0.3,
    "coriza": 0.2
}

# Perguntas e sintomas com pesos
perguntas_sintomas = {
    "Você está com febre?": ("febre", 3),
    "Tem tosse persistente?": ("tosse", 3),
    "Sente um cansaço extremo?": ("cansaço", 2),
    "Está com falta de ar?": ("falta de ar", 4),
    "Perdeu o paladar ou olfato recentemente?": ("perda de paladar/olfato", 5),
    "Sente dor de garganta?": ("dor de garganta", 1),
    "Está com dores no corpo?": ("dores no corpo", 2),
    "Tem dor de cabeça?": ("dor de cabeça", 1),
    "Sente calafrios?": ("calafrios", 2),
    "Está com coriza ou nariz escorrendo?": ("coriza", 1)
}

# Função principal do diagnóstico
def diagnosticar():
    """
    Coleta respostas do usuário, calcula a pontuação com base nos sintomas
    e exibe o diagnóstico. Também chama a função para gerar o gráfico.
    """
    pontuacao = 0  # Pontuação inicial
    sintomas_usuario = []  # Lista de sintomas relatados pelo usuário

    print("Responda às perguntas com 's' para sim e 'n' para não.\n")

    for pergunta, (sintoma, peso) in perguntas_sintomas.items():
        while True:  # Validação para garantir respostas válidas
            resposta = input(pergunta + " (s/n): ").strip().lower()
            if resposta in ["s", "n"]:
                break  # Se a resposta for válida, sai do loop
            print("Resposta inválida. Por favor, responda apenas com 's' ou 'n'.")

        if resposta == "s":  # Se o usuário respondeu "sim"
            pontuacao += peso  # Adiciona o peso do sintoma à pontuação
            sintomas_usuario.append(sintoma)  # Registra o sintoma relatado

    # Diagnóstico baseado na pontuação total
    if pontuacao >= 15:
        diagnostico = "Provável COVID-19. Procure atendimento médico."
    elif 8 <= pontuacao < 15:
        diagnostico = "Possível COVID-19 ou outra virose. Fique atento aos sintomas."
    else:
        diagnostico = "Sintomas leves, provavelmente não COVID-19, mas monitore sua saúde."

    print(f"\nDiagnóstico: {diagnostico}")
    exibir_grafico_frequencia(sintomas_usuario)  # Exibe o gráfico ao final

# Função para exibir o gráfico de frequência
def exibir_grafico_frequencia(sintomas_usuario):
    """
    Gera um gráfico comparando a frequência estimada de sintomas para COVID-19
    com os sintomas relatados pelo usuário.
    """
    # Preparar os dados do gráfico
    sintomas = list(frequencia_covid_estimada.keys())  # Todos os sintomas conhecidos
    frequencias_estimadas = [frequencia_covid_estimada[s] for s in sintomas]  # Frequências estimadas
    frequencias_usuario = [1.0 if s in sintomas_usuario else 0.0 for s in sintomas]  # Frequências do usuário

    # Criar o gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 5))  # Define o tamanho do gráfico
    ax.bar(
        sintomas,
        frequencias_estimadas,
        color='blue',
        alpha=0.6,
        label="Frequência Estimada em Casos de COVID"
    )  # Barras azuis para frequência estimada
    ax.bar(
        sintomas,
        frequencias_usuario,
        color='red',
        alpha=0.6,
        label="Sintomas do Usuário"
    )  # Barras vermelhas para frequência do usuário

    # Configurar o gráfico
    ax.set_xlabel("Sintomas")  # Rótulo do eixo X
    ax.set_ylabel("Frequência")  # Rótulo do eixo Y
    ax.set_title("Comparação de Sintomas com Frequência Estimada para COVID")  # Título do gráfico
    plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos dos sintomas para melhorar a legibilidade
    ax.legend()  # Adiciona uma legenda para identificar as barras

    # Exibir o gráfico
    plt.show()

# Executar o diagnóstico
diagnosticar()