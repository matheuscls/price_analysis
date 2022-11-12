from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date, time, datetime, timedelta


class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.__get_html()

    def __get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def __get_rooms(self):
        return self.soup.find_all("div", class_="c4mnd7m dir dir-ltr")

    def __get_title(self, room):
        return room.find("div", class_="t1jojoys dir dir-ltr").text

    def __get_subtitle(self, room):
        return room.find("span", class_="t6mzqp7 dir dir-ltr").text

    def __get_price(self, room_html):
        return room_html.find("span", class_ = "_14y1gc").find("span", class_ = "a8jt5op dir dir-ltr").text[2:].split()[0]

    def __get_price_original(self, room_html):
        try:
            valor = room_html.find("span", class_ = "_14y1gc").find("span", class_ = "a8jt5op dir dir-ltr").text.split()[4][2:]
        except:
            valor = None
        return valor

    def __get_avaliacao(self, room):
        return room.find("span", class_="t5eq1io r4a59j5 dir dir-ltr").text

    def __get_href(self, room):
        href_room = str(room.find("a", class_="ln2bl2p dir dir-ltr"))
        return "https://www.airbnb.com.br/" + href_room.split()[5][7:-1]

    def get_session_id(self):
        session_id = str(self.soup.find("a", class_="_1bfat5l")).split()[3].split('"')[1].replace('amp;', '')
        return "https://www.airbnb.com.br" + session_id

    def pick_all_rooms(self):
        list_of_rooms = []

        for room in self.__get_rooms():

            room_info = {}

            room_info["Request Date"] = date.today()
            room_info["Title"] = self.__get_title(room)
            room_info["Subtitle"] = self.__get_subtitle(room)
            room_info["Actual_price"] = self.__get_price(room)
            room_info["Original_price"] = self.__get_price_original(room)
            #room_info["Score"] = self.__get_avaliacao(room)
            room_info["href"] = self.__get_href(room)

            list_of_rooms.append(room_info)
            # print(len(list_of_rooms))
        return list_of_rooms