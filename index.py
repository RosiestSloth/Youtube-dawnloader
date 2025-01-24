import yt_dlp
import os

def baixar_musica_yt_dlp(url, pasta_destino):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar música: {e}")

# Exemplo de uso
if __name__ == "__main__":
    url = input("Insira a URL do vídeo do YouTube: ")
    pasta_destino = "musicas"
    os.makedirs(pasta_destino, exist_ok=True)
    baixar_musica_yt_dlp(url, pasta_destino)
