from api import getSongData,getSongId
from create_pdf import create_pdf

if __name__=='__main__':
    #main()
    search = input("Introduce el nombre de la canción: \n")
    song_data = getSongData(getSongId(search))
    print(song_data['description'])
    create_pdf(song_data['description'],"img",song_data['lyrics'],"data")