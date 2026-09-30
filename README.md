# INFINITE ROBOTICS TEAM 2026

Starter code for Pybricks / FLL.

GitHub URL: https://github.com/infiniteroboticsteam/infinity-2026

Our driving base is based on the Nautiq Box:
https://www.fllcasts.com/materials/3056-nautiq-lego-education-spike-prime-box-robot

> **New to Git/GitHub?** Follow the [Developer Setup Guide](docs/SETUP.md)
> first — it covers creating a GitHub account, generating an SSH key, and
> cloning this repo. The steps below assume you can already clone the repo.

---

# 1. Set up the hub

1. Connect your hub to your computer with a USB cable.
2. Go to https://code.pybricks.com/, click **Install Pybricks Firmware** on the
   left, and follow the instructions to install the Pybricks firmware on your hub.
3. When prompted, give your hub a name (e.g. `infinite-1`). You'll need this
   name later to run code from VS Code.
4. You can use the web interface at code.pybricks.com to write code and control
   the hub directly. The rest of this guide sets up VS Code instead.

# 2. Install Python

Download and install Python from https://www.python.org/downloads/.

On **Windows**, check **"Add python.exe to PATH"** in the installer.

# 3. Windows only: allow PowerShell scripts

VS Code activates the Python virtual environment with a PowerShell script,
which Windows blocks by default. Open PowerShell (no admin needed) and run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Answer `Y` if prompted.

# 4. Set up VS Code

1. Download and install VS Code: https://code.visualstudio.com/download
2. Install the **Python** extension (this also installs Pylance).
3. Clone this repo: click **Source Control** on the left (or press
   `Ctrl+Shift+G`), choose **Clone Repository**, and enter
   `git@github.com:infiniteroboticsteam/infinity-2026.git`.
   Open the cloned folder when prompted.
4. Open the Command Palette (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on Mac),
   type **Python: Create Environment**, choose **Venv**, and pick the Python
   you installed in step 2.
5. Open the Command Palette again, run **Python: Create Terminal**, and in that
   terminal install the tools:

   ```bash
   pip install pybricks pybricksdev
   ```

6. Open `.vscode/launch.json` and change `infinite-1` to your hub's name.
   **Do not commit this change** — everyone's hub name is different.
7. Turn on your hub, open `TestRun.py`, and press **F5**. The code is sent to
   the hub over Bluetooth and runs. Output from `print()` appears in the VS
   Code terminal.

   If F5 doesn't work, you can run the same thing from the terminal:

   ```bash
   pybricksdev run ble --name infinite-1 TestRun.py
   ```

---

# Code structure

| File / folder | Purpose |
|---|---|
| `robot_config.py` | Parameters for the driving base (wheel size, axle track, motor ports, sensor ports) and the `GearSwapMotor` helper for attachments with swappable gearing. |
| `library.py` | Shared helpers: `set_drivebase()` applies our speed/acceleration settings, `print_drivebase_settings()` prints the current ones. |
| `run1.py` … `run6.py` | One file per **run**. Each defines an `async def runN()` that drives the base and moves attachments to complete its missions. |
| `run_silo.py` | Test script for the center attachment. |
| `ui.py` | Hub menu: `add_program()` registers a run under a button/color; `user_interface()` lets you pick and start runs with the hub buttons. |
| `robot.py` | **The competition program.** Imports all runs, registers them with `ui.py`, and starts the menu. Laptops/tablets are not allowed at the table, so this is what runs on the hub. |
| `TestRun.py` | Drives one wheel rotation forward — use it to check the hub connection and calibrate `robot_config.py`. |
| `DetactPort.py` | Lists which motor/sensor is plugged into each port. |
| `advanced/` | Optional extras: `music_library.py` and `measurement/` (calibration tools, Xbox controller teleop). See `advanced/README.md`. |
| `depreciated/` | Last season's code, kept for reference. `run_demo_1` … `run_demo_6` are tutorials on the drive base, motors, and sensors — read them in order if you're new to Pybricks. See `depreciated/README.md`. |
| `docs/` | Team documentation (Git/SSH setup guide). |

## What is a run?

A **run** is a trip where the driving base, with attachments installed, starts
from a launch area and returns to a home or launch area. One run can complete
several missions.

## Writing a new run

1. Copy `run1.py` to the next free number (e.g. `run7.py`) and rename the
   function inside to match (`async def run7()`).
2. Define a function per attachment movement needed for each mission.
3. Write the driving path. At the appropriate waypoints (by distance or turn),
   call the attachment functions.
4. Test the run on its own: open the file and press **F5**.
5. When it works, add it to `robot.py`:
   ```python
   from run7 import run7
   ...
   await add_program(run7, '7', Color.WHITE)
   ```
   Match the color to the color marker on the attachment so it's easy to pick
   the right one at the table.

## Uploading your code with Git

See the [Developer Setup Guide](docs/SETUP.md#6-daily-workflow) for the
pull → branch → commit → push → pull request workflow.

* If you changed the hub name in `.vscode/launch.json`, do not include that
  file in your commit.
* Don't commit `__pycache__/` — it's already in `.gitignore`.

---

# Notes

## Pybricks is MicroPython, not full Python

MicroPython on the SPIKE Prime hub includes only a subset of the standard
library. `pybricksdev` uploads the file you run plus any modules it imports
from the **same folder**, so keep runs and shared modules in the repo root —
packages in subfolders won't work on the hub.

# References

## Gears

Introduction to gears:

- [Part 1](https://community.legoeducation.com/blogs/31/64)
- [Part 2](https://community.legoeducation.com/blogs/31/70)

# Credits

* The original code was forked from
  https://github.com/MonongahelaCryptidCooperative/FLL-2025-2026.
* Thanks to Boyd Fletcher for sharing his experience using Pybricks.
* Original guide to setting up VS Code for Pybricks:
  https://pybricks.com/project/pybricks-other-editors/
