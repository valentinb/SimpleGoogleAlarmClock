import time
import os

class Hour:
    "Manage Hour"

    def update(self):
        print "Update !"

    def print_time(self):
        os.system("clear")
        print time.strftime("%H:%M")
