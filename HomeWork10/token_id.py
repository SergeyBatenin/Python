

def token_id():
    with open("token", encoding="utf-8") as file:
        token_id = file.readline()
        return token_id

