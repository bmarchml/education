import random as r
answer = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

def hello():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.\nКак тебя зовут?')
    name = input()
    print(f'Привет {name}')

def magic():
    print('Задай мне вопрос')
    question = input()
    print(f'Мой ответ:\n{r.choice(answer)}')

def so_what():
    while True:
        print('У тебя есть ко мне еще вопросы?')
        text = input().lower()
        if text not in ('y','n','д','н', 'да', 'нет'):
            print('Я не понимаю тебя')
            text = input().lower()
        elif text in ('y','д'):
            print('Продолжим!')
            return True
        else:
            return False

def main():
    hello()
    while True:
        magic()
        if so_what():
            continue
        else:
            print('Знаю, ты вернешься, мы не прощаемся')
            break

main()
