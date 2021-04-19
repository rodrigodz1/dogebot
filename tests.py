import datetime
import time

now = datetime.datetime.now()
minute = ''
preco = '20.20'

while(True):
    print(preco.replace(".", ","))
    time.sleep(5)
