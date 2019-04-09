import requests
from fetch_spacex import download_picture

def fetch_hubble_pictures(url):
    response = requests.get(url)
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

def get_extension_picture(link):
    chunks_links = link.split('.')
    return chunks_links[-1]

