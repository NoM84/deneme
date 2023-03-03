import requests
import time
from datetime import datetime


def send_message(channel_id, token,mesaj):
    message = {'content': mesaj}
    headers = {'Authorization': token}
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=message, headers=headers)
    return r
def send_intreact(token,payload):
    message = payload
    header = {'Authorization': token}
    r = requests.post("https://discord.com/api/v9/interactions",json=payload,headers=header)
    return r


kanal_id ="1053726991309877269"

payload1 = {
        'type': 2,
        'application_id': '624187616312426512',
        'guild_id': '787718450206343218',
        'channel_id': kanal_id,
        'session_id': 'bcbaa31b6538beb56f5a08f304832a2e',
        'data': {
            'version': '1074395882000224347',
            'id': '1074395881547239477',
            'name': 'hunt',
        }
    }
msg= "Dene: "
token = input("Tokeni Giriniz: ")
times = int(input('Tekrarlanacak işlem sayisini giriniz: '))

b = 1
for i in range(times):
    response=send_intreact(token,payload1)
    time.sleep(15)
    response=send_intreact(token,payload1)
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print('Yapilan işlem sayisi: {}  Saat: {}'.format(b, current_time))
    b += 1
    time.sleep(615)
