
import requests
import wget
from bs4 import BeautifulSoup

# Получаем URL и число аудиофайлов для скачивания
url = input("Введите URL: ")
b = int(input("Введите количество аудиофайлов для скачивания: "))

# Функция для скачивания всех аудио ссылок
def download_audio(links):
    for i, link in enumerate(links):
        filename = f"{i+1}.mp3"
        wget.download(link, out=filename)
        print(f"{filename} загружен")

# Отправляем запрос к веб-странице
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Поиск всех ссылок на скачивание аудиофайлов
audio_links = []
items = soup.find_all('div', class_='download')
for item in items:
    links = item.find_all_next('a')
    for link in links:
        if 'mp3' in link.get('href', ''):
            audio_links.append(link['href'])

# Ограничение списка до требуемого количества аудиофайлов
audio_links = audio_links[:b]

# Скачивание аудиофайлов
download_audio(audio_links)
