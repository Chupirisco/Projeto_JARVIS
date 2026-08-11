# 🤖 JARVIS

Assistente virtual pessoal por voz, local e gratuito, inspirado no JARVIS dos filmes do Homem de Ferro.

> Ainda em fase inicial de desenvolvimento. Este README será atualizado conforme o projeto evolui.

---

## 💡 Sobre o projeto

O JARVIS é um assistente de voz para notebook capaz de:

- ouvir comandos por voz, ativado pela palavra **"JARVIS"**;
- entender variações naturais de fala (ex: "abre o vscode" vs "quero abrir o visual studio code");
- executar ações no computador (abrir programas, pesquisar na web, etc.);
- conversar livremente quando não é um comando conhecido;
- responder por voz.

O objetivo não é criar uma IA extremamente avançada, e sim um assistente **simples que realmente funcione**, rodando 100% no hardware do usuário.

---

## ⚙️ Princípios do projeto

- **Custo zero.** Sem APIs pagas, assinaturas ou dependências que exijam cartão de crédito. Prioridade total para software livre e modelos locais.
- **Local em primeiro lugar.** O funcionamento principal não depende de internet. Cloud só entra futuramente, e apenas se for opcional.
- **Simples antes de inteligente.** É preferível um assistente limitado que funcione do que um sistema ambicioso que dependa de recursos que o hardware não tem.
- **Feedback constante.** O JARVIS sempre informa por voz o que está fazendo — nunca executa uma ação em silêncio.
- **Fala natural.** Sem exigir comandos formais ou robóticos, mas também sem forçar uma naturalidade artificial demais.

---

## 🧠 Como funciona (visão geral)

```
Voz do usuário
      ↓
Wake word ("JARVIS")
      ↓
Speech-to-Text (local)
      ↓
JARVIS Core (Python)
      ↓
Roteador de intenção
      │
      ├── Match direto no catálogo de comandos → executa
      │
      └── Sem match → classificador de IA local decide
                │
                ├── Reconheceu comando → executa
                ├── Reconheceu cancelamento → encerra escuta
                └── Não entendeu → pede pra repetir
      ↓
Resposta falada (Text-to-Speech, local)
```

Comandos simples e determinísticos (abrir programas, por exemplo) são resolvidos sem IA, por reconhecimento direto de texto. Quando a fala foge do padrão esperado, um modelo de linguagem local (via [Ollama](https://ollama.com/)) entra em ação para interpretar a intenção — sempre respondendo em formato fechado, nunca texto livre, evitando comportamento imprevisível.

---

## 🖥️ Hardware-alvo

Desenvolvido e testado inicialmente em uma máquina modesta, sem GPU dedicada:

- Notebook Samsung Book NP550XDA-KP1BR
- Intel Core i3-1115G4
- 16 GB RAM DDR4
- Intel UHD Graphics integrada

Por isso, o projeto prioriza modelos de linguagem pequenos (~1-4B parâmetros) e evita qualquer dependência de hardware pesado.

---

## 🗺️ Roadmap

- [ ] **0.1** — Wake word, reconhecimento de voz, comandos básicos, resposta por voz
- [ ] **0.2** — Pesquisa na web, controle de volume, arquivos/pastas, comandos de sistema
- [ ] **0.3** — Classificador de intenção via IA local + conversação livre
- [ ] **0.4** — Memória e contexto entre conversas
- [ ] **0.5** — Automação em múltiplas etapas, com verificação de resultado
- [ ] **1.0** — Assistente pessoal completo

---

## 🛠️ Stack (planejada)

| Camada | Tecnologia (a definir/testar) |
|---|---|
| Linguagem principal | Python |
| Wake word | A definir (candidato: openWakeWord) |
| Speech-to-Text | A definir (candidatos: Whisper leve, Vosk) |
| Text-to-Speech | A definir |
| Modelo de linguagem local | A definir, via Ollama |
| Sistema operacional (dev) | Zorin OS / Linux |
| Navegador | Firefox |

---

## 📁 Estrutura (referência, ainda em construção)

```
JARVIS/
├── main.py
├── core/        → roteador de intenção, estado da sessão, config
├── voice/       → wake word, speech-to-text, text-to-speech
├── commands/    → ações reais (abrir programas, sistema, arquivos)
├── ai/          → integração com o modelo local (classificação + conversa)
└── memory/      → memória persistente (futuro)
```

A estrutura final é construída de forma incremental, camada por camada, testando cada parte isoladamente antes de integrar.

---

## 🔐 Segurança e privacidade

- Comandos locais (abrir programas, arquivos, etc.) nunca são enviados para serviços externos.
- O JARVIS sempre avisa por voz antes/durante a execução de qualquer ação.
- Não há automação de ações destrutivas ou de risco no escopo atual do projeto.

---

## 📌 Status

Projeto em fase de planejamento e estruturação inicial. Nenhum código funcional publicado ainda.
