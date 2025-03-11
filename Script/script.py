import pyautogui
import time

# Constantes
COOLDOWN_MENSAGEM = 10
COOLDOWN_CICLO = 1800  # 30 minutos
COOLDOWN_CLIQUE = 2
COOLDOWN_CONFIRMAR = 3

# Solicita o ID do usuário
user_id = input("Digite o ID do usuário (apenas os números dentro do <@id>): ")

# Função para enviar uma mensagem com um cooldown específico
def enviar_mensagem(mensagem, cooldown=COOLDOWN_MENSAGEM):
    pyautogui.write(mensagem)
    pyautogui.press('enter')
    time.sleep(cooldown)

# Função para clicar no botão verde "✔️ confirmar"
def clicar_confirmar():
    try:
        print("Procurando o botão '✔️ confirmar' na tela...")
        botao_pos = pyautogui.locateOnScreen('confirmar.png', confidence=0.8)
        if botao_pos:
            botao_center = pyautogui.center(botao_pos)
            print(f"Movendo o mouse para o centro do botão: {botao_center}")
            pyautogui.moveTo(botao_center)
            pyautogui.click()
            print("Botão '✔️ confirmar' clicado com sucesso!")
            return True
        else:
            print("Botão '✔️ confirmar' não encontrado na tela.")
            return False
    except Exception as e:
        print(f"Erro ao procurar o botão: {e}")
        return False

# Ciclo principal
while True:
    # Envia as mensagens com cooldown
    mensagens = [
        "zwork",
        f"zbeijar <@{user_id}>",
        f"zcafune <@{user_id}>",
        f"zabracar <@{user_id}>",
        f"zsocar <@{user_id}>",
        f"zrep <@{user_id}>"
    ]

    for mensagem in mensagens:
        enviar_mensagem(mensagem, COOLDOWN_MENSAGEM if mensagem != "zrep" else 0)

    # Procura o botão "✔️ confirmar" e clica nele
    time.sleep(COOLDOWN_CONFIRMAR)
    if clicar_confirmar():
        print("Botão '✔️ confirmar' clicado com sucesso após o envio da mensagem 'zrep'.")
    else:
        print("Falha ao clicar no botão '✔️ confirmar'.")

    # Aguarda e faz um clique na posição atual do mouse
    time.sleep(COOLDOWN_CLIQUE)
    pyautogui.click()
    print("Click realizado após 2 segundos!")

    # Espera 30 minutos antes de reiniciar o ciclo
    time.sleep(COOLDOWN_CICLO)
