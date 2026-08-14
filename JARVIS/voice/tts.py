import subprocess
import tempfile
import os


def falar(texto):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as arquivo_temp:
        caminho_audio = arquivo_temp.name

    subprocess.run(
        ["piper", "--model", "pt_BR-faber-medium", "--output_file", caminho_audio],
        input=texto.encode("utf-8")
    )

    subprocess.run(["aplay", caminho_audio], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    os.remove(caminho_audio)
