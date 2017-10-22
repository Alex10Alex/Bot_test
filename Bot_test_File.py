import vk_api
import time


vk = vk_api.VkApi(token = "3676fce2670eb9d72e058bce5821182a6762821f3e06b6acf178d9d4b380b54dce30b72ab180a2c421157")
vk.auth()

values = {'out':0, 'count':100, 'time_offset':60}
vk.method('messages.get', values)

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id, 'messages':s})
