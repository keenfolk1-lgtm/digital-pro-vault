"""
Генератор озвучки для YouTube Shorts / TikTok / Reels на базе бесплатного нейросетевого голоса Microsoft Edge-TTS!
Озвучивает любой русский или английский текст студийным голосом Dmitry / Svetlana / Christopher и сохраняет чистый MP3 + субтитры .srt!
Установка: pip install edge-tts
Запуск: python shorts_ai_generator.py
"""

import asyncio
import edge_tts

TEXT_TO_SPEAK = (
    "Знаете ли вы, почему 90 процентов трейдеров теряют депозит в первый месяц? "
    "Всё дело в одной психологической ловушке, которую используют маркетмейкеры!"
)
VOICE = "ru-RU-DmitryNeural"  # Мужской студийный голос (или ru-RU-SvetlanaNeural — женский)
OUTPUT_MP3 = "shorts_voiceover.mp3"
OUTPUT_SRT = "shorts_subtitles.srt"

async def generate():
    communicate = edge_tts.Communicate(TEXT_TO_SPEAK, VOICE, rate="+10%")
    submaker = edge_tts.SubMaker()
    with open(OUTPUT_MP3, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])
    with open(OUTPUT_SRT, "w", encoding="utf-8") as sf:
        sf.write(submaker.generate_subs())
    print(f"✅ Готово! Сохранены файлы: {OUTPUT_MP3} и {OUTPUT_SRT}")

if __name__ == "__main__":
    asyncio.run(generate())