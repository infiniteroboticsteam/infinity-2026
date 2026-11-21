# Writing Runs

How to write, test, and add a run for the robot. If you're new to Python,
read [Python Basics](PYTHON_BASICS.md) first, and skim the
[Code Guide](CODE_GUIDE.md) to see where things come from.

---

## What is a run?

A **run** is one trip where the robot, with the right attachments installed,
leaves a launch area, completes one or more missions, and comes back to a
home or launch area. We write one function per run, and pick which run to
start from the menu on the hub.

---

## Your first run, step by step

### 1. Make your file

Create a new file in the **main folder** (next to `robot.py`), for example
`M2_Example.py`. Don't put it in a subfolder: the hub won't find it.

You can also copy `TestRun.py` or `M1_DroneSurvey.py` and edit the copy.

### 2. Use this template

```python
from pybricks.tools import run_task, wait

from library import set_drivebase
from robot_config import DRIVE_BASE


async def run_m2():
    DRIVE_BASE.use_gyro(True)         # use the gyro for accurate turns
    await set_drivebase()              # start from our standard settings

    await DRIVE_BASE.straight(500)    # forward 500 mm
    await DRIVE_BASE.turn(90)         # turn right 90 degrees
    await DRIVE_BASE.straight(200)    # forward 200 mm

    DRIVE_BASE.use_gyro(False)        # turn the gyro off when done


if __name__ == "__main__":
    run_task(run_m2())
```

Things to notice:

- The function is `async def` and every robot move has `await` in front.
- It starts with `use_gyro(True)` and `await set_drivebase()` so each run
  begins the same way.
- The block at the bottom lets you press **F5** to run this file alone.
  Change `run_m2` there if you rename the function.
- Give your function a **unique name**, such as `run_m2`. If two files both
  define `main`, importing both into `robot.py` causes confusion.

### 3. Test it

Put the robot at the start position, open your file, and press **F5**. Watch
the robot, read the terminal, and adjust the numbers. See
[Tuning](#tuning-your-run) below.

---

## Driving commands

All of these live on `DRIVE_BASE` and need `await`.

| Command | What it does |
|---|---|
| `await DRIVE_BASE.straight(500)` | Drive forward 500 mm. Use a negative number to go backward. |
| `await DRIVE_BASE.turn(90)` | Turn in place 90° **clockwise (right)**. Use a negative number for left. |
| `await DRIVE_BASE.curve(300, 90)` | Drive along an arc with a 300 mm radius, through 90°. |
| `DRIVE_BASE.use_gyro(True)` | Use the hub's gyro to keep headings accurate. (No `await`.) |
| `DRIVE_BASE.settings(...)` | Change speed, acceleration, turn rate. (No `await`.) |
| `DRIVE_BASE.distance()` | How far the robot thinks it has driven, in mm. |
| `DRIVE_BASE.reset()` | Set distance and angle readings back to zero. |
| `DRIVE_BASE.stop()` | Stop right away. |

Distances are in **millimeters**; angles are in **degrees**.

### Changing speed for one move

The standard settings (from `robot_config.py`) are fast. For precise moves,
slow down, then restore the standard settings:

```python
DRIVE_BASE.settings(straight_speed=200, straight_acceleration=300)
await DRIVE_BASE.straight(130)       # slow and careful
await set_drivebase()                # back to normal speeds
```

The four settings are:

| Name | Meaning |
|---|---|
| `straight_speed` | Top speed driving straight (mm/s) |
| `straight_acceleration` | How quickly it speeds up and slows down (mm/s²) |
| `turn_rate` | Top turning speed (°/s) |
| `turn_acceleration` | How quickly turning speeds up and slows down (°/s²) |

Slower and gentler is almost always more accurate. If wheels slip, the
distance will be short. Lower the acceleration.

### The gyro

`use_gyro(True)` makes turns and straight lines follow the hub's gyro, so the
robot drives straighter and turns more precisely. Our runs turn it on at the
start and off at the end. If the gyro isn't set up with the right hub
orientation in the profile, turns will be wrong. See
[Hub orientation](CODE_GUIDE.md#robot-profiles-one-per-hub).

### What happens at the end of a move?

By default the robot **holds** its position when a move ends. Pass `then=` to
change that:

```python
from pybricks.parameters import Stop

await DRIVE_BASE.straight(300, then=Stop.COAST)   # roll to a stop, don't hold
```

| `then=` | Meaning |
|---|---|
| `Stop.HOLD` (default) | Stop and actively hold position |
| `Stop.BRAKE` | Brake, but allow it to be pushed |
| `Stop.COAST` | Let the motors spin freely |

`COAST` is handy for attachment motors, so they aren't fighting a mission
model after they've pushed it.

---

## Attachment commands

Attachment motors are `LEFT_ATTACHMENT` and `RIGHT_ATTACHMENT`:

```python
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

await LEFT_ATTACHMENT.run_angle(200, 90)
#                               │    └── turn 90 degrees
#                               └── at a speed of 200 degrees per second
```

- A **negative angle** turns the other way: `run_angle(200, -90)`.
- Add `then=Stop.COAST` to let go at the end.
- `speed` is how fast (always positive), `angle` is how far and which way.

### Tell the motor about its gears

If the motor reaches the model through gears, describe them at the start of
the run. Then the angles you write are the angles of the **final gear**:

```python
LEFT_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE, [12, 36])
RIGHT_ATTACHMENT.reconfigure(Direction.CLOCKWISE, None)    # no gears
```

How to write the gear list is in the
[Code Guide](CODE_GUIDE.md#attachments-and-gears-gear_swap_motorpy).

> Always call `reconfigure()` for each attachment you use at the beginning of
> your run. Another run might have left it set up for different gears.

### Check for missing attachments

`LEFT_ATTACHMENT` is `None` if the profile does not define it. If your run
uses it on a robot without it, you will get an error like
`AttributeError: 'NoneType' object has no attribute 'run_angle'`. That means
the profile is missing the attachment.

---

## Doing two things at once

To drive and move an attachment at the same time, use `multitask`. It starts
everything inside it together and continues when **all** of them are done:

```python
from pybricks.tools import multitask

await multitask(
    DRIVE_BASE.straight(200),
    LEFT_ATTACHMENT.run_angle(300, 90),
)
```

This saves time, which matters in a 2.5-minute match. Notes:

- Put a comma after each item. Don't write `await` inside the `multitask(...)`
  — just `await multitask(...)` outside.
- Both items finish before the next line runs.
- Don't make two items control the same motor.

---

## Using the color sensors

```python
from robot_config import LEFT_COLOR_SENSOR
from pybricks.parameters import Color

color = await LEFT_COLOR_SENSOR.color()
if color == Color.RED:
    print("Found red")
```

Use `color_test.py` first to see what colors the sensor sees on your mats.
See the `depreciated/run_demo_5_color_sensors.py` file for a longer example
(note it uses an older robot config).

---

## Organizing a long run

A run with 30 lines of moves is hard to read and hard to fix. Split it into
small functions with names that say what they do:

```python
from pybricks.parameters import Direction
from pybricks.tools import run_task

from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT


async def drive_to_mission():
    await DRIVE_BASE.straight(615)
    await DRIVE_BASE.turn(42)

async def lift_arm():
    await LEFT_ATTACHMENT.run_angle(300, 115)

async def run_m2():
    DRIVE_BASE.use_gyro(True)
    await set_drivebase()
    LEFT_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE, [12, 36])

    await drive_to_mission()
    await lift_arm()
    await DRIVE_BASE.straight(-615)       # back home

    DRIVE_BASE.use_gyro(False)


if __name__ == "__main__":
    run_task(run_m2())
```

Habits that help:

- **Define one function for each attachment movement**, then call them from
  the driving path at the right waypoints.
- **Comment what the move is for**, e.g. `# approach the lifting mission`.
  Numbers like `615` mean nothing a week later.
- **Print as you go** (`print("Turning left")`) so you can see where a run was
  when something went wrong.
- Keep robot moves **inside functions**, not at the top level of the file.
  Anything at the top level runs the instant the file is imported by
  `robot.py`.

---

## Tuning your run

No run works the first time. Change **one thing at a time**, re-run, and
write down what you learned.

1. **Same start every time.** Start in exactly the same place with the same
   alignment (use jigs or the launch area edge). If the start varies, nothing
   else can be trusted.
2. **Measure the first leg.** Is the robot short or long? Adjust the distance
   and try again.
3. **Then the turn.** Adjust the angle a few degrees at a time.
4. **Then the mission.** Tune the attachment angles one by one.
5. **Slow down if it's inconsistent.** If the same run gives different results,
   lower the speed and acceleration for the part that varies.
6. **Check the basics.** Is the battery charged? Are the wheels clean? Is
   the hub fixed firmly? Low battery changes motor behavior.

If distances are always off by the same percent, the wheel diameter in the
profile is probably wrong. Run `TestRun.py` and measure what the robot
actually does (see
[Testing](TESTING_AND_TROUBLESHOOTING.md#testrunpy--calibrating-the-wheel-size)).

---

## Adding your run to the menu

When your run works on its own, add it to `robot.py` so you can start it
from the hub buttons without a laptop.

1. Open `robot.py`.
2. Add an import at the top, next to the other imports:

   ```python
   from M2_Example import run_m2
   ```

3. In `main()`, find the line `# await add_program(run1, '1', Color.GREEN)`
   and add a line for your run before `await user_interface()`:

   ```python
   await add_program(run_m2, '2', Color.WHITE)
   ```

   The three values are the run function (no parentheses), the character to
   show on the hub, and the light color. Pick the color to match the color
   marker on the attachment, so it's obvious at the table which attachment
   goes with which run. Runs show up in the menu in the order you add them.

4. Run `robot.py` (open it and press **F5**). The hub shows your run's
   letter. Use the left and right buttons to select it, and the center
   button to start.

> Note that `M1_DroneSurvey.py` names its function `main`. To register it, either
> rename the function (e.g. `run_m1`) in the file and the bottom block, or
> import it under another name:
> `from M1_DroneSurvey import main as run_m1`.

---

## Sharing your run with the team

Save your work with Git as described in the
[Developer Setup Guide](SETUP.md#6-daily-workflow): pull → make a branch →
commit → push → open a pull request.

- `.vscode/` and `__pycache__/` are already ignored by Git, so your personal
  hub name won't be shared.
- Runs are shared by every robot, but each robot loads its own profile (by
  hub name). Distances that depend on wheel size or turns that depend on the
  axle track will differ between robots, so test a run on the robot it is for.
- Write a short, clear commit message, e.g. `Add M2 run for lifting
  mission`.

---

## Quick checklist before competition

- [ ] The run works from `robot.py`'s menu, not only from F5.
- [ ] Every attachment is `reconfigure()`d at the start of the run.
- [ ] Every run starts with `use_gyro(True)` and `await set_drivebase()`.
- [ ] No leftover test code, `return` lines, or commented-out debug moves
      that you don't intend.
- [ ] Each run's letter and color match the attachment marker.
- [ ] The hub is fully charged, and `robot.py` is the program on the hub.
- [ ] You have run the whole match in order at least three times.
