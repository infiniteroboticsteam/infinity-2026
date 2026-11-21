# Getting Started

This guide takes you from "nothing installed" to "my code is running on the
robot". Do the steps in order. You only need to do this once per computer
(step 1 is once per hub).

**Before you begin:** do the [Git and GitHub setup](SETUP.md) first. It
explains how to get a GitHub account and download (clone) this project. The
steps below assume you can already clone the repo.

**What you will need**

- A computer (Windows, Mac, or Linux) with Bluetooth
- A LEGO SPIKE Prime hub and its USB cable
- Chrome or Edge (for installing the hub firmware)

---

## 1. Set up the hub (once per hub)

The hub normally runs LEGO's own software. We replace it with **Pybricks**,
which lets us write our own Python programs.

1. Connect the hub to your computer with the USB cable.
2. Open <https://code.pybricks.com/> in Chrome or Edge.
3. Click **Install Pybricks Firmware** on the left and follow the
   instructions.
4. When it asks you to name your hub, give it a short, unique name such as
   `infinite-1` or `infinite-2`.

   > **Write this name down.** The robot code uses the name to know which
   > robot it is running on, and VS Code uses it to find your hub over
   > Bluetooth. See [Code Guide](CODE_GUIDE.md#robot-profiles-one-per-hub).

You can also write and run code directly on code.pybricks.com. We use VS Code
instead because it works much better for a team project with many files.

---

## 2. Install Python

1. Download Python from <https://www.python.org/downloads/> and install it.
2. **Windows only:** on the first installer screen, tick
   **"Add python.exe to PATH"** before you click Install.

To check it worked, open a terminal (Terminal on Mac, PowerShell on Windows)
and type:

```bash
python --version
```

(On Mac you may need `python3 --version`.) You should see a version number.

---

## 3. Windows only: allow PowerShell scripts

VS Code starts your Python "virtual environment" with a PowerShell script, and
Windows blocks that by default. Open PowerShell (you do not need
administrator) and run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Type `Y` if it asks you to confirm.

---

## 4. Set up VS Code

VS Code is the program where you will write code.

1. Download and install VS Code: <https://code.visualstudio.com/download>
2. Open VS Code. Click the **Extensions** icon on the left (four squares),
   search for **Python**, and install the one from Microsoft. This also
   installs Pylance, which underlines mistakes in your code.
3. **Clone the repo.** Click **Source Control** on the left (or press
   `Ctrl+Shift+G`), choose **Clone Repository**, and enter:

   ```
   git@github.com:infiniteroboticsteam/infinity-2026.git
   ```

   Open the folder when VS Code asks.

   > If you already cloned it from the terminal (see [SETUP](SETUP.md)),
   > use **File → Open Folder** and pick the `infinity-2026` folder instead.

4. **Create a virtual environment.** This is a private box of Python tools
   just for this project, so it cannot mess up anything else on your computer.
   Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux,
   `Cmd+Shift+P` on Mac), type **Python: Create Environment**, choose
   **Venv**, and pick the Python you installed in step 2.

5. **Install the Pybricks tools.** Open the Command Palette again and run
   **Python: Create Terminal**. A terminal opens at the bottom with
   `(.venv)` at the start of the line. Type:

   ```bash
   pip install pybricks pybricksdev
   ```

   - `pybricks` lets VS Code understand the robot commands (so it can help you
     type them and underline mistakes).
   - `pybricksdev` is the tool that sends your code to the hub.

   If you do not see `(.venv)`, close the terminal and run
   **Python: Create Terminal** again.

6. **Create your run configuration.** Pressing **F5** in VS Code needs a file
   called `.vscode/launch.json` that says "send this file to my hub".
   That folder is private to each computer (it is in `.gitignore`), so a fresh
   clone does not have it — you make your own:

   1. In the file list on the left, create a folder named `.vscode`
      (if it is not there already).
   2. Inside it, create a file named `launch.json` with this content, and
      change `infinite-1` to **your hub's name**:

      ```json
      {
          "version": "0.2.0",
          "configurations": [
              {
                  "name": "Run current file on hub (Bluetooth)",
                  "type": "debugpy",
                  "request": "launch",
                  "module": "pybricksdev",
                  "args": ["run", "ble", "--name", "infinite-1", "${file}"],
                  "console": "integratedTerminal",
                  "justMyCode": true
              }
          ]
      }
      ```

   Because `.vscode/` is not shared through Git, everyone can use their own
   hub name without affecting anyone else.

---

## 5. Run your first program

1. Turn on the hub (press the center button). Make sure Bluetooth is on in
   your computer and that no other program (such as code.pybricks.com) is
   connected to the hub.
2. Put the robot on the floor with a clear space of about 1 meter in front.
3. In VS Code, open `TestRun.py`.
4. Press **F5**.

The code is sent to the hub over Bluetooth and starts running. The robot
drives forward one wheel rotation and then backward. Anything the program
`print()`s shows up in the VS Code terminal.

If F5 does not work, run the same thing by typing in the VS Code terminal
(replace `infinite-1` with your hub's name):

```bash
pybricksdev run ble --name infinite-1 TestRun.py
```

**To stop a program early:** press the hub's center button, or
press `Ctrl+C` in the VS Code terminal.

If the robot did not move, or you saw an error, go to
[Testing and Troubleshooting](TESTING_AND_TROUBLESHOOTING.md).

---

## 6. Create a profile for your driving base

**Every team member must do this for their own driving base before writing or
testing runs.**

Our code does not know how your robot is built. Which ports the motors are
plugged into, which way they turn, how big the wheels are, and how the hub is
mounted all differ from robot to robot. That information lives in one file,
`robot_profiles.py`, as one **profile per hub**. When the code starts, it asks
the hub for its name and loads the profile with the same name.

Until you add a profile for your hub name, the code prints
`No profile for hub ... - using infinite-1` and borrows Coach Chao's robot.
If your robot is wired differently, it may drive backward, spin in circles, or
crash!

### Steps

1. **Know your hub name.** It is the name you chose in step 1 and put in
   `launch.json` (for example `infinite-2`). The profile name must match it
   exactly, including capitals and dashes.
2. **Write down your robot's details:**
   - which port (A–F) each drive motor, attachment motor, and color sensor is
     plugged into
   - the wheel diameter in mm (measure it; the wheels we use are 56 mm)
   - the axle track in mm: the distance between the points where the two
     wheels touch the ground
   - how the hub is mounted: which side faces up, and which side faces forward
3. **Open `robot_profiles.py`** in VS Code.
4. **Copy the `"infinite-1"` entry**, paste it right below itself inside
   `PROFILES`, and edit the copy. It should look like this (the example
   below is for a hub named `infinite-2`):

   ```python
   PROFILES = {
       # coach chao's robot
       "infinite-1": {
           ...
       },

       # <your name>'s robot
       "infinite-2": {
           "hub_top_side": Axis.Z,
           "hub_front_side": - Axis.Y,
           "wheel_diameter": 56,  # mm
           "axle_track": 114,     # mm
           "drive_left": {"port": Port.C, "direction": Direction.COUNTERCLOCKWISE},
           "drive_right": {"port": Port.D, "direction": Direction.CLOCKWISE},
           "left_attachment": {"port": Port.B, "direction": Direction.COUNTERCLOCKWISE},
           "right_attachment": {"port": Port.A, "direction": Direction.COUNTERCLOCKWISE},
           "left_color_sensor": Port.E,
           "right_color_sensor": Port.F,
       },
   }
   ```

   Change the name (the key) and every value that doesn't match your robot.
   If your robot has no right attachment or no color sensor, delete that line.
   Keep the commas and brackets: a missing comma is a `SyntaxError`.
5. **Don't edit anyone else's profile.** Add your own entry only.
   (`DEFAULT_PROFILE` at the bottom of the file stays as it is.)
6. **Test it.** Put the robot on a stand or hold it in the air, open
   `port_test.py`, and press **F5**. The first line of output should say
   `using profile <your hub name>`. Then check each part moved as expected. If
   the robot drives backward or an attachment turns the wrong way, flip
   `CLOCKWISE` ↔ `COUNTERCLOCKWISE` for that motor and run it again. See
   [`port_test.py`](TESTING_AND_TROUBLESHOOTING.md#port_testpy--does-the-profile-match-the-robot).
7. **Share it.** Commit `robot_profiles.py` with your new entry and open a
   pull request (see the [Git workflow](SETUP.md#6-daily-workflow)). Because
   each person only adds their own entry, profiles rarely conflict.

For what each setting means, how to work out the hub orientation, and what
`Direction` does, see
[Robot profiles](CODE_GUIDE.md#robot-profiles-one-per-hub) in the Code Guide.

---

## What next?

| If you want to... | Read |
|---|---|
| Learn the Python you need (no experience needed) | [Python Basics](PYTHON_BASICS.md) |
| Understand how all the files fit together | [Code Guide](CODE_GUIDE.md) |
| Write a run for a mission | [Writing Runs](WRITING_RUNS.md) |
| Fix something that is not working | [Testing and Troubleshooting](TESTING_AND_TROUBLESHOOTING.md) |
| Save and share your code with the team | [Git workflow](SETUP.md#6-daily-workflow) |
