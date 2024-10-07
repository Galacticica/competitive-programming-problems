beats, buttons = (input()).split(' ')
beats = int(beats)
buttons = int(buttons)
points = 0
beat_array = []
button_array = []

for i in range (beats):
    beat_array.append(int(input()))

for i in range (buttons):
    button_array.append(int(input()))

# pass for 15
for i in range (len(beat_array)):
    for j in range (len(button_array)):
        if ((button_array[j] == None) or (beat_array[i] == None)) :
            pass
        elif (button_array[j] in range(beat_array[i]-15, beat_array[i]+16)):
            points += 7
            button_array[j] = None
            beat_array[i] = None
            for k in range(j+1):
                button_array[k] = None

for i in range (len(beat_array)):
    for j in range (len(button_array)):
        if ((button_array[j] == None) or (beat_array[i] == None)):
            pass 
        elif (button_array[j] in range(beat_array[i]-23, beat_array[i]+24)):
            points += 6
            button_array[j] = None
            beat_array[i] = None
            for k in range(j+1):
                button_array[k] = None

for i in range (len(beat_array)):
    for j in range (len(button_array)):
        if ((button_array[j] == None) or (beat_array[i] == None)):
            pass
        elif (button_array[j] in range(beat_array[i]-43, beat_array[i]+44)):
            points += 4
            button_array[j] = None
            beat_array[i] = None
            for k in range(j+1):
                button_array[k] = None

for i in range (len(beat_array)):
    for j in range (len(button_array)):
        if ((button_array[j] == None) or (beat_array[i] == None)):
            pass
        elif (button_array[j] in range(beat_array[i]-102, beat_array[i]+103)):
            points += 2
            button_array[j] = None
            beat_array[i] = None
            for k in range(j+1):
                button_array[k] = None

print (points)