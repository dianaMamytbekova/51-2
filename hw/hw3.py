import emoji
import random

# emoji — это библиотека для работы с эмодзи.
# С её помощью можно добавлять эмодзи в строки Python.

# список эмодзи
emoji_list = [
    ":grinning_face:", ":winking_face:", ":smiling_face_with_sunglasses:",
    ":thinking_face:", ":face_with_tears_of_joy:", ":star_struck:",
    ":party_popper:", ":rocket:", ":fire:", ":thumbs_up:"
]

# случайный эмодзи
random_emoji = random.choice(emoji_list)

# сообщение с эмодзи
message = emoji.emojize(f"Твой случайный эмодзи дня: {random_emoji}")

# результат
print(message)
