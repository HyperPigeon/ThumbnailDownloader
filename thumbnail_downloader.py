import typer
import os
import requests
from pytube import Playlist

app = typer.Typer()

@app.command()
def download(video_id, resolution='maxresdefault', directory = 'thumbnails'):
	image_url = 'http://img.youtube.com/vi/{}/{}.jpg'.format(video_id,resolution)
	thumbnail_request = requests.get(image_url)

	if os.path.isdir(directory):
		with open("{}/{}.jpg".format(directory,video_id), 'wb') as f:
			f.write(thumbnail_request.content)
	else:
		os.mkdir(directory)
		with open("{}/{}.jpg".format(directory,video_id), 'wb') as f:
			f.write(thumbnail_request.content)
		
@app.command()
def downloadPlaylist(playlist_id, resolution='maxresdefault', directory = 'playlist_thumbnails'):
	p = Playlist('https://www.youtube.com/playlist?list={}'.format(playlist_id))
	for url in p:
		video_id = url.split('?v=')[1]
		image_url = 'http://img.youtube.com/vi/{}/{}.jpg'.format(video_id,resolution)
		thumbnail_request = requests.get(image_url)

		if os.path.isdir(directory):
			with open("{}/{}.jpg".format(directory,video_id), 'wb') as f:
				f.write(thumbnail_request.content)
		else:
			os.mkdir(directory)
			with open("{}/{}.jpg".format(directory,video_id), 'wb') as f:
				f.write(thumbnail_request.content)

	

if __name__ == "__main__":
	app()