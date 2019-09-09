import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import urllib.request
load_dotenv()

clientid = os.getenv("CLIENT_ID")
accesstoken = os.getenv("CLIENT_ACCESS_TOKEN")

def authRequestJson(url, params={}):
    headers = {
         
       "Authorization": "Bearer {}".format(accesstoken)
    }
    response = requests.get(url,headers=headers, params=params)
    if response.status_code == 404:
        return None
    #print(response.status_code)
    #print(response.headers)
    return response.json()

def authRequestText(url, params={}):
    headers = {
         
       "Authorization": "Bearer {}".format(accesstoken)
    }
    response = requests.get(url,headers=headers, params=params)
    if response.status_code == 404:
        return None
    #print(response.status_code)
    #print(response.headers)
    return response.text

def getSongId(search):
    params = {'q': search}

    url = "https://genius.com/api/search/multi?" + urlencode(params)
    response = requests.get(url)
    response = response.json()['response']
    hits = response['sections'][0]['hits']
    if hits:
        tophit = hits[0]
        if tophit['type'] == "song":
            resultado = (tophit['result'])
    return resultado['id']

def getChildren(dic):
    if type(dic) is dict:
        if 'children' in dic:
            return dic['children']
        else:
            return ""
    else:
        return dic

def getDescription(song):
    string=[]
    for des in filter(None, song):
        for descr in des['children']:
            for des in getChildren(descr):
                if type(des) is dict:
                    string.append("")
                else:
                    string.append(des)
    return "".join(string)

def getSongData(id):
    data = authRequestJson("https://api.genius.com/songs/{}".format(id))
    data = data['response']['song']
    song_description = getDescription(data['description']['dom']['children'])
    song_img = data['header_image_url']
    song_url = data['url']
    song_album = data['album']
    song_artist_id = data['album']['artist']['id']
    song_dict={
        "song_id":id,
        "lyrics":getSongLyrics(song_url),
        "description":song_description,
        "img":song_img,
        "url":song_url,
        "album":song_album,
        "artist_id":song_artist_id
    }
    return song_dict

def getSongLyrics(song_url):
    page = authRequestText(song_url)
    html = BeautifulSoup(page, "html.parser")
    div = html.find("div", class_="lyrics")
    if not div:
        return None
    lyrics = div.get_text()
    return lyrics.strip("\n")

def getImg(url,song,dirName):
    img_data = requests.get(url).content
    with open(dirName+'/'+song+'_img.jpg', 'wb') as handler:
        handler.write(img_data)



