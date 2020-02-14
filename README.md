# Real-Time-Facial-Recognition-using-OpenCV

Real time Facial Recognition using opencv haarcascade with automatic dataset creater.

Just follow these simple steps.

1. Run "python dataset-creater.py" in cmd.Enter id of the user. If there are n users then run this command n times with different ids. Make sure person is ready at the camera so that data can be collected automatically. Your dataset will be saved in dataset folder.

2. Run "python trainner.py" in cmd. Your .yml file will be saved in trainner folder.

3. Now run "python detector.py" in cmd. Before running this file, make sure you have entered name according to the id inside the file. Camera will recognize every user according to the ids.

I have tested this in windows as well as in linux(Eg. Raspberry Pi). 
