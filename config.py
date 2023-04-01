def get_api_key():
    key = ''
    with open('api-key.txt', 'r') as file:
        key = file.readline().strip()
    return key