#coding:utf-8
import json
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_trades():
    re=requests.get('https://api.kraken.com/0/public/Trades?pair=XBTEUR')
    content=re.content
    history=json.loads(content)
    date=[]
    price=[]
    amount=[]
    for trade in history['result']['XXBTZEUR']:
        date.append(trade[2])
        price.append(float(trade[0]))
        amount.append(float(trade[0])*float(trade[1]))
    return date,price,amount

def main():
    date,price,amount =get_trades()
    print(len(price))
    plt.figure()
    plt.plot(date, price)
    plt.show()

if __name__ == '__main__':
  main()


