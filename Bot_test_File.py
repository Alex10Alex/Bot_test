import vk_api
import time


vk = vk_api.VkApi(token = "3676fce2670eb9d72e058bce5821182a6762821f3e06b6acf178d9d4b380b54dce30b72ab180a2c421157")
vk._auth_token()

values = {'out':0, 'count':100, 'time_offset':60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id, 'messages':s})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        write_msg(item['user_id'], 'Привет, человек')
    time.sleep(1)

