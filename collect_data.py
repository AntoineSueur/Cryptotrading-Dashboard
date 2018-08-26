# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:44:57 2018

@author: antoi
"""
import poloniex
polo = poloniex.Poloniex()
import time
from datetime import datetime
import os 
import shutil



available_currencies = ['ETH','LTC','XRP','DASH','XMR','BTC','BCH']
altcoins = ['ETH','LTC','XRP','DASH','XMR','XEM']
possible_pairs = list(polo.returnOrderBook().keys())
currencies  = list(polo.returnCurrencies().keys())

def get_price(pair):
    if(pair in possible_pairs):
        return float(polo.returnTicker()[pair]['last'])
    else:
        try:
            buy, sell = pair.split("_")
            return float(polo.returnTicker()[sell+"_"+buy]['last'])
        except:
            #print("error")
            return 0

if not os.path.exists('./data'):
    os.makedirs('./data')
timestep = 5
i = 0    
while(1):
    i+=1
    for c in available_currencies:
        if c+'.csv' not in os.listdir('data'):
            with open('./data/'+c+'.csv','w')as f:
                f.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+","+str(get_price(c+'_USDT'))+"\n")
        else:
            with open('./data/'+c+'.csv','a')as f:
                f.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+", "+str(get_price(c+'_USDT'))+"\n")
        if(i%60==0):
            try:
                shutil.copyfile('./data/'+c+'.csv', './data/'+c+'_copy.csv')
            except:
                pass
    time.sleep(timestep)