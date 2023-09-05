"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""
import datetime

questions_and_answers = {
    'привет': 'Привет!',
    'как дела': 'Хорошо!',
    'что делаешь': 'Ничего.',
    'пока': 'Пока!',
}

def ask_user(questions_and_answers):
    characters_to_remove = '!?.,'

    while True:
        question = input('Вопрос: ')
        question_handled = ''

        for i in question.strip().lower():
            if i not in characters_to_remove:
                question_handled += i

        if question_handled == 'пока':
            print(f'Ответ: {questions_and_answers[question_handled]}')
            break

        print(f'Ответ: {questions_and_answers[question_handled]}')


if __name__ == "__main__":
    ask_user(questions_and_answers)
