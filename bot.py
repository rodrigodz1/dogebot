import tweepy
import requests
import json
import datetime
import time


# Authenticate to Twitter
auth = tweepy.OAuthHandler("olJVFia9WcU8QhUiR6HVON8kB",
                           "rwGUC5BxLne9katX2cDLD8oP1DWwnxXuMwYNkeC7xL772ez3Fo")
auth.set_access_token("1383822673520648203-viR24xiHx9TS2yxkE3ME1D0BovXNvQ",
                      "3EH3MGqDoKFiqjD9E27qFtFPGEWkFhkwd5BKoziEeVWLr")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#post = api.update_status("Test tweet from Tweepy Python")

r = requests.get("https://api.coingecko.com/api/v3/coins/dogecoin")
r = r.json()
valor_em_reais = 0
market_cap_rank = r['market_cap_rank']


string1 = "To the moon! 🚀 - DogeCoin agora vale R$"

print("Postando em 1 min.")
time.sleep(60)

minute = ''
hour = ''
horario = ''

while(True):
    now = datetime.datetime.now()
    if (now.minute < 10):
        minute = f"0{now.minute}"
    else:
        minute = f"{now.minute}"

    if (now.hour < 10):
        hour = f"0{now.hour}"
    else:
        hour = f"{now.hour}"

    horario = f"{hour}:{minute}"

    oldvalue = valor_em_reais

    if valor_em_reais == 0:
        string1 = "DogeCoin agora vale R$"
        valor_em_reais = r['market_data']['current_price']['brl']
    elif (r['market_data']['current_price']['brl'] < valor_em_reais):
        string1 = "Caiu! :( - DogeCoin agora vale R$"
        valor_em_reais = r['market_data']['current_price']['brl']
    elif (r['market_data']['current_price']['brl'] > valor_em_reais):
        string1 = "To the moon! 🚀 - DogeCoin agora vale R$"
        valor_em_reais = r['market_data']['current_price']['brl']

    if oldvalue == valor_em_reais:
        print(
            "Valor igual o anterior. Não é necessário postar nada. Valor:", valor_em_reais)
    else:
        api.update_status(
            f"{string1} {valor_em_reais} as {horario}")
        print("Tweet criado! Daqui a 15 minutos nova atualização")

    r = requests.get("https://api.coingecko.com/api/v3/coins/dogecoin")
    r = r.json()

    time.sleep(900)
