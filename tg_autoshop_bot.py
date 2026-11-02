"""
Telegram Бот Автопродаж Цифровых Товаров (Python + SQLite + Админ-Панель)
Установка: pip install aiogram==3.*
Запуск: вставьте ваш BOT_TOKEN и ADMIN_ID ниже и запустите: python tg_autoshop_bot.py
"""

import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "ВСТАВЬТЕ_ТОКЕН_ОТ_BOTFATHER"
ADMIN_ID = 123456789  # Ваш Telegram ID (узнать в @userinfobot)

def init_db():
    conn = sqlite3.connect("shop.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, desc TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY AUTOINCREMENT, item_id INTEGER, secret_data TEXT)")
    conn.commit()
    conn.close()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(msg: types.Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="🛒 Каталог товаров", callback_data="catalog")
    kb.button(text="👤 Профиль", callback_data="profile")
    if msg.from_user.id == ADMIN_ID:
        kb.button(text="⚙️ Админ-панель", callback_data="admin")
    kb.adjust(1)
    await msg.answer("👋 Добро пожаловать в магазин автовыдачи 24/7!\nВыберите раздел ниже:", reply_markup=kb.as_markup())

@dp.callback_query(F.data == "catalog")
async def show_catalog(cb: types.CallbackQuery):
    conn = sqlite3.connect("shop.db")
    items = conn.execute("SELECT id, name, price FROM items").fetchall()
    conn.close()
    kb = InlineKeyboardBuilder()
    for i_id, name, price in items:
        kb.button(text=f"{name} — {price} ₽", callback_data=f"buy_{i_id}")
    kb.button(text="🔙 Назад", callback_data="back")
    kb.adjust(1)
    await cb.message.edit_text("🛒 Выберите товар для мгновенной покупки:", reply_markup=kb.as_markup())

@dp.message(Command("add_item"))
async def admin_add_item(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return
    # Формат: /add_item Название | Цена | Секретный_товар
    parts = msg.text.replace("/add_item", "").strip().split("|")
    if len(parts) < 3:
        await msg.answer("Использование: `/add_item Подписка Pro | 299 | КЛЮЧ-ИЛИ-ССЫЛКА`")
        return
    name, price, secret = parts[0].strip(), int(parts[1].strip()), parts[2].strip()
    conn = sqlite3.connect("shop.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, price, desc) VALUES (?, ?, ?)", (name, price, name))
    item_id = cur.lastrowid
    cur.execute("INSERT INTO stock (item_id, secret_data) VALUES (?, ?)", (item_id, secret))
    conn.commit()
    conn.close()
    await msg.answer(f"✅ Товар «{name}» ({price} ₽) добавлен в автовыдачу!")

async def main():
    init_db()
    print("Бот автопродаж запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())