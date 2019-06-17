import math as m

timeForPics = int(input())
scenes = int(input())
sceneTime = int(input())

timeForReady = timeForPics * 0.15
timeForScenes = scenes * sceneTime
timeNeeded = timeForReady + timeForScenes

if timeNeeded < timeForPics:
    print(f"You managed to finish the movie on time! You have {m.floor(timeForPics - timeNeeded)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {m.floor(timeNeeded - timeForPics)} minutes.")