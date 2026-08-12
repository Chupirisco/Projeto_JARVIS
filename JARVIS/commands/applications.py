import subprocess

COMANDOS = {
    "abrir_vscode": {
        "sinonimos": ["abra o vscode", "abra o vs code", "abra o visual studio code", "abre o vscode", "abre o vs code"],
        "acao": "code",
        "mensagem": "Abrindo o VS Code."
    },
    "abrir_firefox": {
        "sinonimos": ["abrir firefox", "abre o firefox", "abrir navegador", "abre o navegador", "abra o firefox", "abra o navegador"],
        "acao": "firefox",
        "mensagem": "Abrindo o Firefox."
    },
}

def executar_comando(comando_id):
    comando = COMANDOS[comando_id]
    print(comando["mensagem"])
    subprocess.run([comando["acao"]])
