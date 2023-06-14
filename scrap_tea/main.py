import requests
import lxml
import random
import json
from bs4 import BeautifulSoup
import csv
from time import sleep
from pprint import pprint


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}
count=0
iteration_count=29
for i in range(29):
    sleep(15)
    url=f'https://i-tea.ru/chaj/?page={i}'

    req=requests.get(url, headers=headers)
    src=req.text
    #print(src)
    with open("index.html2", "w") as file:
        file.write(src)
    with open("index.html2") as file:
        src=file.read()
    soup=BeautifulSoup(src, "lxml")
    data=soup.find_all("div", class_="caption")
    #print(data)
    all_tea_data_dict={}
    for i in data:
        tea_name=i.find("h4").find("a").text#имя товара
        tea_price=i.find("p",class_="price").text.replace('\t', '')#цена товара
        tea_href=i.find("a").get("href") #ссылка на товар
        all_tea_data_dict[tea_name]={tea_href:tea_price}
    #pprint(all_tea_data_dict)

    with open("all_tea_data_dict.json", "w", encoding="utf-8") as file:
         json.dump(all_tea_data_dict, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"# Итерация {count}. {tea_name} записан...")
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print("Работа завершена")
        break

    print(f"Осталось итераций: {iteration_count}")