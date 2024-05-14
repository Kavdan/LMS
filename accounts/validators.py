import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r"^[a-zA-Zа-яА-Я]+\/(...)\/(....)"
    message = _(
        "Имя пользователя не прошло валидацию. Только русские и английские буквы, "
        "числа, и символы @/./+/-/_"
    )
    flags = re.ASCII
