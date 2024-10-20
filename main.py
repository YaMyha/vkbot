import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
import os
from flask import Flask

# Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv('API_KEY')
PORT = int(os.getenv('PORT', 5000))  # Используем порт из переменной окружения или 5000 по умолчанию

# Инициализация Flask приложения
app = Flask(__name__)

# Авторизация через токен ВКонтакте
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

# Создание объекта для получения событий Long Poll
longpoll = VkLongPoll(vk_session)


# Функция для отправки сообщения
def send_message(user_id, message):
    vk.messages.send(user_id=user_id, message=message, random_id=0)


# Обработчик для корневого маршрута
@app.route('/')
def index():
    return 'VK Bot is running!'


# Функция для прослушивания сообщений от ВКонтакте через Long Poll
@app.route('/listen')
def listen():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            # Проверяем, что сообщение пришло в личные сообщения
            message_text = event.text.lower()

            if message_text == 'привет':
                send_message(event.user_id, 'Привет! Как дела?')
            elif message_text == 'как тебя зовут?':
                send_message(event.user_id, 'Меня зовут Бот!')

    return "Listening to VK Long Poll events."

