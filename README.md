# CARTOONIFIER-WEB-APP

Our goal is to make the Real World Images look like they are genuinely from a Cartoon. This is done by using a bilateral filter and applying some edge detection on our input image.  

## Original Image

<img src="https://github.com/koyomi69/CARTOONIFIER-WEB-APP/blob/master/backend/src/input.jpg" height="50%" width="50%">

## Cartoonizer Result

<img src="https://github.com/koyomi69/CARTOONIFIER-WEB-APP/blob/master/backend/src/output.png" height="60%" width="60%">

### Process of Running Files

-) First of all, run the following command to install the required libraries:

pip install -r req.tx

-) Next, cd into backend and run the command:

python manage.py runserver 0.0.0.0:8181

-) Now open up your browser and enter your ip address and the 8181 port number in this format -> IPADDRESS:8181/cartoon 
  e.g. 127.0.0.1:8181/cartoon

-) Test the Cartoonizer Web App

-) Note: If some warning of unapplied migrations appears, then run the following command to solve it:

python manage.py migrate
