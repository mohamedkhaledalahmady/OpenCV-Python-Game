# *OpenCV-Python-Game*
> ## Game Description:
   * By using OpenCV library with python, able to implement this game, it video game when game start your webcam open and your work to push buttons that appear on screen. i used openCV and cvzone libraries with python to access camera and detect position of hand.
   * To calculate distance of hand from camera, i do sequence of trail and collect data between x and y, where:
      * x &#x2192; represent distance between point (5) and (17) in image bellow.
      * y &#x2192; represent actual distance in centimeters.
    this is one challenge of project to find relation to relate x and y, as relation is nonlinear.
   * Store players names and their scores in a file `Players.txt` and display at end of game max score till now.
   * Game has down counter after it exceed the Game Over, and has two options 
      * press `r` to repeat game
      * press `ESC` to end game
<p style="text-align:center;">
   <img src="images/hand_landmarks.png" alt="Logo" width="771.5" height="269">
</p>

> ## Contents:
   * _game.py_ &#x2192; source code of game
   * _modules folder_ &#x2192; contain helper.py file taht contain some useful functions implemented 
   * _Makefile_ &#x2192; makfile to run python file
   * _Players.txt_ &#x2192; text file to store players name and their scores
   * _images_ &#x2192; folder contain all images
   * _video_ &#x2192; folder contain video while game running 
   
> ## Setup and run game:
   * Clone project on your local machine 
    `git clone https://github.com/mohamedkhaledalahmady/OpenCV-Python-Game.git`
   * Download `OpenCV` library and other libraries required:
        * by using pip package `pip install opencv-python`
        * by using pip package `pip install cvzone`
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
