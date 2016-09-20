from google import search
from os import system

song_name = raw_input('Enter song name: ')
result = search(song_name).next()
system('youtube-dl -f bestaudio ' + result)


