import subprocess
from voice.tts import falar

COMANDOS = {
    "abrir_vscode": {
        "sinonimos": ["abrir vscode", "abrir vs code", "abrir visual studio code", "abre o vscode", "abre o vs code"],
        "descricao": "Abrir o editor de código Visual Studio Code",
        "acao": ["code"],
        "mensagem": "Abrindo o VS Code."
    },
    "abrir_firefox": {
        "sinonimos": ["abrir firefox", "abre o firefox", "abrir navegador", "abre o navegador"],
        "descricao": "Abrir o navegador de internet Firefox, também chamado de navegador ou internet",
        "acao": ["firefox"],
        "mensagem": "Abrindo o Firefox."
    },
    "abrir_terminal": {
        "sinonimos": ["abrir terminal", "abre o terminal", "abrir console"],
        "descricao": "Abrir o terminal do sistema",
        "acao": ["gnome-terminal"],
        "mensagem": "Abrindo o terminal."
    },
    "abrir_arquivos": {
        "sinonimos": ["abrir gerenciador de arquivos", "abrir arquivos", "abre os arquivos", "abrir pasta de arquivos"],
        "descricao": "Abrir o gerenciador de arquivos do sistema",
        "acao": ["nautilus"],
        "mensagem": "Abrindo o gerenciador de arquivos."
    },
    "abrir_spotify": {
        "sinonimos": ["abrir spotify", "abre o spotify", "abrir musica", "quero ouvir musica"],
        "descricao": "Abrir o Spotify para ouvir música",
        "acao": ["flatpak", "run", "com.spotify.Client"],
        "mensagem": "Abrindo o Spotify."
    },
}


def executar_comando(comando_id):
    comando = COMANDOS[comando_id]
    falar(comando["mensagem"])
    subprocess.run(comando["acao"])