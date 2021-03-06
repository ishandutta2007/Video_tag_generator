#!/bin/python3

from multiprocessing.dummy import Pool as ThreadPool
import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from collections import Counter
import glob
import speech_recognition as sr
import subprocess as sp
import sys
import threading
import time

def processing(text):
    print('processing...')
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = [wordnet_lemmatizer.lemmatize(x.lower()) for x in tokenizer.tokenize(text) if x.lower() not in stopwords.words("english")]
    count = Counter(tokens)
    sorted_tags = sorted(count, key=count.get, reverse=True)
    imp_tags = [x[0] for x in nltk.pos_tag(sorted_tags) if 'NN' in x[1]]
    db = [x.lower().strip() for x in open('db.txt').read().split('\n')]
    return [x for x in imp_tags if x in db]

def pat_to_wav(file_pattern):
    filenames = glob.glob(file_pattern)
    print("Following files are selected: ", filenames)
    ret = []
    for filename in filenames:
        cmd = 'ffmpeg -y -i '+ filename +' -vn -acodec pcm_s16le -ar 44100 -ac 2 ' + filename[:-4]+'.wav'
        p = sp.Popen(cmd,shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        out, err = p.communicate()
        ret.append(filename[:-4]+'.wav')
    return ret

def get_audio(filename):
    with sr.AudioFile(filename) as source:
        r=sr.Recognizer()
        print("Geting audio... ",filename)
        audio = r.record(source)  # read the entire audio file
    return audio

def recog(audio):
    print("recognizing...")
    r=sr.Recognizer()
    text = r.recognize_sphinx(audio)
    return text
        
start = time.clock()
threads = []
file_pattern = sys.argv[1]
wav_files = pat_to_wav(file_pattern)

i = 0
audio=[0]*len(wav_files)
for x in wav_files:
    audio[i] = get_audio(x)
    i+=1
# Start new Threads
pool = ThreadPool(len(audio))
results = pool.map(recog, audio)
pool.close()
pool.join()

i=0
for x in results:
	print(wav_files[i],processing(x))
    i+=1

print("time:", time.clock() - start)
print ("Exiting Main Thread")
