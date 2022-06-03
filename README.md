# ColabFiles

PLEASE READ THIS ONCE

This project ran successfully with no error during the time of creation but revisiting it now, the tensorflow versions have changed for which "No module named tensorflow.python" error pops up.

I tried with many tensorflow versions and ran it in Windows and Ubuntu to check for any system incompatibility but the error still remained until Google Colab was able to run it but it has its own setbacks.

The first Google Colab Setback was that I couldn't use my webcam directly via my Python code for which I had to import the Camera Code Snippet which is written in JSX.
The second being, uploading the model and label is a must while running the Colab file and it stays only for the session.

There are 5 files in the zip named "FRAS_Colab.ipynb", "FRAS.py", "oldFRAS.py", "celebrity&empty.h5" and "celebrity&empty.txt", which are explained below:

	1) FRAS_Colab.ipynb: 	Code file. Most RECOMMENDED way of running this file in Google Colab. Webcam Access Required to click an Image
	2) FRAS_Colab_Upload: 	Code file. RECOMMENDED if you want to upload an image to check instead of clicking an image through webcam.
	3) OldFRAS.py: 	Code file that I used during the Project. If you are lucky, it will run without Google Colab. It will access your webcam, click an image and process it.
	4) celebrity&empty.ipynb: Machine Learning Model that has been trained on 20 Celebrities with 50 images per person.
	5) celebrity&empty.txt: The names of the celebrities which will be read by the program to recognise the person.

___________________________
Running "FRAS_Colab.ipynb":
___________________________

Step by step guide:

	1) Go to https://colab.research.google.com/
	2) Sign in with Google account
	3) After Signing in, select "New Notebook" option
	4) Click on File and select "Upload Notebook" 
	5) Click "Choose File" and head over to my zip, extract it and select "FRAS_Colab.ipynb"
	6) On extreme left hand side, click "Files" found below "{X}".
	7) Click on "Upload to session storage" and select "celebrity&empty.h5" and "celebrity&empty.txt"
	8) After it's uploaded, Press CTRL+F9 or Runtime->Run All
	9) Give permission for Camera, click "Allow"
	10) On second cell you can Capture an image using your webcam 
	11) You will find a CSV file created based on the date where you uploaded the model, download to check the details.


___________________________
Running "FRAS_Colab_Upload.ipynb":
___________________________

Step by step guide:

	1) Go to https://colab.research.google.com/
	2) Sign in with Google account
	3) After Signing in, select "New Notebook" option
	4) Click on File and select "Upload Notebook" 
	5) Click "Choose File" and head over to my zip, extract it and select "FRAS_Colab_Upload.ipynb"
	6) On extreme left hand side, click "Files" found below "{X}".
	7) Click on "Upload to session storage" and select "celebrity&empty.h5" and "celebrity&empty.txt"
	8) After the model and label are uploaded, select the image you want to check but rename it to "image.jpg"
	9) Press CTRL+F9 or Runtime->Run All
	10) You will find a CSV file created based on the date in Files (below {X}), download to check the details.


___________________
Running OldFras.py:
___________________

Step by step guide:

	1) Make sure you have Python 3.7 in your system.
	2) Open cmd and run "pip install tensorflow keras pillow image opencv-python" to download required packages.
	3) Extract my zip in a folder and open "OldFRAS.py" using any IDE and Run the program.
	4) Open the folder where you extracted, you will find a CSV file which will have the details.



*** The Celebrities on whom the model was trained can be found in celebrity&empty.txt file, if picture of anyone other than them is uploaded or your picture is clicked for processing, the result will be the Celebrity which resembles the most.***


In depth details on the functions used in OldFRAS.py:

	1) readLabels()- This function reads the label data from the text file using file handling. The labels or classes are automatically stored in a global list variable.
	2) imageCapture()- This module uses OpenCV to access the camera and use it to save the image captured by the camera. The image is saved as “image.jpg” on the folder where the program and model have been saved. The image gets replaced every time the system saves an image, overwriting the previous image and saving memory from getting clogged due to the continuous image saving habit of the system.
	3) imageProcessing()- The saved model is first loaded and the image saved is accessed by the system which later changes the dimensions and saves it in a NumPy array. The system thus converts every image into an array after which it fits it into the model to find the closest possibility of the image being in the model. After which it finds the maximum possibility of the subject in the model. The accuracy of the prediction can be set with a variable to make sure any prediction made is accurate enough to be considered as a record. The prediction percentage is then converted into the label stored according to the maximum probability of the subject. The function then calls dateTime and passes the prediction label.
	4) dateTime(x)- This function takes the stored label, checks the system time, and then saves it into the excel sheet. The excel sheet will be edited or else it will be created with a name that is based on the date. The creation of a new CSV is done once daily and every time a new record is stored, all the old records are automatically stored above it so that there is no data loss of any kind. 
