import os
import subprocess

class Radio:
    "Manage Radio"

    def play(self):
        args = ['mplayer', '-playlist', 'http://bbc.co.uk/radio/listen/live/r4.asx']
        self.p = subprocess.Popen(args)
        #os.system("mplayer -playlist \"http://bbc.co.uk/radio/listen/live/r4.asx\"")

    def stop(self):
        p.kill()

