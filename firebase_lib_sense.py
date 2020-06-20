import os
import tkinter
import time
import json
from priv_key.firebase_sense import Firebase


def _structured_data_write(turn: str, who: str) -> None:
    cont = {
        u'turn': turn,
        u'who': who,
        u'time': int(time.time())
    }
    f.write(cont, False)
    return

f = Firebase()




last_logged = int(time.time())
while True:
    res = f.read_async()
    if res['time'] != last_logged:
        print("Latest read: ", end="")
        print(res)
        f.write({u"time": int(time.time())}, False)
        last_logged = f.read_async()['time']
    print(os.getcwd() + "->> ", end="")
    c = input()
    f.run(c)
    time.sleep(1)