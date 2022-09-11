import requests
import pandas as pd
import telebot
from datetime import date
from telebot import types
url = 'http://numbersapi.com'
class API:
    def __init__(self,url):
        self.url=url
    def number(self,number):
        url_1=[self.url,str(number)]
        url_str=str('/'.join(url_1))
        resp = requests.get(url_str)
        return(resp.text)
    def event(self,date_str):
        month=date_str[3:]
        day=date_str[:2]
        url_2 = [self.url,str(month),str(day)]
        url_str="/".join(url_2)
        resp = requests.get(url_str)   
        return (resp.text)
    def year(self,year):
        url_3 = [self.url,str(year),'year']
        url_str="/".join(url_3)
        resp = requests.get(url_str)
        return (resp.text)

bot = telebot.TeleBot('5663397350:AAHZPEJnvj6Ik0j3Y16DMvJK8ByowIn8rbI')
    
@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, 'Привет. Введите данные:\nДля получения события по дате, введите дату в формате \n"дд.мм".\nДля получения события по году, введите год в формате \n"!гггг"\nДля получения интересного факта о числе, введите число в формате \n"?число"')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text[2] == ".":
      f=API(url)
      answer=f.event(message.text)
      bot.send_message(message.from_user.id, answer)
  elif message.text[0] == "!":
      f=API(url)
      answer=f.year(message.text[1:])
      bot.send_message(message.from_user.id, answer)
  elif message.text[0] == "?":
      f=API(url)
      answer=f.number(message.text[1:])
      bot.send_message(message.from_user.id, answer)
  else:
      bot.send_message(message.from_user.id, "Я не понимаю. Напиши '/start'.")
  bot.polling(none_stop=True, interval=0)
