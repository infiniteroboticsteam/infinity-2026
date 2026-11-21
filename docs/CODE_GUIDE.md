# Code Guide

How our robot code is organized, what each file does, and how to set it up
for your own robot. Read [Python Basics](PYTHON_BASICS.md) first if
terms like "function", "import" or "dictionary" are new to you.

Our driving base is based on the
[Nautiq Box](https://www.fllcasts.com/materials/3056-nautiq-lego-education-spike-prime-box-robot).

---

## The big picture

```
                         robot_profiles.py        "what is MY robot like?"
                                │                 (ports, wheel size, ...)
                                ▼
                          robot_config.py         creates DRIVE_BASE, HUB,
                                │                 LEFT_ATTACHMENT, ...
              ┌─────────────────┼──────────────────┐
              ▼                 ▼                  ▼
          library.py          ui.py        your run files
     (speed settings)    (hub menu)      (M1_DroneSurvey.py, ...)
              │                 │                  │
              └─────────────────┴────────┬─────────┘
                                         ▼
                                      robot.py     the competition program
```

Think of it in layers:

1. **`robot_profiles.py`** describes the physical robot.
2. **`robot_config.py`** reads that description and builds the Python objects
   that control the robot.
3. **Run files** import those objects and tell the robot what to do.
4. **`robot.py`** collects all the runs into a menu on the hub, so we can
   pick one with the hub buttons at the competition table.

---

## File map

### Core files (you will use these every day)

| File | What it does |
|---|---|
| `robot_profiles.py` | One entry per hub: motor and sensor ports, motor directions, wheel diameter, axle track, hub orientation. **The only place port numbers live.** |
| `robot_config.py` | Reads the connected hub's name, loads the matching profile, and creates `HUB`, `DRIVE_BASE`, `LEFT_ATTACHMENT`, `RIGHT_ATTACHMENT`, `LEFT_COLOR_SENSOR`, `RIGHT_COLOR_SENSOR`. Also holds the default speeds (`SPEED`, `ACCELERATION`, `TURN_SPEED`, `TURN_ACCELERATION`). |
| `library.py` | Shared helpers. `set_drivebase()` applies our default speeds and accelerations. `print_drivebase_settings()` prints the current ones. |
| `gear_swap_motor.py` | `GearSwapMotor`: an attachment motor that understands gears, so you can say "turn the *final gear* 90°" and it works out how far the *motor* must turn. |
| `ui.py` | The hub menu: shows a letter and color for each run, and lets you pick and start runs with the hub buttons. |
| `robot.py` | **The competition program.** Imports every run, registers it with the menu, and starts the menu. Laptops and tablets are not allowed at the table, so this is what runs on the hub. |

### Runs (the missions)

| File | What it does |
|---|---|
| `M1_DroneSurvey.py` | A run for Mission 1. |
| `RogerRun.py` | A run (Roger's version). |
| `TestRun.py` | Drives one wheel rotation forward and back. Use it to check the hub connection and calibrate wheel size. |

Add your own runs in the main folder the same way. See
[Writing Runs](WRITING_RUNS.md).

### Test and tool scripts

| File | What it does |
|---|---|
| `port_test.py` | Moves every motor and flashes every sensor in the profile so you can check the wiring matches `robot_profiles.py`. |
| `detect_port.py` | Finds out what is plugged into each port A–F and tests it. Use when you don't know what's where. |
| `color_test.py` | Shows what the color sensors see on the hub's display. |
| `gear_swap_test.py` | Checks the gear ratio math. No motor needed. |
| `gear_swap_motor_test.py` | Checks `GearSwapMotor` on the real robot with real gears. |

How to use them: [Testing and Troubleshooting](TESTING_AND_TROUBLESHOOTING.md).

### Folders

| Folder | What's in it |
|---|---|
| `docs/` | These guides. |
| `code_2025_unearthed/` | Last season's runs (`run1`…`run6`, `run_silo`). Kept for ideas. **They will not run as-is** — they use `CENTER_ATTACHMENT` and `FRONT_ATTACHMENT`, which the current `robot_config.py` no longer has (it has `LEFT_ATTACHMENT` and `RIGHT_ATTACHMENT`). |
| `advanced/` | Optional extras: `music_library.py` and `measurement/` (calibration tools, Xbox controller driving). These were written for an older `robot_config.py` and need updating before use. |
| `depreciated/` | Older code. `run_demo_1` … `run_demo_6` are short tutorials on the drive base, motors, sensors, and multitasking. They are good to read, but they too use the older attachment names. |

> **Rule of thumb:** if a file in a folder is not working, check its imports
> first. Names that no longer exist in `robot_config.py` cause an error.

---

## `robot_config.py`: what you can use

When you write `from robot_config import ...` you can pick up any of these:

| Name | What it is |
|---|---|
| `HUB` | The hub. Use `HUB.display`, `HUB.light`, `HUB.speaker`, `HUB.buttons`, `HUB.imu` (the gyro). |
| `DRIVE_BASE` | The two drive wheels as one unit. `straight()`, `turn()`, `curve()`, etc. |
| `LEFT_ATTACHMENT`, `RIGHT_ATTACHMENT` | The attachment motors (`GearSwapMotor`). Can be `None` if the profile does not define them. |
| `LEFT_COLOR_SENSOR`, `RIGHT_COLOR_SENSOR` | The color sensors. Can be `None`. |
| `HUB_NAME` | The name of the hub you are running on, such as `"infinite-1"`. |
| `PROFILE_NAME`, `PROFILE` | Which profile was loaded, and its contents. |
| `SPEED`, `ACCELERATION`, `TURN_SPEED`, `TURN_ACCELERATION` | Default drive settings (mm/s, mm/s², deg/s, deg/s²). |

Two things to know:

- `robot_config.py` runs **the moment any file imports it**. It talks to the
  hub and the motors. If a motor in the profile isn't plugged in, you get an
  error right away (see [Troubleshooting](TESTING_AND_TROUBLESHOOTING.md)).
- Pybricks defaults are slow and the acceleration is rough on the wheels.
  `SPEED = 700` etc. at the top of `robot_config.py` are our tuned values.
  If the wheels slip (distances come out short), lower `ACCELERATION`.
  Change them only after talking to your team, because they affect every run.

---

## Robot profiles: one per hub

Different robots have motors in different ports and different wheels. Rather
than editing code for each robot, each hub gets a **profile** in
`robot_profiles.py`. When the code starts, `robot_config.py` asks the hub
"what is your name?" and loads the profile with the same name.

```
Hub is named "infinite-2"  ──►  PROFILES["infinite-2"]  is loaded
```

If there is no profile with your hub's name, the code prints
`No profile for hub <name> - using infinite-1` and uses the default one.

### Adding your robot

1. Open `robot_profiles.py`.
2. Copy the whole `"infinite-1": { ... },` entry and paste it right below it.
3. Change the key to your hub's name exactly as you typed it when installing
   the firmware (capitals and dashes matter).
4. Update every value to match your robot, using the table below.
5. Save, then run `port_test.py` (press F5 on that file) and watch whether
   each part moves as expected.

### What each setting means

```python
"infinite-1": {
    "hub_top_side": Axis.Z,
    "hub_front_side": - Axis.Y,
    "wheel_diameter": 56,   # mm
    "axle_track": 114,      # mm
    "drive_left":  {"port": Port.C, "direction": Direction.COUNTERCLOCKWISE},
    "drive_right": {"port": Port.D, "direction": Direction.CLOCKWISE},
    "left_attachment":  {"port": Port.B, "direction": Direction.COUNTERCLOCKWISE},
    "right_attachment": {"port": Port.A, "direction": Direction.COUNTERCLOCKWISE},
    "left_color_sensor": Port.E,
    "right_color_sensor": Port.F,
},
```

| Setting | Meaning |
|---|---|
| `wheel_diameter` | Diameter of the drive wheel in millimeters. Measure it. Wrong value → every distance is wrong. |
| `axle_track` | Distance between the two points where the left and right wheels touch the ground, in millimeters. Wrong value → every turn is wrong. |
| `drive_left` / `drive_right` | Port of each drive motor and its **direction**. |
| `left_attachment` / `right_attachment` | Port and direction of each attachment motor. Leave the line out if you don't have it. |
| `left_color_sensor` / `right_color_sensor` | Port of each color sensor. Leave out if you don't have it. |
| `hub_top_side`, `hub_front_side` | How the hub is mounted. See below. |

**Ports** are the letters printed on the hub: `Port.A` … `Port.F`.

**Direction** is the way a motor turns when it is told to go *positive*
(forward for a drive wheel). The left and right drive motors face opposite
ways, so they usually have opposite directions. Not sure? Run `port_test.py`
and flip `CLOCKWISE` ↔ `COUNTERCLOCKWISE` for any motor that goes the wrong
way. Run it with the robot lifted off the table at first.

**Hub orientation.** The gyro measures turning around the hub's "up" axis, so
the code has to know which way the hub is mounted. The hub has three axes:

| Axis | Direction on the hub |
|---|---|
| `Axis.Z` | Top (the side with the light matrix) |
| `Axis.X` | Front |
| `Axis.Y` | Left |

A minus sign means the opposite side: `-Axis.Y` is the right side.

- `hub_top_side`: which side of the hub faces **up** on the robot.
- `hub_front_side`: which side of the hub faces the direction the robot
  **drives**.

For example, `Axis.Z` and `-Axis.Y` mean "the top of the hub faces up, and the
hub's right side faces forward". If this is wrong, turns with the gyro are
wrong too — for example, the robot spins too far or too little, or in the
wrong direction.

### What if I don't have an attachment?

Leave it out of the profile. In code, `LEFT_ATTACHMENT` will then be `None`,
and your run should not try to move it. (The test scripts skip anything that
is `None` automatically.)

---

## `library.py`

```python
await set_drivebase()
```

Call this at the start of every run. It sets the drive base to our standard
speed, acceleration, turn rate, and turn acceleration from `robot_config.py`.
Any settings you changed earlier are reset.

Why it matters: `DRIVE_BASE.settings(...)` stays in effect until you change it
again, even into the next run. Calling `set_drivebase()` at the beginning means
every run starts from the same known state.

```python
await print_drivebase_settings()
```

Prints the current settings (speed, acceleration, turn rate, turn
acceleration) to the terminal.

---

## `ui.py` and `robot.py`: the hub menu

At the competition you will not have a laptop, so `robot.py` shows a menu on
the hub:

| Hub button | What it does |
|---|---|
| **Left** (◀) | Previous run |
| **Right** (▶) | Next run |
| **Center** | Start the selected run |

The hub display shows a letter (for example `1`) and the button light shows a
color. We pick the color to match a color marker on the attachment, so it's
easy to confirm the right attachment is on the robot before pressing start.

A red light with an **E** means the gyro isn't ready. Put the robot flat and
still for a moment; the menu appears when the gyro is ready.

To add a run to the menu, you import it and add one line in `robot.py`:

```python
from M1_DroneSurvey import run_m1            # at the top

...
await add_program(run_m1, '1', Color.GREEN)  # in main(), before user_interface()
```

`add_program(function, letter, color)` takes the run function (no
parentheses!), the character to show, and the light color. Runs appear in the
menu in the order you add them. Full steps in
[Writing Runs](WRITING_RUNS.md#adding-your-run-to-the-menu).

`robot.py` also prints the drive base settings and calls `set_drivebase()`
once at startup.

> **Stopping a run:** `ui.py` disables the hub's normal stop button
> (`set_stop_button(None)`) so an accidental press does not stop the menu. To
> abort a run while running `robot.py` on the hub, turn the hub off by holding
> the center button. (When you press F5 on a single run file, the stop button
> works normally.)

---

## Attachments and gears (`gear_swap_motor.py`)

Attachment motors rarely connect directly to the part they move. Usually there
are gears in between. Gears change **how far** and **how fast** the part turns
compared to the motor.

`GearSwapMotor` lets you describe the gears once, then talk about the
**final gear** (the one touching the mission model):

```python
LEFT_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE, [12, 36])
await LEFT_ATTACHMENT.run_angle(100, 90)   # final gear turns 90 degrees at 100 deg/s
```

- The first argument is the direction the **final gear** turns for a positive
  angle. If it turns the wrong way, swap `CLOCKWISE` and `COUNTERCLOCKWISE`.
- The second argument lists the gears, in order, **from the motor to the
  final gear**, by their tooth counts.
- Use `None` if there are no gears: `reconfigure(Direction.CLOCKWISE, None)`.
- The angle and speed you give are for the final gear. The motor class
  multiplies them by the gear ratio for you.

You can call `reconfigure()` at the start of a run, so different attachments
(with different gears) can use the same motor.

### How to write the gear list

| You build | Write | Ratio |
|---|---|---|
| 8-tooth gear on the motor drives a 24-tooth gear | `[8, 24]` | 3 (final gear turns 3× slower, 3× stronger) |
| Same, with a 16-tooth gear in between as an *idler* | `[8, 16, 24]` | 3 (idlers cancel out) |
| 8T drives a 24T; an 8T fixed on the **same axle** as that 24T drives a 40T | `[8, (24, 8), 40]` | 3 × 5 = 15 |

A pair in parentheses, `(24, 8)`, is a **compound gear**: two gears locked on
the same axle, so they turn together. The first number is the gear that meshes
with the gear *before* it, the second number meshes with the gear *after*.

**Common mistake:** `[8, 24, 8, 40]` means four separate gears meshing in a
row (ratio 5). If the 24T and the 8T share an axle, you need `(24, 8)`.

`gear_swap_test.py` checks this math and `gear_swap_motor_test.py` tests it on
the robot; see [Testing](TESTING_AND_TROUBLESHOOTING.md).

### Limitations to know about

- Only `run_angle()` understands gears. Other motor commands like
  `run_target()`, `run()` and `angle()` use **raw motor degrees**.
- `run_angle()` on a `GearSwapMotor` **resets the motor angle to zero** each
  time (unless you pass `reset_angle=False`).
- The motor's real speed is `speed × ratio`. Large ratios can ask for more
  speed than the motor can give (about 1000 deg/s), so use a lower final-gear
  speed.

---

## MicroPython notes

The hub runs MicroPython, which is a subset of full Python:

- Only a small part of Python's standard library is available. If a tutorial
  online uses a library that is missing on the hub, it will not work.
- The upload tool sends your file and every module it imports **from the same
  folder**. So keep runs and shared modules in the repo root. Files in
  subfolders are not sent.
- The hub has limited memory. Keep prints and lists reasonable.
