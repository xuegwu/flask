# translator.py
import datetime
import json


MAX_SIZE= 20 * 1024 * 1024

replyBuf = ''

def translate(text):
    global replyBuf
    current_time = datetime.datetime.now()
    buf = str(current_time) + ':'+'\n'+text+'\n'
    replyBuf = replyBuf + buf

    while len(replyBuf) > MAX_SIZE:
        pos = replyBuf.index('\n', 1) + 1
        replyBuf = replyBuf[pos:]

    return replyBuf
