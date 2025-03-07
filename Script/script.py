import pyautogui
import time

# Solicita o ID do usuário
user_id = input("Digite o ID do usuário (apenas os números dentro do <@id>): ")

# Função para enviar uma mensagem com um cooldown específico
def enviar_mensagem(mensagem, cooldown):
    pyautogui.write(mensagem)
    pyautogui.press('enter')
    time.sleep(cooldown)

# Função para clicar no botão verde "✔️ confirmar"
def clicar_confirmar():
    try:
        print("Procurando o botão '✔️ confirmar' na tela...")
        # Procura o botão na tela
        botao_pos = pyautogui.locateOnScreen('confirmar.png', confidence=0.8)
        if botao_pos:
            print(f"Botão encontrado na posição: {botao_pos}")
            # Calcula o centro do botão
            botao_center = pyautogui.center(botao_pos)
            print(f"Movendo o mouse para o centro do botão: {botao_center}")
            pyautogui.moveTo(botao_center)
            print("Clicando no botão...")
            pyautogui.click()
            print("Botão '✔️ confirmar' clicado com sucesso!")
            return True  # Retorna True se o botão foi clicado
        else:
            print("Botão '✔️ confirmar' não encontrado na tela.")
            return False  # Retorna False se o botão não foi encontrado
    except Exception as e:
        print(f"Erro ao procurar o botão: {e}")
        return False  # Retorna False em caso de erro

# Ciclo principal
while True:
    # Envia as mensagens com cooldown de 10 segundos
    time.sleep(5)
    enviar_mensagem(f"zwork <@{user_id}>", 10)
    enviar_mensagem(f"zbeijar <@{user_id}>", 10)
    enviar_mensagem(f"zcafune <@{user_id}>", 10)
    enviar_mensagem(f"zabracar <@{user_id}>", 10)
    enviar_mensagem(f"zsocar <@{user_id}>", 10)

    # Envia a mensagem "zrep"
    enviar_mensagem(f"zrep <@{user_id}>", 0)  # Sem cooldown aqui

    # Procura o botão "✔️ confirmar" e clica nele
    time.sleep(3)
    if clicar_confirmar():
        print("Botão '✔️ confirmar' clicado com sucesso após o envio da mensagem 'zrep'.")
    else:
        print("Falha ao clicar no botão '✔️ confirmar'.")

    # Aguarda 2 segundos e faz um clique na posição atual do mouse
    time.sleep(2)
    pyautogui.click()
    print("Click realizado após 4 segundos!")

    # Espera 30 minutos antes de reiniciar o ciclo
    time.sleep(1800)  # 1800 segundos = 30 minutos
