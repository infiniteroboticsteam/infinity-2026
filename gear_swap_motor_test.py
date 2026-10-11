from pybricks.parameters import Direction
from pybricks.tools import run_task, wait

from gear_swap_motor import calculate_simple_gear_ratio
from robot_config import LEFT_ATTACHMENT, RIGHT_ATTACHMENT, PROFILE_NAME

# Checks GearSwapMotor on the real robot with the real gears.
# Put a mark (tape or a pen line) on the FINAL gear, run this, and watch that
# the final gear turns the angle that is printed, not the motor.
# For the gear ratio math alone (no motor), use gear_swap_test.py.
#
# Edit GEAR_TESTS to match the gears you built. See calculate_simple_gear_ratio
# in gear_swap_motor.py for how to write a chain (ints) vs a compound gear
# ((in, out) tuples). The direction is trial and error: if the final gear turns
# the wrong way on the "+90" step, swap CLOCKWISE and COUNTERCLOCKWISE.

# attachment: LEFT_ATTACHMENT or RIGHT_ATTACHMENT (None entries are skipped)
# name:       label printed while testing
# direction:  the way a positive angle should turn the final gear
# gears:      motor gear first, final gear last
GEAR_TESTS = [
    {"name": "no gears", "attachment": LEFT_ATTACHMENT,
     "direction": Direction.CLOCKWISE, "gears": None},
    {"name": "12T -> 36T chain", "attachment": LEFT_ATTACHMENT,
     "direction": Direction.CLOCKWISE, "gears": [12, 36]},
    {"name": "12T -> 36T chain", "attachment": RIGHT_ATTACHMENT,
     "direction": Direction.CLOCKWISE, "gears": [12, 36]},
    {"name": "12T -> (36)", "attachment": LEFT_ATTACHMENT,
     "direction": Direction.CLOCKWISE, "gears": [8, (24, 8), 40]},
]

# Final gear angles to turn, in order. They add up to 0, so the mark on the
# final gear should be back where it started at the end of each test.
TARGET_ANGLES = [90, 360, -90, -360]

# Final gear speed in deg/s. The motor runs at SPEED * ratio, so keep
# SPEED * ratio below about 1000 for big ratios.
SPEED = 90
PAUSE_MS = 1500


async def run_gear_test(test):
    motor = test["attachment"]
    name = test["name"]
    if motor is None:
        print(name, ": attachment not in profile, skipped")
        return

    ratio = calculate_simple_gear_ratio(test["gears"])
    print("")
    print("==", name, "==")
    print("gears", test["gears"], "ratio", ratio)
    print("final gear speed", SPEED, "deg/s -> motor speed", SPEED * ratio, "deg/s")

    motor.reconfigure(test["direction"], test["gears"])
    motor.reset_angle(0)

    for target in TARGET_ANGLES:
        print("final gear", target, "deg -> motor should turn", target * ratio, "deg")
        await motor.run_angle(SPEED, target, reset_angle=False)
        print("  motor angle now", motor.angle(), "deg (starts at 0 and should end at 0)")
        await wait(PAUSE_MS)

    print("done: the mark on the final gear should be back at the start")

async def gear_motor_test():
    print("Gear motor test, profile", PROFILE_NAME)
    await run_gear_test(GEAR_TESTS[1])
    await run_gear_test(GEAR_TESTS[2])
    #for test in GEAR_TESTS[]:
    #    await run_gear_test(test)
    print("Gear motor test done")


if __name__ == "__main__":
    run_task(gear_motor_test())
