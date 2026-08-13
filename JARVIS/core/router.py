from commands.applications import COMANDOS, executar_comando
from ai.classifier import classificar_intencao, CANCELAR
from voice.tts import falar


def identificar_comando_regex(texto):
    texto = texto.lower().strip()
    for comando_id, dados in COMANDOS.items():
        if texto in dados["sinonimos"]:
            return comando_id
    return None


def processar_texto(texto):
    comando_id = identificar_comando_regex(texto)

    if comando_id:
        executar_comando(comando_id)
        return

    resultado = classificar_intencao(texto)

    if resultado == CANCELAR:
        falar("Ok, cancelado.")
    elif resultado:
        executar_comando(resultado)
    else:
        falar("Não entendi. Pode repetir?")


if __name__ == "__main__":
    while True:
        texto = input("Você: ")
        processar_texto(texto)