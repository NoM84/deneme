import requests
import json
import time
kanalid="1085534102813425694"
gonderilecekid="1082633377095614534"

def send_message(channel_id, token,mesaj):
    message = {'content': mesaj}
    headers = {'Authorization': token}
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=message, headers=headers)
    return r
def RetrieveMessage(Kanalid,Token):
    header={
    'Authorization': Token
    }
    r=requests.get(f'https://discord.com/api/v9/channels/{Kanalid}/messages',headers=header)
    jsonn=json.loads(r.text)
    for deger in jsonn:
        return deger['content']

def silme_komutu_yolla(Kanalid, token):
    message = {'content': "!sil"}
    headers = {'Authorization': token}
    r = requests.post(f'https://discord.com/api/v9/channels/{Kanalid}/messages', data=message, headers=headers)
    return r 
def send_backpackcommand(token,kanalid):
    CantaPayloadi = {
        'type': 2,
        'application_id': '624187616312426512',
        'guild_id': '787718450206343218',
        'channel_id': kanalid,
        'session_id': '55803ce04f439a79ade1ce794019be30',
        'data': {
            'version': '1081513164467863552',
            'id': '1081513164115542128',
            'name': 'inventory',
        }
    }
    message = CantaPayloadi
    header = {
        'Authorization': token}
    r = requests.post("https://discord.com/api/v9/interactions",
                      json=CantaPayloadi, headers=header)
    return r

def send_charactercommand(token,kanalid):
    karakterpayload = {
        'type': 2,
        'application_id': '624187616312426512',
        'guild_id': '787718450206343218',
        'channel_id': kanalid,
        'session_id': '8e3f574cd0853a86f2a88f07b697b114',
        'data': {
            'version': '1081513164425932862',
            'id': '1081513163851313212',
            'name': 'character',
            'type': 1,
            'options':[{
                'type': 3,
                'name': 'secenek',
                'value': 'goruntule',
            }]
        }
         
    }
    message = karakterpayload
    header = {
        'Authorization':token}
    r = requests.post("https://discord.com/api/v9/interactions",
                      json=karakterpayload, headers=header)
    return r

def send_characterstatuscommand(token,kanalid):
    karakterpayload = {
        'type': 2,
        'application_id': '624187616312426512',
        'guild_id': '787718450206343218',
        'channel_id': kanalid,
        'session_id': '8e3f574cd0853a86f2a88f07b697b114',
        'data': {
            'version': '1081513164425932862',
            'id': '1081513163851313212',
            'name': 'character',
            'type': 1,
            'options':[{
                'type': 3,
                'name': 'secenek',
                'value': 'stats',
            }]
        }
         
    }
    message = karakterpayload
    header = {
        'Authorization':token}
    r = requests.post("https://discord.com/api/v9/interactions",
                      json=karakterpayload, headers=header)
    return r

Token1=input("1.Tokeni Giriniz:")
Token2=input("2.Tokeni Giriniz:")
Token3=input("3.Tokeni Giriniz:")
Token4=input("4.Tokeni Giriniz:")

while True:
    komut=RetrieveMessage(kanalid,Token1)
    time.sleep(1)
    if(komut==None):
        continue
    if(("çanta"in komut)and ("1" in komut)):
        send_backpackcommand(Token1,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token1,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token1)
        continue
    if(("çanta"in komut)and ("2" in komut)):
        send_backpackcommand(Token2,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token2,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token2)
        continue
    if(("çanta"in komut)and ("3" in komut)):
        send_backpackcommand(Token3,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token3,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token3)
        continue
    if(("çanta"in komut)and ("4" in komut)):
        send_backpackcommand(Token4,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token4,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token4)
        continue
    if(("karakter"in komut)and ("1" in komut)):
        send_charactercommand(Token1,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token1,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token1)
        continue
    if(("karakter"in komut)and ("2" in komut)):
        send_charactercommand(Token2,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token2,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token2)
        continue
    if(("karakter"in komut)and ("3" in komut)):
        send_charactercommand(Token3,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token3,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token3)
        continue
    if(("karakter"in komut)and ("4" in komut)):
        send_charactercommand(Token4,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token4,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token4)
        continue
    if(("statü"in komut)and ("1" in komut)):
        send_characterstatuscommand(Token1,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token1,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token1)
        continue
    if(("statü"in komut)and ("2" in komut)):
        send_characterstatuscommand(Token2,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token2,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token2)
        continue
    if(("statü"in komut)and ("3" in komut)):
        send_characterstatuscommand(Token3,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token3,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token3)
        continue
    if(("statü"in komut)and ("4" in komut)):
        send_characterstatuscommand(Token4,gonderilecekid)
        print("Komut Kullanıldı")
        send_message(kanalid,Token4,"Komut Gönderildi!")
        time.sleep(2)
        silme_komutu_yolla(kanalid,Token4)
        continue
        

