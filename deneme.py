import requests
import time
from datetime import datetime


def send_message(channel_id, token,mesaj):
    message = {'content': mesaj}
    headers = {'Authorization': token}
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=message, headers=headers)
    return r

islem ='0'
kanal_id ="1081187817562062959"
if islem == '0':
    payload1 = {
        'type': 2,
        'application_id': '624187616312426512',
        'guild_id': '787718450206343218',
        'channel_id': kanal_id,
        'session_id': '14351d4f4e9897f76ddb2b2a0df20245',
        'data': {
            'version': '1042350843300679691',
            'id': '1042350843103547441',
            'name': 'hunt',
        }
    }
msg= "Dene: "
token = "NzE4NDk3Mjg4OTYzNjIwOTA0.GYIOsV.3XmgtlXhDpBBTqzNUvvh9Ydxl4gVv-PwNTaUcI"
times = int(input('Tekrarlanacak işlem sayısını giriniz: '))

b = 1
for i in range(times):
    response = send_message(kanal_id, token,(msg + f'{i}'))
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print('Yapılan işlem sayısı: {}  Saat: {}'.format(b, current_time))
    b += 1
    time.sleep(30)
