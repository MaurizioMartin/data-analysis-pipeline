# Music analysis pipeline

This is a pipeline made with Python that take 2 arguments from the User. '-s' or '--song' followed by the name of the song the user wants to search and '-m' or '--mail' to set the mail where the user wants to receive the PDF.

For example:

$ python main.py -s "la bicicleta" -m user@mail.com

The program will check in the API of Genius if it exists and will take the principal data of the song and artist. After that, the program checks in 2 datasets taked from Kaggle (One with 19000 songs and another with the top 200 in 53 countries for 2 years) more data so we can make graphs and make a further analysis. 

With all the information, the program generates a PDF that will save in the computer and also send to the mail that the user introduced.

It contains the photo of the song, a description, a table with the principal data, the graphs and the lyrics.

# Links & Resources

- https://docs.genius.com/
- https://www.kaggle.com/edumucelli/spotifys-worldwide-daily-song-ranking
- https://www.kaggle.com/edalrami/19000-spotify-songs#