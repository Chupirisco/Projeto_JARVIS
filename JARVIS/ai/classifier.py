import json
import ollama
from commands.applications import COMANDOS

CANCELAR = "cancelar"


def montar_prompt(texto_usuario):
    lista_comandos = "\n".join(
        f'- {comando_id}: {dados["descricao"]}'
        for comando_id, dados in COMANDOS.items()
    )

    return f"""Você é um classificador de intenções. Sua única tarefa é identificar o que o usuário quer, com base na fala dele.

Comandos disponíveis:
{lista_comandos}

Além dos comandos, o usuário pode querer CANCELAR a conversa/sessão atual, dizendo algo como "nada não", "deixa pra lá", "esquece", "não precisa mais", etc.

Regras:
- Responda APENAS com um JSON, sem nenhum texto antes ou depois.
- O JSON deve ter exatamente a chave "comando".
- Se for um dos comandos da lista: {{"comando": "<id_do_comando>"}}
- Se o usuário quiser cancelar/desistir: {{"comando": "cancelar"}}
- Se não for nem comando nem cancelamento claro: {{"comando": null}}
- Nunca invente um comando que não esteja na lista.

Exemplos:
Fala: "abre o editor de código"
Resposta: {{"comando": "abrir_vscode"}}

Fala: "que horas são"
Resposta: {{"comando": null}}

Fala: "deixa pra lá, não precisa"
Resposta: {{"comando": "cancelar"}}

Fala do usuário: "{texto_usuario}"
Resposta:"""


def classificar_intencao(texto_usuario):
    prompt = montar_prompt(texto_usuario)

    resposta = ollama.chat(
        model="llama3:8b",
        messages=[{"role": "user", "content": prompt}]
    )

    conteudo = resposta["message"]["content"].strip()

    try:
        dados = json.loads(conteudo)
        comando_id = dados.get("comando")
        if isinstance(comando_id, str):
            comando_id = comando_id.strip()

        if comando_id == CANCELAR:
            return CANCELAR
        if comando_id in COMANDOS:
            return comando_id
        return None
    except (json.JSONDecodeError, AttributeError):
        return None