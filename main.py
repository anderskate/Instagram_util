import os
from instabot import Bot
from dotenv import load_dotenv
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_pictures

def publish_photos():
    bot = Bot()
    bot.login(username=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))

    images = os.listdir('images')[1:]
    for image in images:
        path_to_file = 'images/' + image 
        bot.upload_photo(path_to_file)

def main():
    load_dotenv()
    if not os.path.exists('images'):
        os.makedirs('images')

    fetch_spacex_last_launch('https://api.spacexdata.com/v3/launches/latest')
    fetch_hubble_pictures('http://hubblesite.org/api/v3/images?page=all&collection_name=printshop')
    publish_photos()

if __name__ == '__main__':
    main()


