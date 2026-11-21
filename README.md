# INFINITE ROBOTICS TEAM 2026

Robot code for Pybricks / FLL.

GitHub URL: https://github.com/infiniteroboticsteam/infinity-2026

Our driving base is based on the Nautiq Box:
https://www.fllcasts.com/materials/3056-nautiq-lego-education-spike-prime-box-robot

## Documentation

New to the team? Read these in order. No Python experience is needed.

| # | Guide | What you'll learn |
|---|---|---|
| 1 | [Developer Setup (Git & GitHub)](docs/SETUP.md) | Make a GitHub account, create an SSH key, clone the repo, and share your work with Git. |
| 2 | [Getting Started](docs/GETTING_STARTED.md) | Install Pybricks on the hub, install Python and VS Code, and run your first program on the robot. |
| 3 | [Python Basics](docs/PYTHON_BASICS.md) | Just the Python you need: variables, functions, `async`/`await`, loops, imports, and how to read errors. |
| 4 | [Code Guide](docs/CODE_GUIDE.md) | How the files fit together, robot profiles (ports, wheels, hub orientation), the hub menu, and gear-swap attachments. |
| 5 | [Writing Runs](docs/WRITING_RUNS.md) | Write, tune, and register a run for a mission. |
| 6 | [Testing and Troubleshooting](docs/TESTING_AND_TROUBLESHOOTING.md) | Test scripts, calibration, and fixes for common problems. |

## Quick start (if you've done the setup)

1. Turn on your hub, open `TestRun.py` in VS Code, and press **F5**.
2. **Create a profile for your driving base** in `robot_profiles.py`
   ([how](docs/GETTING_STARTED.md#6-create-a-profile-for-your-driving-base)),
   then run `port_test.py`.
3. Copy `M1_DroneSurvey.py`, edit it, and press **F5** to test your run.
4. When it works, add it to the menu in `robot.py`.

## Project layout

| File / folder | Purpose |
|---|---|
| `robot_profiles.py` | One entry per hub: ports, motor directions, wheel size, hub orientation. |
| `robot_config.py` | Builds the drive base, hub, attachments, and sensors from the profile. |
| `library.py` | Shared helpers such as `set_drivebase()`. |
| `gear_swap_motor.py` | Attachment motor that understands gear ratios. |
| `ui.py` | Hub-button menu for choosing a run. |
| `robot.py` | **The competition program.** Registers the runs and starts the menu. |
| `M1_DroneSurvey.py`, `RogerRun.py` | Runs. |
| `TestRun.py` | Drive one wheel rotation; checks the connection and wheel size. |
| `port_test.py`, `detect_port.py`, `color_test.py` | Hardware checks for ports, motors, and color sensors. |
| `gear_swap_test.py`, `gear_swap_motor_test.py` | Tests for the gear ratio math and for gear-swapped motors. |
| `docs/` | Team guides (above). |
| `advanced/` | Optional extras: music, measurement tools, Xbox controller driving. |
| `code_2025_unearthed/` | Last season's runs, kept for reference. |
| `depreciated/` | Older code, including `run_demo_1` … `run_demo_6` tutorials. |

The archive folders were written for an older `robot_config.py` and need
updating before they will run. Details in the [Code Guide](docs/CODE_GUIDE.md#file-map).

## Notes

- Pybricks runs **MicroPython**, a subset of Python. The upload tool sends your
  file plus the modules it imports from the **same folder**, so keep runs and
  shared modules in the repo root.
- Laptops and tablets are not allowed at the table, so the competition program
  is `robot.py`, which runs from the hub's buttons.

## References

### Gears

Introduction to gears:

- [Part 1](https://community.legoeducation.com/blogs/31/64)
- [Part 2](https://community.legoeducation.com/blogs/31/70)

## Credits

* The original code was forked from
  https://github.com/MonongahelaCryptidCooperative/FLL-2025-2026.
* Thanks to Boyd Fletcher for sharing his experience using Pybricks.
* Original guide to setting up VS Code for Pybricks:
  https://pybricks.com/project/pybricks-other-editors/
