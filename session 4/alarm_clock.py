import datetime

import pyglet

music = pyglet.resource.media('crowd-cheering.mp3')
# currentDT = str(datetime.datetime.now().strftime("%I:%M"))
# # print (currentDT)
# alarmtime = str("08:01")
# if currentDT == alarmtime:
#     print ("Continue Sleeping")
# else:
#     print ("cais gif ddayas")


while True:
    currentDT = datetime.datetime.now().strftime("%I:%M")
    alarmtime = str("08:03")
    if currentDT != alarmtime:
        print ("Continue Sleeping")
    else:
        music.play()
        pyglet.app.run()
        break
