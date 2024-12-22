import whisper
from pydub import AudioSegment

def transcribe_audio(file_path):
    print("Конвертирую MP3 в WAV...")
    audio = AudioSegment.from_file(file_path, format="mp3")
    wav_path = "converted.wav"
    audio.export(wav_path, format="wav")
    
    print("Загружаю модель...")
    model = whisper.load_model("base")
    
    print("Обрабатываю файл...")
    result = model.transcribe(wav_path)
    
    print("Текст из файла:")
    print(result["text"])

if __name__ == "__main__":
    audio_file = "music.mp3"
    try:
        transcribe_audio(audio_file)
    except FileNotFoundError:
        print(f"Файл '{audio_file}' не найден. Поместите файл с этим именем в текущую директорию.")
