
# *OpenCV-Python-Game*
> ## Game Description:
   * By using OpenCV library with python, able to implement this game, it video game when game start your webcam          
   open and your work to push buttons that appear on screen. i used openCV and cvzone libraries with python to access camera and detect position of hand.
   * To calculate distance of hand from camera, i do sequence of trail and collect data between x and y, where
    x &#x2192; represent distance between point (5) and (17) in image bellow
    y &#x2192; reprecent actual distance in centimeters
    this is one challenge of project to find relation to relate x and y, as relation is nonlinear

  <p style="text-align:center;">
        <img src="images/hand_landmarks.png" alt="Logo" width="771.5" height="269">
  </p>   
> ## Contents:
   * _game.py_ &#x2192; source code of game
   * _modules folder_ &#x2192; contain helper.py file taht contain some useful functions implemented 
   * _Makefile_ &#x2192; makfile ti run python file
   * _Players.txt_ &#x2192; text file to store players name and their scores
   
> ## Setup and running settings:
   * Download `OpenCV` library and other libraries:
        * by using pip package `pip install opencv-python`
        * by using pip package `pip install cvzone`
   * Clone project on local machine 
   * open terminal in project directory
   * run code by typing `make` or `make run`
   * enjoy &#128522;
> ### Images:
<img src="images/screen%200.png" width="640" height="360">
<img src="images/screen%206.png" width="640" height="360">

> ### Video:
  * <a href="https://drive.google.com/file/d/1St52DaiI-QAjCqqSOWrf7c3OeruUm7kQ/view?usp=sharing">
            while game running
   </a>
