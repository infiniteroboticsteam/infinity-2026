# INFINITE ROBOTICS TEAM 2025
Starter Code for  Pybricks/FLL

Github url: https://github.com/infiniteroboticsteam/infinite-2025

Our driving base is based on the Nautiq Box: https://www.fllcasts.com/materials/3056-nautiq-lego-education-spike-prime-box-robot


# Set up the hub
* Connect your hub to your computer via cable.
* GO to https://code.pybricks.com/, click "Install Pybricks Firmware" on the left and follow the intructions to install pybricks firmware on your hub.
* You can use the web interface to write code and control the hub

Below are the instructions to use vscode for programming with pybricks

# Set up github
* Download (https://desktop.github.com/download/) and install github
* Log in to github with your google gmail account and create a github account.
* In github cmd (windows), set up user.name and user.email like below: 
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

# Change in powershell

* Open powershell as an admin, type "Set-ExecutionPolicy Unrestricted -Force"
This is needed otherwise vscode cannot open the venv.

# Install python

* Download (https://www.python.org/downloads/) and install python

# Set up vscode 

* Download (https://code.visualstudio.com/download) and install visual studio code. In vscode, 
* Install the following extensions: pylance, python
* In command, type "py create env" and select "Python: Create Environment..." to create a virtual environment
* In command, type "py create term" and select "Python: Create Terminal". In the terminal, type: pip install pybricks pybricksdev
* Click "source control" on the left, and clone our team repo: https://github.com/infiniteroboticsteam/FLL-2025-2026. Then you should have downloaded the repo in your local computer. 
* Click "Explorer" to go back to view the files. Go to .vscode/launch.json and change "infinite-1" to the name of your hub.
* Click "run_demo.py", review the code and Press F5 to do a test run.


# code structure

1. robot_config.py: defines the parameters for our driving base and sensor ports.

2. run_demo_*.py: following the numbers to learn how to control drive base, motors and sensors.

    A run is defined as a procedure where the driving base with attachments installed starts from a launch area and returns to either a home area or a launch area. 

    A run can be programed to complete multiple missions.
3. Steps to write your code for a run.
    * Create a file run_missions_*.py according to your missions. 
    * For each run to finish multiple missions, define a function to move the each attachment to complete a mission.
    * Define a function to move the driving base, at approporiate waypoint (based on distance), add movements for attachments.
    * Run the file to test the function for a run in your run.

4. robot.py & ui.py: We will use robot.py to add all runs to the program so that during the competition we run different runs by pressing buttons on the hub. Remember, laptop/ipad are not allowed in the game.


# Use git to upload your code for missions

TODO

* If you changed the name in launch.json, do not add the json file in your commit.

# Notes

## spike prime and pybricks are based on MicroPython
MicroPython uses a subset of modules from standard python. Spike prime does not include sys module. so folders may not be useful.


# References

## Gears

See here for introduction to gears: 
    - [Part 1](https://community.legoeducation.com/blogs/31/64)
    - [Part 2](https://community.legoeducation.com/blogs/31/70)
    

# Credits

* The original repo was forked from https://github.com/MonongahelaCryptidCooperative/FLL-2025-2026.
* Thanks to Boyd Fletcher for sharing his experience using pybricks.
* Original guide to set up vscode for pybricks: https://pybricks.com/project/pybricks-other-editors/
