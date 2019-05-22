song_list = {}
menu = ['Show All Songs', 'Show Details', 'Play a Song', 'Search and Download', 'Exit']
counter = 1
for i in menu:
    print (counter, ".", i)
    counter += 1
action = input(">>> ")

if action == 1:
    if song_list.items() != 0:
        for key, value in song_list.items():
            print (counter, ".", key)
    else:
        print ("There is no song!")
