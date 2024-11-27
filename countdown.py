from time import *
import threading
x=0
#actual bg timer part

if x == 0 :
    def countdown():
        global mytimer

        mytimer=5

        for x in range(5):
            mytimer = mytimer-1
            sleep(1)
        print('ehh')

countdownthread = threading.Thread(target = countdown)
countdownthread.start()
x=1
if x == 1:
    break
#secondry thinghy
while mytimer>0:
    print('ello mate')
    sleep(1)
print("done")

