import sys
import typer
from rich.console import Console
from ui.banner import show_banner
from core.bot import run_bot
from core.config import load_config, save_config

app = typer.Typer(help="Z-Auto - Automação de Bot com Playwright.")
console = Console()

def menu_configuracoes():
    """Menu para gerenciar configurações avançadas."""
    config = load_config()
    while True:
        show_banner(console, "CONFIGURAÇÕES")
        
        console.print(f"[cyan]1.[/] Token Discord: [dim]{'Preenchido' if config.discord_token else 'Vazio'}[/]")
        console.print(f"[cyan]2.[/] ID do Servidor: [dim]{config.server_id if config.server_id else 'Vazio'}[/]")
        console.print(f"[cyan]3.[/] ID do Canal: [dim]{config.channel_id if config.channel_id else 'Vazio'}[/]")
        console.print(f"[cyan]4.[/] ID do Usuário Alvo: [dim]{config.target_user_id if config.target_user_id else 'Vazio'}[/]")
        console.print(f"[cyan]5.[/] Intervalo do Ciclo: [dim]{config.cooldown_min} a {config.cooldown_max} minutos[/]")
        console.print(f"[cyan]6.[/] Gerenciar Comandos (Ligar/Desligar)")
        console.print(f"[cyan]7.[/] Navegador Invisível (Headless): [bold]{'Sim' if config.headless else 'Não'}[/]")
        console.print("[cyan]0.[/] Voltar\n")
        
        escolha = console.input("[bold]Escolha uma opção: [/]")
        
        if escolha == "1":
            token = console.input("[bold]Cole seu Token do Discord: [/]")
            if token: config.discord_token = token
        elif escolha == "2":
            sid = console.input("[bold]ID do Servidor: [/]")
            if sid: config.server_id = sid
        elif escolha == "3":
            cid = console.input("[bold]ID do Canal: [/]")
            if cid: config.channel_id = cid
        elif escolha == "4":
            tid = console.input("[bold]ID do Usuário Alvo: [/]")
            if tid: config.target_user_id = tid
        elif escolha == "5":
            try:
                cmin = int(console.input("[bold]Minutos mínimos de espera (ex: 20): [/]"))
                cmax = int(console.input("[bold]Minutos máximos de espera (ex: 120): [/]"))
                if cmin > 0 and cmax >= cmin:
                    config.cooldown_min = cmin
                    config.cooldown_max = cmax
                    console.print("[green]Tempo de espera atualizado![/]")
                else:
                    console.print("[red]Valores inválidos.[/]")
            except ValueError:
                console.print("[red]Digite apenas números.[/]")
            console.input("[dim]Pressione Enter...[/]")
        elif escolha == "6":
            menu_comandos(config)
        elif escolha == "7":
            config.headless = not config.headless
            console.print(f"[green]Navegador Invisível agora está: {'Sim' if config.headless else 'Não'}[/]")
            console.input("[dim]Pressione Enter...[/]")
        elif escolha == "0":
            save_config(config)
            break
        
        save_config(config)

def menu_comandos(config):
    """Sub-menu para gerenciar os comandos ativos."""
    while True:
        show_banner(console, "COMANDOS")
        comandos_lista = list(config.commands_enabled.keys())
        
        for i, cmd in enumerate(comandos_lista, 1):
            status = "[green]ON[/]" if config.commands_enabled[cmd] else "[red]OFF[/]"
            console.print(f"[cyan]{i}.[/] {cmd.ljust(15)} {status}")
        console.print("[cyan]0.[/] Voltar\n")
        
        escolha = console.input("[bold]Digite o número para alterar (ou 0 para voltar): [/]")
        if escolha == "0":
            break
        
        try:
            idx = int(escolha) - 1
            if 0 <= idx < len(comandos_lista):
                cmd_name = comandos_lista[idx]
                config.commands_enabled[cmd_name] = not config.commands_enabled[cmd_name]
                save_config(config)
        except ValueError:
            pass

@app.callback(invoke_without_command=True)
def interactive(ctx: typer.Context) -> None:
    """Menu principal do Z-Auto."""
    if ctx.invoked_subcommand is None:
        while True:
            show_banner(console, "MENU PRINCIPAL")
            console.print("\n[bold magenta]1.[/] Iniciar Bot")
            console.print("[bold magenta]2.[/] Configurações Avançadas")
            console.print("[bold magenta]0.[/] Sair\n")
            
            choice = console.input("[bold]Escolha uma opção: [/]")
            if choice == "1":
                show_banner(console, "EXECUTANDO AUTOMAÇÃO")
                run_bot()
                console.input("\n[dim]Pressione Enter para voltar ao menu...[/]")
            elif choice == "2":
                menu_configuracoes()
            elif choice == "0":
                sys.exit(0)

@app.command()
def run():
    """Roda a automação diretamente pela linha de comando."""
    show_banner(console, "EXECUTANDO AUTOMAÇÃO")
    run_bot()

if __name__ == "__main__":
    app()
