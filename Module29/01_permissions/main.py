from collections.abc import Callable
import functools

user_permissions = ['admin']


def check_permission(name: str = 'user') -> Callable:
    """ Декоратор проверки прав доступа"""

    def decorator_func(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper_check(*args, **kwargs):
            if name in user_permissions:
                return func(*args, **kwargs)
            raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию add_comment')

        return wrapper_check

    return decorator_func


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

# Результат:
# Удаляем сайт
# PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment

# зачёт!
