import requests

class AuthToken(object):
    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url

    def __enter__(self):
        pass

    def get_token(self):
        try:
            body = '{"username": "%s", "password": "%s"}' %(self.username, self.password)
            response = requests.post(self.url, data=body)
            return response.text
        except:
            return ""

    def __exit__(self,  type, value, traceback):
        pass

if __name__ == "__main__":
    token = AuthToken("http://shawnswlin.com:5000/auth")
    print token.get_token()