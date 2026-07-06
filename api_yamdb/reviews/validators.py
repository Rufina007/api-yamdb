import re

from django.core.exceptions import ValidationError

USERNAME_REGEX = re.compile(r'^[\w.@+-]+\Z')


def validate_username(value):
    """Запрещает имя пользователя 'me' и символы вне [\\w.@+-]."""
    if value == 'me':
        raise ValidationError(
            'Использовать имя "me" в качестве username запрещено.'
        )
    if not USERNAME_REGEX.match(value):
        invalid_chars = ''.join(set(re.sub(r'[\w.@+-]', '', value)))
        raise ValidationError(
            f'Имя пользователя содержит запрещённые символы: {invalid_chars}'
        )
    return value
