import requests


class BoardApi:
    def __init__(self, base_url: str, api_token: str, api_key: str):
        self.base_url = base_url
        self.api_token = api_token
        self.api_key = api_key

    def get_all_boards_by_org_id(self, org_id: str) -> list:
        parameters = {
            'key': self.api_key,
            'token': self.api_token
        }
        path = ("{trello}/organizations/{id}/boards?key={key}&token={token}"
                .format(trello=self.base_url, id=org_id, key=self.api_key,
                        token=self.api_token))
        print(path)

        resp = requests.get(path, params=parameters)
        return resp.json()

    def create_board(self, name, default_lists=True) -> dict:
        body = {
            'defaultLists': default_lists,
            'name': name,
            'token': self.api_token
        }
        parameters = {
            'key': self.api_key,
            'token': self.api_token
        }
        path = ("{trello}/boards/?name={name}&key={key}&token={token}"
                .format(trello=self.base_url, name=name,
                        key=self.api_key, token=self.api_token))
        requests.post(path, json=body, params=parameters)

    def delete_board_by_id(self, id: str):
        parameters = {
            'key': self.api_key,
            'token': self.api_token
        }
        path = ("{trello}/boards/{board_id}?key={key}&token={token}"
                .format(trello=self.base_url, board_id=id,
                        key=self.api_key, token=self.api_token))
        requests.delete(path, params=parameters)
