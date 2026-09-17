import time
import random
import sys
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeRemainingColumn
from playwright.sync_api import sync_playwright, TimeoutError
from core.config import load_config

console = Console()

def wait_with_progress(seconds: int, description: str = "Aguardando..."):
    """Espera utilizando uma barra de progresso do Rich."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(f"[cyan]{description}", total=seconds)
        for _ in range(seconds):
            time.sleep(1)
            progress.advance(task)

def inject_token_and_login(page, token: str):
    """Injeta o token do Discord no LocalStorage para logar direto."""
    console.print("[dim]Acessando a página de login para injetar o token...[/]")
    page.goto("https://discord.com/login")
    
    # O Discord tenta bloquear modificações no localStorage. 
    # O script abaixo contorna isso criando um iframe temporário.
    js_code = f"""
    (() => {{
        setInterval(() => {{
            let iframe = document.createElement('iframe');
            document.body.appendChild(iframe);
            iframe.contentWindow.localStorage.token = '"{token}"';
        }}, 50);
        setTimeout(() => {{
            location.reload();
        }}, 2500);
    }})();
    """
    page.evaluate(js_code)
    
    # Aguarda o reload da página que ocorre no setTimeout de 2500ms
    console.print("[dim]Aguardando o recarregamento automático (2.5s)...[/]")
    page.wait_for_timeout(3500)

def run_bot():
    """Ciclo principal do bot usando Playwright."""
    config = load_config()
    
    # Validações Iniciais
    faltando = []
    if not config.discord_token: faltando.append("Token do Discord")
    if not config.server_id: faltando.append("ID do Servidor")
    if not config.channel_id: faltando.append("ID do Canal")
    if not config.target_user_id: faltando.append("ID do Usuário Alvo")
    
    if faltando:
        console.print(f"\n[bold red]⚠ Faltam configurações obrigatórias para rodar:[/]")
        for item in faltando:
            console.print(f"  - {item}")
        console.print("[yellow]Por favor, volte ao menu e acesse 'Configurações' para preencher os dados.[/]\n")
        return

    console.print(f"\n[bold magenta]Iniciando Z-Auto via Navegador Invisível...[/]")
    console.print("[dim](Pressione Ctrl+C nesta janela a qualquer momento para parar)[/]\n")
    
    ciclo = 1
    
    try:
        with sync_playwright() as p:
            console.print("[dim]Iniciando o navegador Chromium...[/]")
            browser = p.chromium.launch(headless=config.headless)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = context.new_page()
            
            # Login por Token
            inject_token_and_login(page, config.discord_token)
            
            # Navegar para o canal específico
            url_canal = f"https://discord.com/channels/{config.server_id}/{config.channel_id}"
            console.print(f"[dim]Navegando para o servidor/canal: {url_canal}[/]")
            page.goto(url_canal)
            
            # Aguarda a tela carregar para confirmar que logou
            try:
                # Espera a caixa de texto do chat aparecer
                page.wait_for_selector('div[role="textbox"]', timeout=20000)
                console.print("[green]✓ Login efetuado e chat encontrado com sucesso![/]")
            except TimeoutError:
                console.print("[bold red]Falha ao acessar o canal. O Token é válido? O Bot está no servidor?[/]")
                return
            
            # Loop principal
            while True:
                console.print(f"\n[bold white on magenta] --- CICLO {ciclo} --- [/]")
                
                # Prepara as mensagens que estão ativadas
                comandos = [
                    ("zwork", ""),
                    ("zbeijar", f" <@{config.target_user_id}>"),
                    ("zcafune", f" <@{config.target_user_id}>"),
                    ("zabracar", f" <@{config.target_user_id}>"),
                    ("zsocar", f" <@{config.target_user_id}>"),
                    ("zrep", f" <@{config.target_user_id}>")
                ]
                
                mensagens = [cmd + sufixo for cmd, sufixo in comandos if config.commands_enabled.get(cmd, False)]
                
                if not mensagens:
                    console.print("[yellow]Nenhum comando ativado nas configurações.[/]")
                    break
                
                for i, mensagem in enumerate(mensagens):
                    cooldown = 0 if i == len(mensagens) - 1 else random.randint(20, 120)
                    
                    # Digita e envia
                    chat_box = page.locator('div[role="textbox"]')
                    chat_box.fill(mensagem)
                    page.keyboard.press('Enter')
                    
                    console.print(f"[green]✓[/] Mensagem enviada: [bold]'{mensagem}'[/]")
                    
                    if cooldown > 0:
                        wait_with_progress(cooldown, f"Cooldown aleatório ({cooldown}s)")
                
                # Clicar no botão Confirmar (Zany Bot)
                console.print(f"[dim]Aguardando 3-5s para o bot Zany responder com o botão...[/]")
                time.sleep(random.uniform(3.0, 5.0))
                
                try:
                    # Procurar botão que tenha um "✔️" ou texto "confirmar" no DOM
                    # No Discord, botões de componentes geralmente são botões HTML 
                    btn = page.locator('button', has_text="✔️")
                    if btn.count() > 0:
                        # Clica no último botão com esse símbolo enviado no chat
                        btn.last.click()
                        console.print("[green]✓ Botão '✔️ confirmar' encontrado no HTML e clicado com sucesso![/]")
                    else:
                        console.print("[yellow]⚠ Botão '✔️ confirmar' não encontrado nas mensagens recentes.[/]")
                except Exception as e:
                    console.print(f"[red]Erro ao tentar clicar no botão:[/] {e}")
                
                # Cooldown do Ciclo (Baseado na configuração)
                console.print(f"\n[cyan]Ciclo {ciclo} finalizado![/]")
                minutos_espera = random.randint(config.cooldown_min, config.cooldown_max)
                segundos_espera = minutos_espera * 60
                
                wait_with_progress(segundos_espera, f"Aguardando próximo ciclo ({minutos_espera} minutos)")
                ciclo += 1

    except KeyboardInterrupt:
        console.print("\n[bold red]Automação interrompida pelo usuário (Ctrl+C).[/]")
    except Exception as e:
        console.print(f"\n[bold red]Erro crítico na automação:[/] {e}")
