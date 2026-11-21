# Python Basics for Robot Programmers

You do **not** need to know Python before you start. This page teaches only
the parts of Python that our robot code uses, with robot examples. Read it
once from top to bottom, then come back to look things up.

Our robot runs **MicroPython** (a small version of Python) with the
**Pybricks** library. Everything here works on the hub.

> **Tip:** The best way to learn is to change a number, run the program, and
> see what the robot does. You cannot break anything by editing code — Git
> remembers every version.

---

## 1. Printing messages

`print()` shows a message in the VS Code terminal while the program runs. Use
it all the time to see what your robot is doing.

```python
print("Driving forward")
print("Battery level is", 85)
```

Text goes inside quotes `" "`. You can print several things separated by
commas.

---

## 2. Comments

A line starting with `#` is a **comment**. The robot ignores it. Comments are
notes for humans.

```python
# This line is only a note
await DRIVE_BASE.straight(500)   # a note can go at the end of a line too
```

You can also "comment out" a line to turn it off without deleting it:

```python
#await DRIVE_BASE.turn(90)
```

In VS Code, select lines and press `Ctrl+/` (`Cmd+/` on Mac) to comment or
uncomment them.

---

## 3. Variables

A **variable** is a name that stores a value.

```python
SPEED = 700          # a whole number
WHEEL_DIAMETER = 56  # millimeters
hub_name = "infinite-1"   # text
is_ready = True      # True or False
```

- Use `=` to **store** a value. `SPEED = 700` means "SPEED is 700".
- Names are case-sensitive: `speed` and `SPEED` are different.
- Names can't have spaces. Use underscores: `turn_speed`.
- By team habit, values that never change are written in `CAPITAL_LETTERS`
  (like `SPEED`, `DRIVE_BASE`).

You can do math with numbers:

```python
distance = 600 + 130      # 730
half = distance / 2       # 365.0
doubled = distance * 2    # 1460
```

---

## 4. Indentation matters!

Python uses **spaces at the start of a line** to know which lines belong
together. This is the number-one thing that trips up beginners.

```python
async def run1():                      # the function starts here
    await DRIVE_BASE.straight(500)     # 4 spaces: inside the function
    await DRIVE_BASE.turn(90)          # 4 spaces: still inside
print("done")                          # 0 spaces: NOT inside the function
```

Rules:

- Use **4 spaces** for each level. VS Code adds them when you press `Tab`.
- Every line in the same block must be indented the same amount.
- **Never mix tabs and spaces in one file.** It looks the same on screen but
  Python reports an error. (A few older files in this repo, like
  `M1_DroneSurvey.py`, use tabs. If you edit one, keep using tabs in that
  file. For new files, use 4 spaces.)

---

## 5. Functions

A **function** is a named group of instructions. You *define* it once, then
*call* it whenever you want it to run.

```python
def say_hello():          # define: "def", a name, (), and a colon
    print("Hello")        # the body is indented

say_hello()               # call: name followed by ()
```

Functions can take **inputs** (called *arguments* or *parameters*):

```python
def add(a, b):
    return a + b          # "return" hands a result back

total = add(2, 3)         # total is 5
```

On the robot you call functions from the Pybricks library all the time:

```python
DRIVE_BASE.straight(500)       # function with one argument: 500 mm
motor.run_angle(200, 90)       # two arguments: speed, then angle
```

The order of arguments matters. You can also name them to make it clearer:

```python
motor.run_angle(speed=200, rotation_angle=90)
```

---

## 6. `async` and `await` — how the robot does things

Robot actions take time. Driving 500 mm takes a couple of seconds. Our code
uses **async functions** so that the robot can do more than one thing at the
same time (for example, drive *and* lift an arm).

You only need two rules:

1. A function that does robot actions is written with `async def`:

   ```python
   async def run1():
       ...
   ```

2. Put `await` in front of anything that takes time, and wait for it to
   finish before going to the next line:

   ```python
   async def run1():
       await DRIVE_BASE.straight(500)   # drive, and WAIT until done
       await DRIVE_BASE.turn(90)        # then turn, and WAIT until done
       await wait(1000)                 # then pause 1000 ms (1 second)
   ```

**If you forget `await`**, the line starts the action but does not wait, and
the next line runs immediately. The robot may skip moves or act strangely.
When something seems to be ignored, check for a missing `await`.

**You can only use `await` inside an `async def` function.**

### Starting an async function

A normal program calls `my_function()`. An `async` function needs a helper
called `run_task`. At the bottom of each run file you will see:

```python
if __name__ == "__main__":
    run_task(run1())
```

This means: "if I am running this file directly (pressing F5), start `run1`."
When `robot.py` imports the file instead, this block is skipped, so the run
only starts when you pick it from the hub menu. Copy this block exactly.

### Doing two things at once: `multitask`

```python
await multitask(
    arm_motor.run_angle(300, 90),
    DRIVE_BASE.straight(200),
)
```

Both actions start together, and the code continues when **both** are done.
See [Writing Runs](WRITING_RUNS.md#doing-two-things-at-once).

---

## 7. `if` and `else` — making decisions

```python
if color == Color.RED:
    print("I see red")
elif color == Color.GREEN:
    print("I see green")
else:
    print("I see something else")
```

- `==` **compares** two values ("is equal to"). A single `=` stores a value.
- Other comparisons: `!=` (not equal), `<`, `>`, `<=`, `>=`.
- Combine with `and`, `or`, `not`.
- `in` checks whether something is in a collection:
  `if Button.LEFT in buttons:`

---

## 8. Loops — repeating things

**`for` loop** — repeat a fixed number of times:

```python
for i in range(4):               # 4 times: i is 0, 1, 2, 3
    await DRIVE_BASE.straight(200)
    await DRIVE_BASE.turn(90)    # drives a square
```

**`while` loop** — repeat as long as something is true:

```python
while True:                      # forever
    print("hello")
    await wait(1000)
```

> **Always put an `await wait(...)` inside a `while True` loop** in async
> code. Without it, nothing else (like button checks) gets a turn to run.

Use `break` to leave a loop early.

---

## 9. Lists, tuples, and dictionaries

These hold several values in one variable. You will see all three in our code.

**List** `[ ]` — an ordered collection:

```python
gears = [12, 36]                 # a list of two numbers
print(gears[0])                  # 12 (counting starts at 0!)
print(len(gears))                # 2
```

**Tuple** `( )` — like a list but fixed. We use one for a pair of gears fixed
to the same axle: `(24, 8)`.

**Dictionary** `{ }` — pairs of a *key* and a *value*, like a real dictionary
looks up a word to get its meaning:

```python
robot = {
    "wheel_diameter": 56,
    "axle_track": 114,
}
print(robot["wheel_diameter"])   # 56
```

`robot_profiles.py` is a dictionary that holds the settings for each robot.

---

## 10. Importing code from other files

`import` lets one file use code from another so we do not copy and paste.

```python
from library import set_drivebase
from robot_config import DRIVE_BASE, HUB
```

This reads as: "from the file `library.py`, bring in `set_drivebase`."
(Leave off the `.py`.)

Rules for our project:

- **Keep all your files in the main folder** (the repo root), next to
  `robot_config.py`. The tool that sends code to the hub only sends the file
  you run plus the files it imports from the *same folder*. Files in
  subfolders will not be found on the hub.
- A file must exist and have the exact name (capital letters count).
- Don't put robot moves at the top of a file outside a function — they would
  run the moment the file is imported! Put moves inside `async def`
  functions.

The `pybricks` imports you will see:

| Import | What it gives you |
|---|---|
| `from pybricks.tools import wait, multitask, run_task` | pause, run things together, start a program |
| `from pybricks.parameters import Color, Direction, Stop, Port, Button` | named constants |
| `from pybricks.pupdevices import Motor, ColorSensor` | motors and sensors |
| `from pybricks.robotics import DriveBase` | the two-wheel drive system |
| `from pybricks.hubs import PrimeHub` | the hub itself |

VS Code can add imports for you: start typing a name, and press `Enter` on
the suggestion.

---

## 11. Classes and objects (just enough)

An **object** is a thing with its own data and its own functions. A `Motor` is
an object: it knows its port and its angle, and it has functions like
`run_angle`. You use a dot to reach inside:

```python
LEFT_ATTACHMENT.run_angle(200, 90)   # object . function ( arguments )
LEFT_ATTACHMENT.angle()              # ask the motor where it is
```

You do not need to write classes to make runs. `gear_swap_motor.py` defines
one (`GearSwapMotor`) if you are curious.

---

## 12. Reading error messages

When something goes wrong, Python prints an error in the terminal. Read it
from the **bottom up**. The last line says what went wrong, and a line above it
says which file and line number.

```
Traceback (most recent call last):
  File "run7.py", line 12, in run7
NameError: name 'DRIVE_BAS' isn't defined
```

| Error | Usually means |
|---|---|
| `SyntaxError` | A typo: missing `:` `)` or quote |
| `IndentationError` | Lines not lined up (see section 4) |
| `NameError` | A name was misspelled, or not imported |
| `ImportError` | The file or the name you imported does not exist |
| `AttributeError` | You used a function name that the object does not have |
| `TypeError` | Wrong number or type of arguments |
| `OSError: [Errno 19] ENODEV` | A motor or sensor is not plugged into the port the profile expects |

More in [Testing and Troubleshooting](TESTING_AND_TROUBLESHOOTING.md).

---

## 13. Cheat sheet

```python
# --- Imports (top of file) ---
from pybricks.parameters import Color, Direction, Stop
from pybricks.tools import multitask, run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT

# --- A run ---
async def run_example():
    DRIVE_BASE.use_gyro(True)               # more accurate turns
    await set_drivebase()                    # our speed settings
    await DRIVE_BASE.straight(500)          # forward 500 mm
    await DRIVE_BASE.turn(90)               # turn right 90 degrees
    await LEFT_ATTACHMENT.run_angle(300, 180)  # speed 300, turn 180 degrees
    await wait(500)                         # pause half a second
    await DRIVE_BASE.straight(-500)         # backward
    DRIVE_BASE.use_gyro(False)

# --- Starter (bottom of file) ---
if __name__ == "__main__":
    run_task(run_example())
```

Continue with [Code Guide](CODE_GUIDE.md) to see how the project fits
together.
