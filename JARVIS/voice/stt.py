import sounddevice as sd
import scipy.io.wavfile as wavfile


def gravar_audio(duracao=5, taxa_amostragem=16000):
    print(f"Gravando por {duracao} segundos... fale agora.")
    audio = sd.rec(int(duracao * taxa_amostragem), samplerate=taxa_amostragem, channels=1, dtype="int16")
    sd.wait()
    print("Gravação concluída.")
    return audio, taxa_amostragem


if __name__ == "__main__":
    audio, taxa = gravar_audio()
    wavfile.write("teste_gravacao.wav", taxa, audio)
    print("Arquivo salvo como teste_gravacao.wav")