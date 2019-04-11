import requests

def fetch_spacex_last_launch(url):
    response = requests.get(url)
    image_links = response.json()['links']['flickr_images']

    for image_number, image_link in enumerate(image_links):
        image_name = 'spacex{}.jpg'.format(image_number)
        download_picture(image_link, image_name)

def download_picture(url, name):
    path_and_filename = 'images/' + name
    response = requests.get(url)

    with open(path_and_filename, 'wb') as file:
        file.write(response.content)
