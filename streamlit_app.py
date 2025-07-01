import streamlit as st
import json
import os

# Список подарков с эмодзи
GIFTS = [
    "Фотосессия 📸",
    "Мастер-класс 🎨",
    "Прогулка на ладье 🚤",
    "Театр 🎭",
    "Экскурсия 🗺️",
    "Лекция 📖",
    "Чаепитие ☕",
]

# Путь к файлу для хранения выбранных подарков
DATA_FILE = "chosen_gifts.json"


# Функция для загрузки данных
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


# Функция для сохранения данных
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


# Инициализация session_state для управления попапом
if "show_popup" not in st.session_state:
    st.session_state.show_popup = False
if "selected_gift" not in st.session_state:
    st.session_state.selected_gift = None

# Загружаем текущие выбранные подарки
chosen_gifts = load_data()

# Основной интерфейс
st.title("Выбери свой подарок! 🎁")

# Фильтруем доступные подарки
available_gifts = [gift for gift in GIFTS if gift not in chosen_gifts]

if not available_gifts:
    st.warning("Все подарки уже выбраны! 😔")
else:
    # Выбор подарка
    selected_gift = st.selectbox("Выбери подарок:", available_gifts)

    if st.button("Подтвердить выбор"):
        # Сохраняем выбранный подарок
        chosen_gifts.append(selected_gift)
        save_data(chosen_gifts)
        # Показываем попап
        st.session_state.show_popup = True
        st.session_state.selected_gift = selected_gift

# Показываем попап, если он активен
if st.session_state.show_popup:
    st.markdown(
        f"""
        <div style='background-color: #e6f3ff; padding: 20px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #2c3e50;'>🎉 Поздравляем! 🎉</h3>
            <p style='font-size: 18px;'>Вы выбрали: <b>{st.session_state.selected_gift}</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Закрыть"):
        st.session_state.show_popup = False
        st.rerun()

# Показываем список уже выбранных подарков
if chosen_gifts:
    st.subheader("Уже выбраны:")
    for gift in chosen_gifts:
        st.write(f"- {gift}")
