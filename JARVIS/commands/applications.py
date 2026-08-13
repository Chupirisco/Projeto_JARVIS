import subprocess
from voice.tts import falar

COMANDOS = {
    "abrir_vscode": {
        "sinonimos": ["abrir vscode", "abrir vs code", "abrir visual studio code", "abre o vscode", "abre o vs code"],
        "descricao": "Abrir o editor de código Visual Studio Code",
        "acao": "code",
        "mensagem": "Abrindo o VS Code."
    },
    "abrir_firefox": {
        "sinonimos": ["abrir firefox", "abre o firefox", "abrir navegador", "abre o navegador"],
        "descricao": "Abrir o navegador de internet Firefox, também chamado de navegador ou internet",
        "acao": "firefox",
        "mensagem": "Abrindo o Firefox."
    },
}


def executar_comando(comando_id):
    comando = COMANDOS[comando_id]
    falar(comando["mensagem"])
    subprocess.run([comando["acao"]])