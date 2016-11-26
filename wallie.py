import random


def get_wallie_action():
    possible_actions = [
        'считает новых пользователей',
        'готовит новую задачу',
        'что-то проверяет',
        'придумывает новую ачивку',
        'проверяет чью-то задачу',
        'проставляет ссылки в энциклопедии',
        'вычитывает статью',
        'ищет стажировки для студентов',
        ]
    return 'Валли ' + random.choice(possible_actions)


if __name__ == '__main__':
    action = get_wallie_action()
    print(action)
