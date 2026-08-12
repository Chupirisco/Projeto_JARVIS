from commands.applications import COMANDOS, executar_comando


def identificar_comando(texto):
    texto = texto.lower().strip()
    for comando_id, dados in COMANDOS.items():
        if texto in dados["sinonimos"]:
            return comando_id
    return None


def processar_texto(texto):
    comando_id = identificar_comando(texto)
    if comando_id:
        executar_comando(comando_id)
    else:
        print("Não entendi. Pode repetir?")


if __name__ == "__main__":
    while True:
        texto = input("Você: ")
        processar_texto(texto)