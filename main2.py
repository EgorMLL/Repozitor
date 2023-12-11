def screaming_filter(text):
    return text.upper()

def bored_filter(text):
    return text.lower() and "...".join(text.split())

def smile_filter(text):
    return "🙂".join(text.split())

def warning_filter(text):
    result = ""
    for word in text.split():
        result += word + "!"
    return result

def camel_filter(text):
    result = ""
    is_next_upper = False
    for i in range(len(text)):
        if text[i] == " ":
            is_next_upper = True
        elif is_next_upper:
            result += text[i].upper()
            is_next_upper = False
        else:
            result += text[i]
    return result


def vowel_letters(text):
    text1 = []
    for i in range(len(text)):
        if text[i] == "о" or text[i] == "а" or text[i] == "у" or text[i] == "э" or text[i] == "ю" or text[i] == "я" or text[i] == "ы" or text[i] == "е" or text[i] == "ё" or text[i] == "и":
            text1.append(text[i])
    return text1

def word_2016_filter(text):
    return "-".join(text.split())


filters = {
    1: {"name": "КРИЧАЩИЙ ФИЛЬТР",
    "description": "Преобразует все буквы слов в верхний регистр",
    "function": screaming_filter
        },

    2: {"name": "уставший...фильтр...",
        "description": "Ставит троеточие в тексте место пробелов",
        "function": bored_filter
        },
    3: {"name": "Улыбающийся фильтр🙂",
        "description": "Ставит смайлик вместо пробелов",
        "function": smile_filter
        },
    4: {"name": "!ФИЛЬТР!ТРЕВОГИ!",
        "description": "Ставит восклицательные знаки в слова и возводит слова в верхний регистр, чтобы принять ощущение важности сообщения.",
        "function": warning_filter
        },
    5: {"name": "camel_",
        "description": "Преобразует текст в формат CamelCase",
        "function": camel_filter
        },
    6: {"name": "-word-2016-filter-",
        "description": "Ставит вместо пробелов тире, придавая формат текста как формат текста в word2016",
        "function": word_2016_filter
        },
    7: {"name": "только гласные буквы",
        "description": "Оставляет из текста только гласные буквы и выводит список этих букв",
        "function": vowel_letters
        }
    }


print("Выберите фильтр для редактора текста:")

for key, value in filters.items():
    print(key, value["name"])
print("0: Выход.")

filter_choice = None
while filter_choice not in filters:
    filter_choice = int(input("Введите номер фильтра или выйдите из программы:"))
    if filter_choice == 0:
        print("Выход из программы")
        exit()

filter_name = filters[filter_choice]["name"]
filter_description = filters[filter_choice]["description"]

print(f"Вы выбрали фильтр: {filter_name}")
print(f"Описание фильтра {filter_name}: {filter_description} \n"
      )

text = input("Введите текст для фильтрации:")
fil_text = filters[filter_choice]["function"](text)
print()
print(f"Отлично! предложение {text} будет отредактировано.\n"

            )
if fil_text:
    answer = input(f"Выбрать фильтр {filter_name} к текущему тексту? (Да или Нет) ")

    if answer.lower() == "да":
        fil_text = filters[filter_choice]["function"](fil_text)
        if fil_text:
            print(f"Отфильтрованный текст: {fil_text} ")

    if answer.lower() == "нет":
        print("Выход из программы.")
        print("Досвидания")
