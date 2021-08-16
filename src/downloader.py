from __future__ import unicode_literals
import youtube_dl

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def download(url, format):
    ydl_opts = {
        'format': format,
        'outtmpl': 'target/%(title)s',
        'noplaylist' : True,
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "Done"