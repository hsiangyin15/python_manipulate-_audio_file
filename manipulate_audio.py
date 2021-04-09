
# -*- coding: utf-8 -*
import os
from os import path
from pydub import AudioSegment

# files
src_path = "raw_songs/"
src = " "
#src = src_path + src
dst = ""
for filename in os.listdir(src_path):
  if filename.endswith(".wav"):
    dst = filename[:-4]
    dst_path = "done_mp3/" + dst + "(40sec).mp3"
    src = src_path + filename
    sound = AudioSegment.from_file(src)
    sound = sound[50000:]
    sound = sound[:40000]
    sound.export(dst_path, format="mp3")
  
  elif filename.endswith(".mp3"):
    dst = filename[:-4]
    dst_path = "done_mp3/" + dst + "(40sec).mp3"
    src = src_path + filename
    sound = AudioSegment.from_file(src)
    sound = sound[50000:]
    sound = sound[:40000]
    sound.export(dst_path, format="mp3")


