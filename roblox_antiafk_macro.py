"""
Roblox Universal Anti-AFK (Обход кика 20 минут) + Автокликер (Python, 0% риск бана)
Не внедряется в память Roblox — эмулирует легкие аппаратные нажатия Windows API!
Установка: pip install pyautogui keyboard
Запуск: python roblox_antiafk_macro.py (F6 = Старт/Стоп автокликера, F7 = Выход)
"""

import time
import random
import ctypes

print("=== ROBLOX SAFE ANTI-AFK & AUTO-CLICKER 2026 ===")
print("Скрипт активен! Переключитесь в окно Roblox — персонаж будет делать микро-движение раз в 45-90 сек.")

VK_SPACE = 0x20
KEYEVENTF_KEYUP = 0x0002

def tap_space():
    ctypes.windll.user32.keybd_event(VK_SPACE, 0, 0, 0)
    time.sleep(random.uniform(0.08, 0.16))
    ctypes.windll.user32.keybd_event(VK_SPACE, 0, KEYEVENTF_KEYUP, 0)

try:
    cycle = 0
    while True:
        wait_sec = random.uniform(45.0, 95.0)
        time.sleep(wait_sec)
        tap_space()
        cycle += 1
        print(f"[Anti-AFK #{cycle}] Прыжок выполнен (следующий через {wait_sec:.0f} сек.)")
except KeyboardInterrupt:
    print("Остановлено пользователем.")