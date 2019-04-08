import requests
import os
from instabot import Bot
from dotenv import load_dotenv

def get_response(url):
    response = requests.get(url)
    return response

def download_picture(url, name):
    path_and_filename = 'images/' + name
    response = get_response(url)

    with open(path_and_filename, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch(url):
    response = get_response(url)
    image_links = response.json()['links']['flickr_images']

    for image_number, image_link in enumerate(image_links):
        image_name = 'spacex' + str(image_number) + '.jpg'
        download_picture(image_link, image_name)

def get_extension_picture(link):
    chunks_links = link.split('.')
    return chunks_links[-1]

def fetch_hubble_pictures(url):

    response = get_response(url)
    collection_picture_information = response.json()
    ids_pictures = [picture_info['id'] for picture_info in collection_picture_information]

    for id_picture in ids_pictures:
        url = 'http://hubblesite.org/api/v3/image/{}'.format(str(id_picture))
        response = requests.get(url)
        images_data = response.json()['image_files']

        picture_links = [link['file_url'] for link in images_data]

        extension_image = get_extension_picture(picture_links[-1])

        image_name = str(id_picture) + '.' + extension_image
        download_picture(picture_links[-1], image_name)

        print('Картинка ' + image_name + ' успешно скачана!')

def main():
    load_dotenv()
    if not os.path.exists('images'):
        os.makedirs('images')

    fetch_spacex_last_launch('https://api.spacexdata.com/v3/launches/latest')
    fetch_hubble_pictures('http://hubblesite.org/api/v3/images?page=all&collection_name=printshop')

    bot = Bot()
    bot.login(username=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))

    images = os.listdir('images')[1:]
    for image in images:
        path_to_file = 'images/' + image 
        bot.upload_photo(path_to_file)

if __name__ == '__main__':
    main()


