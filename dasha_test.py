from dasha import DashaMail

import pytest
import requests

API = '463db793503a3a3cd42b7c48611d0e61'
ID = 208436
dasha = DashaMail(API, ID)


def check(mail: str, r: str) -> bool:
    return mail in r


@pytest.mark.parametrize(
    ('mails', 'deleted_mails'),
    [
        (
                ['test_one_more_time2@mail.ru', 'test_again@gmail.com'],
                ['some_test@gmail.com', 'qwerty505@mail.ru']
        ),
        (
            ['qwerty505@mail.ru'],
            ['test_one_more_time2@mail.ru', 'test_again@gmail.com']
        )
    ]
)
def test(mails, deleted_mails):
    dasha.update_mailing_list(mails)
    url = dasha.BASE_URL + f'api_key={API}&method=lists.get_members&list_id={ID}'
    r = requests.post(url=url).text  # получаем всех мемберов из базы

    for mail in mails:
        assert check(mail, r) is True
    for mail in deleted_mails:
        assert check(mail, r) is False
