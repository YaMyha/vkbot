import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Ваш токен доступа (вставьте сюда свой токен сообщества)
TOKEN = 'vk1.a.oI-bTJpKP_GH8hnDoHHxAFRrmKkyAudZlEni-zDbZnI4-NoCi_XTao2c4Dp9pn1sIPwTEzz6EjplWTiJPvAWSxxP0jU-qwoR7jcKcEFDtlwE0j06l1I5A3RsCqmXBY9dAHpPSZMMhQuHREiAlEdXgGMwm8AxlrBX8yHa5XKbvJHRJwuuaxePJEJmZOdWQ-X-ICvGB89Sd5PcSzRpMUCatQ'

# Авторизация через токен
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

# Создание объекта для получения событий
longpoll = VkLongPoll(vk_session)

# Функция для отправки сообщения
def send_message(user_id, message):
    vk.messages.send(user_id=user_id, message=message, random_id=0)

# Основной цикл для обработки сообщений
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Проверяем, что сообщение пришло в личные сообщения
        message_text = event.text.lower()

        if message_text == 'привет':
            send_message(event.user_id, 'Привет! Как дела?')
        elif message_text == 'как тебя зовут?':
            send_message(event.user_id, 'Меня зовут Бот!')

print("Бот запущен!")
