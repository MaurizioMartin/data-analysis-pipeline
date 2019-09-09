from api import getSongData,getSongId,getImg
from create_pdf import create_pdf
import figs

if __name__=='__main__':
    #main()
    search = input("Introduce el nombre de la canción: \n")
    song_data = getSongData(getSongId(search))
    print(song_data['description'])
    historic_df = figs.import_historic_data()
    dirName = figs.create_folder(search)
    getImg(song_data["img"],search,dirName)
    figs.create_graph(historic_df,search,"ES",dirName)
    figs.create_graph(historic_df,search,"GB",dirName)
    figs.create_graph(historic_df,search,"US",dirName)
    figs.create_graph(historic_df,search,"GLOBAL",dirName)
    create_pdf(search,song_data['description'],song_data['lyrics'],dirName)