import json

import requests


class DashaMail:
    BASE_URL = "https://api.dashamail.com/?"

    def __init__(self, api_key) -> None:
        self.API_KEY = api_key

    def _post(self, url):
        r = requests.post(
            url=DashaMail.BASE_URL + url + f'&api_key={self.API_KEY}'
        ).text
        return r

    def clear_old_list(self, emails: list, base_id: str) -> None:  # убираем из базы тех, кого больше нет в эксельке
        members = requests.post(
            url=DashaMail.BASE_URL + f'method=lists.get_members&list_id={base_id}&api_key={self.API_KEY}'
        ).text
        members = json.loads(members)

        for mem in members['response']['data']:
            mem_id = mem['id']
            if mem['email'] not in emails:
                requests.post(
                    url=DashaMail.BASE_URL + f'method=lists.delete_member&member_id={mem_id}&api_key={self.API_KEY}'
                )  # удаляем почту мембера по id

    def update_mailing_list(self, base_id: str, emails: list):
        self.clear_old_list(emails, base_id)
        emails = json.dumps([{"email": e} for e in emails])
        # добавляем всех тех, кто в эксельке (без повторений)
        response = self._post(f"method=lists.add_member_batch&list_id={base_id}&batch={emails}")
        return response
