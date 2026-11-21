# Testing and Troubleshooting

How to check that the robot and the code agree with each other, and what to do
when something goes wrong.

To run any script below: connect to the hub (see
[Getting Started](GETTING_STARTED.md#5-run-your-first-program)), open the file
in VS Code, and press **F5**. Watch the robot **and** the VS Code terminal.

> **Safety:** the first time you run a test on a new robot, hold it in the air
> or put it on a stand so the wheels can spin freely. Keep hands and fingers
> away from gears and wheels while a program is running.

---

## The test scripts

### `port_test.py` — does the profile match the robot?

Run this **first** on any new robot, and again any time you rewire or rebuild.
It uses your hub's profile and tries each part in turn:

1. **Drive base:** forward 50 mm, turn right 90°, forward 50 mm, then
   retraces the path in reverse. Put the robot on the floor with space around
   it.
2. **Left attachment:** turns 360° clockwise.
3. **Right attachment:** turns 360° counterclockwise.
4. **Left, then right color sensor:** flash their lights for 3 seconds.

Things to check:

- Did the **right motor** move at each step? If the left attachment moved
  when the right was supposed to, the ports are swapped in the profile.
- Did the robot drive **forward** first, not backward? If it went backward,
  flip the direction of **both** drive motors in `robot_profiles.py`.
  If it spun in place, only one drive motor is flipped.
- Did the 90° turn go **right** (clockwise, seen from above)? If the robot
  drove forward correctly but turned left, the left and right drive motors
  are swapped: swap `drive_left` and `drive_right` ports in the profile.
- Did the **correct sensor** flash?
- Parts missing from the profile print `skipped` instead of running.

The first line of output tells you which hub and profile it used:
`Port test for hub infinite-1 using profile infinite-1`. If the profile is
not the one you expected, your hub name and the profile key don't match.

### `detect_port.py` — what is plugged into each port?

Use this when you aren't sure what's connected where. It checks ports A to F:
every motor turns two full rotations and every color sensor flashes three
times, and the terminal prints which port is which. Empty ports print
`EMPTY OR UNSUPPORTED DEVICE`. This script doesn't use the profile, so it
works even before you have written one.

### `color_test.py` — what do the color sensors see?

Slide colored paper or a mission mat under the robot's sensors.

| Hub button | Action |
|---|---|
| Left | Show the left sensor |
| Right | Show the right sensor |
| Center | Stop |

The hub's display shows a letter (`R` red, `Y` yellow, `G` green, `B` blue,
`W` white, `-` nothing) and its light shows the color. Every change is also
printed. Use this to find out how the sensor reads the colors on **your**
competition mat, in the light of **your** room.

### `gear_swap_test.py` — is the gear ratio math right?

Needs no motor. It prints `PASS` or `FAIL` for each ratio case and shows how
far the motor must turn for a 90° turn of the final gear. Run it after anyone
changes `gear_swap_motor.py`. Every line should say `PASS`.

### `gear_swap_motor_test.py` — do my real gears behave?

1. Put a bit of tape on the **final gear** (the one touching the mission
   model) as a mark.
2. Edit `GEAR_TESTS` in the file to describe the gears you built, and make
   `gear_motor_test()` run the test you want.
3. Run it. The final gear should turn 90°, 360°, back 90°, back 360°, and the
   mark should end where it started.

If the final gear turns the **wrong way**, swap `CLOCKWISE` and
`COUNTERCLOCKWISE` in the test. If the **distance** is wrong, recheck the gear
list (see [how to write it](CODE_GUIDE.md#how-to-write-the-gear-list)).

### `TestRun.py` — calibrating the wheel size

`TestRun.py` drives forward one wheel circumference (π × 56 mm ≈ 176 mm) and
back. Use it to check that the wheel size in your profile is right:

1. Put a tape mark at the front edge of the robot's wheels on the floor.
2. Run the program.
3. If the robot ended up exactly where it started, the profile is right.
4. If not, command a longer distance (for example change the number to
   `straight(1000)`), measure how far the robot **really** went, and compute:

   ```
   new wheel_diameter = old wheel_diameter × (real distance ÷ commanded distance)
   ```

   Example: you commanded 1000 mm but it went 980 mm →
   `56 × 980 ÷ 1000 = 54.9`. Put that value in `wheel_diameter` in
   `robot_profiles.py`.

Turns work the same way: command `turn(360)` without the gyro
(`use_gyro(False)`), see how far it really turned, and compute

```
new axle_track = old axle_track × (commanded angle ÷ real angle)
```

Measure the **real** wheel diameter with calipers or a ruler first; the
numbers are usually close, so only small corrections are needed.

(`TestRun.py` has its own `WHEEL_DIAMETER = 56` for the distance it
requests. If your wheels are a different size, update it there as well, but
the real size the robot *uses* comes from the profile.)

---

## Troubleshooting

### Connecting and running

**F5 does nothing, or VS Code asks me to pick a debugger**
- You need `.vscode/launch.json` — see
  [step 4.6 in Getting Started](GETTING_STARTED.md#4-set-up-vs-code).
- Make sure the file you want to run is the active tab.

**"Could not find hub" / it can't connect**
- Is the hub turned on, with the Bluetooth light blinking? Is the name in
  `launch.json` exactly the hub's name (capitals, dashes)?
- Is the hub already connected to something else (code.pybricks.com in a
  browser tab, or an old VS Code run)? Close those, then try again.
- Is Bluetooth on in your computer? Move closer to the hub.
- Turn the hub off and on.

**`pybricksdev` or `pip` is not found**
- You are probably not in the project's virtual environment. The terminal line
  should start with `(.venv)`. Use **Python: Create Terminal** from the
  Command Palette. If that fails, redo the steps in
  [Getting Started](GETTING_STARTED.md#4-set-up-vs-code).

**Windows: "running scripts is disabled on this system"**
- Do [step 3 of Getting Started](GETTING_STARTED.md#3-windows-only-allow-powershell-scripts).

**The hub shows a red `E` and the menu won't appear**
- The gyro isn't ready. Put the robot flat and still on the table for a few
  seconds. If it persists, turn the hub off and on while it sits still.

**I can't stop my program**
- Running a single file with F5: press the hub's center button or
  `Ctrl+C` in the terminal.
- Running `robot.py`: `ui.py` turns off the hub's stop button on purpose.
  Hold the center button to turn the hub off, then turn it on again.

### Errors when the program starts

**`No profile for hub X - using infinite-1`** (printed, not an error)
- Your hub's name isn't a key in `PROFILES` in `robot_profiles.py`. Add your
  profile ([how](CODE_GUIDE.md#adding-your-robot)) and make sure the name is
  spelled exactly the same.

**`OSError: [Errno 19] ENODEV`** (or similar "no device" error)
- The profile says there is a motor or sensor on a port, but the hub doesn't
  find one there. Check the cable is fully clicked in, and compare the
  profile to what's plugged in. `detect_port.py` shows you what's really
  connected.

**`ImportError: no module named 'xyz'`** or `cannot import name`
- The file doesn't exist in the main folder, the name is spelled differently,
  or that name was removed from `robot_config.py`. Archived code in
  `code_2025_unearthed/`, `advanced/`, and `depreciated/` uses old names
  (such as `CENTER_ATTACHMENT`) that no longer exist.
- Files in subfolders can't be imported on the hub. Move the file to the
  main folder.

**`AttributeError: 'NoneType' object has no attribute ...`**
- You used an attachment or sensor that isn't in the profile, so it is `None`.
  Add it to the profile or don't use it.

**`SyntaxError` / `IndentationError`**
- Look at the line number given, and also the line **above** it. Typical
  causes: missing `:` or `)`, or lines not lined up.
- Don't mix tabs and spaces within a file.

**An error about `await` or `async`, or a robot move that is silently skipped**
- A line is missing `await`, or `await` is used outside an `async def`.

### The robot does the wrong thing

| What you see | Likely cause |
|---|---|
| Drives backward when told forward | Drive motor `direction` values in the profile are flipped |
| Spins in place instead of driving straight | One drive motor direction is flipped |
| Always drives short or long by the same percentage | `wheel_diameter` in the profile is wrong |
| Turns too far or not far enough | Gyro off or `hub_top_side`/`hub_front_side` wrong; or `axle_track` wrong |
| Turns the wrong way | Flip sign of the angle (`turn(90)` is right, `turn(-90)` is left) |
| Different result each time | Start position varies; wheels slip (lower acceleration); battery is low |
| Wheels slip at the start | Acceleration too high: lower `ACCELERATION` or use `DRIVE_BASE.settings(...)` for that move |
| Attachment turns the wrong way | Direction in `reconfigure(...)` is flipped |
| Attachment turns too far or too little | Gear list is wrong (check compound gears), or speed × ratio too high |
| Attachment doesn't move at all, no error | Missing `await`, or the motor is blocked/stalled by the model |
| A move gets skipped | Missing `await` |
| Everything slows down or stutters | Low battery: charge the hub |
| Works with F5 but not from the menu | Run isn't registered in `robot.py`, or it changes settings and doesn't restore them (call `await set_drivebase()` at the start) |

### Still stuck?

1. Add `print()` lines to see how far the program got.
2. Make the problem smaller: run just one move and look at what happens.
3. Compare to a run that works.
4. Ask a teammate or coach and show them the **whole error message**, not just
   "it doesn't work".
5. Undo your changes with Git if you need to go back: see
   [SETUP.md](SETUP.md#6-daily-workflow) and ask a coach for help with
   `git restore`.

For Git and GitHub problems (SSH keys, "permission denied"), see the
[Troubleshooting section of the setup guide](SETUP.md#troubleshooting).
