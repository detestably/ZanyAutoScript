import pyautogui
import time

# Função para enviar uma mensagem com um cooldown específico
def enviar_mensagem(mensagem, cooldown):
    pyautogui.write(mensagem)
    pyautogui.press('enter')
    time.sleep(cooldown)

# Função para clicar no botão verde "✔️ confirmar"
def clicar_confirmar():
    # Aqui você precisa encontrar a posição do botão "✔️ confirmar" na tela
    # Você pode usar o pyautogui para encontrar a posição do botão
    # Exemplo: botao_pos = pyautogui.locateOnScreen('confirmar.png')
    # pyautogui.click(botao_pos)
    pass

# Ciclo principal
while True:
    # Envia as mensagens com cooldown de 10 segundos
    enviar_mensagem("zwork <@id>", 10)
    enviar_mensagem("zbeijar <@id>", 10)
    enviar_mensagem("zcafune <@id>", 10)
    enviar_mensagem("zabracar <@id>", 10)
    enviar_mensagem("zsocar <@id7>", 10)

    # Envia a mensagem "zrep" com cooldown de 30 minutos e clica no botão "✔️ confirmar"
    enviar_mensagem("zrep <@id>", 1800)  # 1800 segundos = 30 minutos
    clicar_confirmar()

    # Espera 30 minutos antes de reiniciar o ciclo
    time.sleep(1800)  # 1800 segundos = 30 minutos
