import os
import time 
from config import *
import shutil

if os.path.exists('Bote.session-journal'):
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Bote.session-journal')
	os.remove(path)
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Bote.session')
	os.remove(path)
	time.sleep(1)
if os.path.exists('Bote.session'):
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Bote.session')
	os.remove(path)
	if os.path.exists('Bote_2.session'):
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Bote_2.session')
		os.remove(path)
	time.sleep(1)

from telethon.sync import TelegramClient

client = TelegramClient('Bote',api_id, api_hash)
client.start()
client.disconnect()
if os.path.exists('Bote.session-journal'):
    print('Error')
else:
    print('OK')
    shutil.copyfile("Bote.session", "Bote_2.session")
