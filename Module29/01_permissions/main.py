from collections.abc import Callable
import functools


def check_permission(name: str = 'user') -> Callable:
    """ Декоратор проверки прав доступа"""

    def decorator_func(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper_check(*args, **kwargs):
            try:
                # TODO, пожалуйста, обратите внимание, ловить исключения в этом задании не нужно.
                #  Только вызвать. Код должен завершиться ошибкой, если пользователя нет в списке user_permissions.

                # TODO, нам необходимо проверить наличие name в локальной переменной user_permissions.
                if name == 'admin':
                    return func(*args, **kwargs)
                raise PermissionError('PermissionError')
            except PermissionError as exc:
                print(f'{exc}: У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapper_check
    return decorator_func


user_permissions = ['admin']


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
