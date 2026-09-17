import os
import json
from dataclasses import dataclass, field, asdict
from typing import Dict

CONFIG_FILE = "data/config.json"

@dataclass
class BotConfig:
    discord_token: str = ""
    server_id: str = ""
    channel_id: str = ""
    target_user_id: str = ""
    headless: bool = True
    cooldown_min: int = 20
    cooldown_max: int = 120
    commands_enabled: Dict[str, bool] = field(default_factory=lambda: {
        "zwork": True,
        "zbeijar": True,
        "zcafune": True,
        "zabracar": True,
        "zsocar": True,
        "zrep": True
    })

def load_config() -> BotConfig:
    """Carrega as configurações do arquivo JSON, criando um padrão se não existir."""
    os.makedirs("data", exist_ok=True)
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Mescla com os padrões para garantir que novas chaves (como commands_enabled) não quebrem
            config = BotConfig()
            for k, v in data.items():
                if hasattr(config, k):
                    if k == "commands_enabled" and isinstance(v, dict):
                        config.commands_enabled.update(v)
                    else:
                        setattr(config, k, v)
            return config
        except Exception:
            return BotConfig()
    return BotConfig()

def save_config(config: BotConfig) -> None:
    """Salva a estrutura de configuração no arquivo JSON."""
    os.makedirs("data", exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(asdict(config), f, indent=4)
