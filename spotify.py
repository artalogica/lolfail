# import libraries  
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

# authenticate and connect to the API
client_id = '36eee480d1984cb3afe2d01618259f5b'
client_secret = '2b0e1b6ae66b437288177dbfca55eb88'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# get track ids from playlist
def getPlaylistTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return id

# get song info and audio analysis from song ids
def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # Meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # Features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track  

getPlaylistTrackIDs('ds3q0l2busvilwzpoadvduycn', '3O7drMonef8H38UXN4mHTZ')

# loop over track ids to create dataset
tracks = []
for i in range(0, len(ids)):
    time.sleep(.5)
    track = getTrackFeatures(ids[i])
    tracks.append(track)

df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("D:\code sh\orange", sep = ',')