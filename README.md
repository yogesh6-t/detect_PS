# detect_PS

the code is triggered by an argument parser which takes in 3 different arguments a: file b: rotate(boolean) c: gray(boolean) d:save(boolean) where
a: file is the path of the repository which contains all the video files
b: rotate is a boolean argument which by default is False, for the situation when we have to rotate the frame of videos, we will have to set the argument to 'true' explicitly
c: gray is a boolean argument which by default is False, for the situation when we have to convert each frame to gray scale, we will have to set the argument to 'true' explicitly
d: save is a boolean argument which by default is False, for the situation when we have to save the frame of videos, we will have to set the argument to 'true' explicitly

To execute the script navigate to the repository where the code is saved, from a command prompt run the python script with or without the arguments as specified
for e.g. to just run the videos 'python <path of script detect-3.py >', for rotating, gray scale and saving frames 'python <path of script detect-3.py > -r  True -s True -g True'
