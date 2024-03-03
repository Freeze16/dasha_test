import json

import requests


class DashaMail:
    BASE_URL = "https://api.dashamail.com/?"

    def __init__(self, api_key, base_id) -> None:
        self.API_KEY = api_key
        self.BASE_ID = base_id  # id адресной базы

    def _post(self, url):
        r = requests.post(
            url=DashaMail.BASE_URL + url + f'&api_key={self.API_KEY}'
        ).text
        return r

    def clear_old_list(self, emails: list) -> None:  # убираем из базы тех, кого больше нет в эксельке
        members = requests.post(
            url=DashaMail.BASE_URL + f'method=lists.get_members&list_id={self.BASE_ID}&api_key={self.API_KEY}'
        ).text
        members = json.loads(members)

        for mem in members['response']['data']:
            mem_id = mem['id']
            if mem['email'] not in emails:
                requests.post(
                    url=DashaMail.BASE_URL + f'method=lists.delete_member&member_id={mem_id}&api_key={self.API_KEY}'
                )  # удаляем почту мембера по id

    # Параметр mailing_list, как я понял, здесь заменяется на id адресной базы (закинул в __init__)
    def update_mailing_list(self, emails: list):
        self.clear_old_list(emails)
        emails = json.dumps([{"email": e} for e in emails])
        # добавляем всех тех, кто в эксельке (без повторений)
        response = self._post(f"method=lists.add_member_batch&list_id={self.BASE_ID}&batch={emails}")
        return response


a = DashaMail('463db793503a3a3cd42b7c48611d0e61', 208436)
print(a.update_mailing_list(['qwerty505@mail.ru']))
