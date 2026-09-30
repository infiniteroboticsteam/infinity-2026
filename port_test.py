from pybricks.parameters import Direction
from pybricks.tools import run_task, wait

from robot_config import (DRIVE_BASE, HUB_NAME, LEFT_ATTACHMENT, LEFT_COLOR_SENSOR,
                          PROFILE_NAME, RIGHT_ATTACHMENT, RIGHT_COLOR_SENSOR)

# Checks that the profile in robot_profiles.py matches the connected robot.
# Run it with the robot on the floor and watch that each step moves the right part.

async def test_drive_base():
    DRIVE_BASE.settings(straight_speed=200, straight_acceleration=300,
                        turn_rate=100, turn_acceleration=300)
    print("Drive: forward 50 mm")
    await DRIVE_BASE.straight(50)
    print("Drive: turn right 90 degrees")
    await DRIVE_BASE.turn(90)
    print("Drive: forward 50 mm")
    await DRIVE_BASE.straight(50)

    # Retrace the path in reverse to end where we started, facing the same way.
    print("Drive: returning to start")
    await DRIVE_BASE.straight(-50)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(-50)

async def test_attachment(name, motor, direction):
    if motor is None:
        print(name, "attachment: not in profile, skipped")
        return
    # reconfigure() makes positive angles turn in `direction`, whatever the
    # motor's direction is in the profile.
    motor.reconfigure(direction, None)
    print(name, "attachment: 360 degrees", direction, "at 180 deg/s")
    await motor.run_angle(180, 360)

async def test_color_sensor(name, sensor, seconds=3, blink_ms=250):
    if sensor is None:
        print(name, "color sensor: not in profile, skipped")
        return
    # Flashes the sensor's lights to show which port it is on.
    # To check color readings, use color_test.py.
    print(name, "color sensor: flashing for", seconds, "seconds")
    for _ in range(seconds * 1000 // (2 * blink_ms)):
        await sensor.lights.on(100)
        await wait(blink_ms)
        await sensor.lights.off()
        await wait(blink_ms)

async def port_test():
    print("Port test for hub", HUB_NAME, "using profile", PROFILE_NAME)
    await test_drive_base()
    await test_attachment("Left", LEFT_ATTACHMENT, Direction.CLOCKWISE)
    await test_attachment("Right", RIGHT_ATTACHMENT, Direction.COUNTERCLOCKWISE)
    await test_color_sensor("Left", LEFT_COLOR_SENSOR)
    await test_color_sensor("Right", RIGHT_COLOR_SENSOR)
    print("Port test done")


if __name__ == "__main__":
    run_task(port_test())
