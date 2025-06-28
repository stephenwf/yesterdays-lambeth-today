import json
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import requests
import time

images = {}
headers = {
    'User-Agent': 'flaneurtom@gmail.com'
}


def is_jpg(folder, f):
    if isfile(join(folder, f)):
        if f.lower().endswith(".jpg"):
            return True
    return False

def is_five_digits(s):
    return len(s) == 5 and s.isdigit()


def parse_filename(file):
    bp_id = None
    is_archive = False
    dot_parts = file.split('.')
    if is_five_digits(dot_parts[0]):
        bp_id = dot_parts[0]
        is_archive = True
    else:
        sub_parts = dot_parts[0].split('_')
        if is_five_digits(sub_parts[0]):
            bp_id = sub_parts[0]

    return (bp_id, is_archive)


def scrape_borough_photos(img_data):    
    search_template = "https://boroughphotos.org/lambeth/search-results/?fRefNum=" + img_data["bp_id"]    
    r = requests.get(search_template, headers=headers)
    soup = BeautifulSoup(r.text)
    result = soup.css.select("#searchResultThumbContainer2 a")[0]
    print(result)
    img_data["borough_url"] = "https://boroughphotos.org" + result['href']
    img_data["name"] = result['title']
    print(img_data)
    time.sleep(3)


    


def process_folder(folder):
    files = [f for f in listdir(folder) if is_jpg(folder, f)]
    counter = 0
    for file in files:

        full_name = join(folder, file)
        print(f"looking at file {full_name}...")
        (bp_id, is_archive) = parse_filename(file)
        if bp_id is not None:
            counter = counter + 1
            img_data = images.get(bp_id, {
                "file": None,
                "bp_id": bp_id,
                "name": None,
                "borough_url": None,
                "now_image": None
            })
            if img_data.get("borough_url", None) is None:
                scrape_borough_photos(img_data)

            if is_archive:
                img_data["file"] = full_name
            else:
                img_data["now_image"] = full_name

            images[bp_id] = img_data
        
        else:
            print("not an archival item or derivative")




if __name__ == "__main__":    
    process_folder("C:\\Users\\TomCrane\\Dropbox\\personal\\Lambeth Archives\\220825_Exhibition Lambeth Archives 2208\\Exhibition Layouts 220825 Links")
    process_folder("C:\\Users\\TomCrane\\Dropbox\\personal\\Lambeth Archives\\220825_Exhibition Lambeth Archives 2208\\Exhibition Layouts 220823 Folder\\Links")
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(images, f, ensure_ascii=False, indent=4)

    with open("bp_links.csv", 'w', encoding="utf-8") as f:
        for i, (k, v) in enumerate(images.items()):
            f.write(f'"{k}"')
            f.write(',')
            f.write(f'"{v["file"]}"')
            f.write(',')
            f.write(f'"{v["name"]}"')
            f.write(',')
            f.write(f'"{v["borough_url"]}"')
            f.write(',')
            f.write(f'"{v["now_image"]}"')
            f.write('\n')
        

