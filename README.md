<div align="center">
  <h1 align="center">Z-Auto 🤖</h1>
  <p align="center">
    <strong>Automação Inteligente e Invisível para o Bot Zany no Discord</strong>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/Playwright-Automated-green?style=for-the-badge&logo=playwright" alt="Playwright">
    <img src="https://img.shields.io/badge/Typer-CLI-orange?style=for-the-badge" alt="Typer">
  </p>
</div>

---

## 📌 Sobre o Projeto

O **Z-Auto** é uma ferramenta de automação avançada criada para interagir com o bot *Zany* no Discord de maneira completamente autônoma, segura e **invisível**.

Diferente de scripts tradicionais de Macro (como PyAutoGUI) que sequestram o seu mouse e teclado, o Z-Auto utiliza a tecnologia **Playwright** para rodar um navegador Chromium em *background* (modo Headless). Isso permite que você continue usando o seu computador normalmente enquanto a automação trabalha para você em um servidor e canal específicos!

### ✨ Principais Funcionalidades

- **🥷 Navegação Invisível (Headless):** O bot roda por baixo dos panos, sem abrir janelas ou tomar o controle do seu PC.
- **🕒 Humanização Avançada:** Os tempos de espera (cooldowns) são aleatorizados a cada execução para simular com precisão o comportamento de um usuário real e evitar detecções.
- **⚙️ Menu CLI Interativo:** Interface de linha de comando belíssima construída com `Typer` e `Rich`, permitindo configurar IDs, Token e Tempos de forma dinâmica.
- **🔓 Injeção de Token Segura:** Burlar as restrições de login do Discord injetando o token de usuário diretamente no `localStorage` do navegador isolado.
- **🎯 Clique Dinâmico em Componentes:** O bot escaneia a página HTML dinamicamente atrás do botão "✔️ confirmar", eliminando a necessidade de buscar por "prints de tela".

---

## 🚀 Como Instalar

Siga os passos abaixo para preparar o seu ambiente:

1. **Clone o repositório ou acesse a pasta do projeto:**
   ```bash
   cd caminho/para/o/Zany
   ```

2. **Instale as dependências Python necessárias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Baixe o navegador invisível do Playwright:**
   ```bash
   playwright install chromium
   ```

---

## 🎮 Como Usar

O projeto possui um menu interativo extremamente fácil de usar. Para iniciá-lo, basta rodar:

```bash
python main.py
```

### O Menu Principal
Ao iniciar, você verá uma interface rica e colorida com as seguintes opções:

- **1. Iniciar Bot:** Começa a automação imediatamente.
- **2. Configurações Avançadas:** Menu onde você pode salvar:
  - Seu Token do Discord
  - ID do Servidor & ID do Canal
  - ID do Usuário Alvo
  - Controlar o intervalo aleatório (Ex: de 20 a 120 minutos)
  - Ligar/Desligar ações específicas (zwork, zbeijar, etc)

*(Dica: Se quiser pular o menu e rodar a automação diretamente, execute `python main.py run`)*

---

## ⚠️ Aviso Legal (Disclaimer)

O uso de "Self-Bots" (automatizar contas de usuários comuns) vai contra os **Termos de Serviço (TOS) do Discord**. Embora o **Z-Auto** possua sistemas robustos de "humanização" (atrasos aleatórios e controle de navegador simulando um usuário real) para mitigar os riscos e ser extremamente difícil de detectar, você deve utilizar esta ferramenta por sua própria conta e risco. Os desenvolvedores não se responsabilizam por eventuais suspensões da sua conta.

---
<div align="center">
  Feito com 💜 para maximizar o seu grind!
</div>
