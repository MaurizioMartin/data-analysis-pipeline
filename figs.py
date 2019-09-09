import pandas as pd
import os
from datetime import date
import matplotlib.pyplot as plt
import sys

def import_historic_data():
    return pd.read_csv("output/cleaned_historic_data.csv")
    
def import_song_data():
    return pd.read_csv("output/cleaned_song_data.csv")

def create_folder(song):
    song = song.replace(" ","_")
    fileName = date.today().strftime("%d_%m_%Y_"+song+"_analysis")
    dirName='analysis/'+fileName
    try:
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
        return dirName
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
        return dirName

def create_graph(df,song,region,dirName):
    try:
        name=region+"_graph.png"
        df = df[(df.song_name==song) & (df.region==region)]
        df.plot(x="date",y="position")
        plt.ylim(100,0)
        plt.xticks(rotation=45)
        plt.savefig(dirName+"/"+name, dpi=300)
    except TypeError as te:
        print(te)

def getSongDataDf(df,song,artist_name):
    try:
        filtereddf = df[(df.song_name==song) & (df.artist_name==artist_name)]
        if filtereddf.empty:
            print("Sorry, we don't have data of that song. Try with another one.\n")
            print(artist_name)
            filtereddf = df[df.artist_name==artist_name]
            if filtereddf.empty:
                sys.exit()
            else:
                print(filtereddf)
                sys.exit()
        return filtereddf.to_dict()
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)