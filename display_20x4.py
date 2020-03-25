#!/usr/bin/python

from bs4 import BeautifulSoup
from module.i2c import *
import requests
import time
import math
import csv
import sys


# Insert your URL here
url_c = "https://corona.help/country/switzerland"
# Insert your Population here
population_c = "8570000"
cc = "CH"
population_w = "7770173166"
url_w ="https://corona.help/"
Waiting = '15.0'





while True:
    from module.corona import *
    lcd_init()
    time.sleep(1)
    lcd_string((first),LCD_LINE_1)
    lcd_string(("Infected ")+(infections_c)+(" +")+(today_c),LCD_LINE_2)
    lcd_string("Worldwide",LCD_LINE_3)
    lcd_string(("Infected")+(infections_w)+(" +")+(today_w),LCD_LINE_4)
    
    time.sleep(10)
    
    lcd_init()
    time.sleep(1)
    lcd_string((first),LCD_LINE_1)
    lcd_string((deaths_c)+(" Deaths"),LCD_LINE_2)
    lcd_string("Worldwide",LCD_LINE_3)
    lcd_string((deaths_w)+(" Deaths"),LCD_LINE_4)
    
    time.sleep(10)
    
    lcd_init()
    time.sleep(1)
    lcd_string(("Recoverd ")+(first),LCD_LINE_1)
    lcd_string((survived_c),LCD_LINE_2)
    lcd_string("Recoverd Worldwide",LCD_LINE_3)
    lcd_string(survived_w,LCD_LINE_4)
    
    time.sleep(10)
    

            
        