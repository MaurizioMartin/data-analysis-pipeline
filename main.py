from api import getSongData,getSongId,getImg
from create_pdf import create_pdf
import figs
import mail
import argparse

def get_args(argv=None):

    parser = argparse.ArgumentParser(description="Song analysis")
    parser.add_argument("-s", "--song", type=str, help="Song you want to search")
    parser.add_argument("-m", "--mail", type=str, help="Mail will receive the analysis")
    return parser.parse_args(argv)

def start(song,email):
    song=song.title()
    print("Looking for the data of "+song+"!\n")
    song_data = getSongData(getSongId(song))
    song_name = song_data["song_name"]
    historic_df = figs.import_historic_data()
    song_df = figs.import_song_data()
    song_data_df = figs.getSongDataDf(song_df,song_name,song_data["artist_name"])
    dirName = figs.create_folder(song_name)
    getImg(song_data["img"],song_name,dirName)
    print("Creating graphs!\n")
    figs.create_graph(historic_df,song_name,"ES",dirName)
    figs.create_graph(historic_df,song_name,"GB",dirName)
    figs.create_graph(historic_df,song_name,"US",dirName)
    figs.create_graph(historic_df,song_name,"GLOBAL",dirName)
    print("Generating PDF!\n")
    create_pdf(song_name,song_data['description'],song_data['lyrics'],dirName,song_data_df)
    mail.sentmail(email,song_name,dirName)
    print("Check your mail! PDF attached!")


def main():
    args = get_args()
    if args.mail and args.song:
        song = args.song
        email = args.mail
        start(song,email)
    elif args.mail:
        email = args.mail
        song = input("Introduce el nombre de la canción: \n")
        start(song,email)
    elif args.song:
        song = args.song 
        email = input("Type the receiver mail:")
        start(song,email)


if __name__=='__main__':
    main()
