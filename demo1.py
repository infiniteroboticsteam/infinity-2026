from pybricks.parameters import Stop
from pybricks.tools import run_task, wait

from library import set_drivebase
from robot_config import (DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, HUB,
                          LEFT_ATTACHMENT, LEFT_COLOR_SENSOR, RIGHT_COLOR_SENSOR)

# Reflection below this number counts as "on the black line".
# Measure it on your mat: print reflection() over black and over white,
# then use the number halfway between them.
BLACK = 50


async def print_reflection():
    """Prints both sensor readings so you can find the BLACK threshold"""
    left = await LEFT_COLOR_SENSOR.reflection()
    right = await RIGHT_COLOR_SENSOR.reflection()
    print("left:", left, " right:", right)


async def drive_to_line(speed=150, black=BLACK):
    """Drives forward until the left sensor sees the black line, then stops.
    The gyro keeps the robot driving straight on the way there."""
    DRIVE_BASE.drive(speed, 0)
    while await LEFT_COLOR_SENSOR.reflection() > black:
        await wait(5)
    DRIVE_BASE.stop()


async def square_on_line(speed=100, black=BLACK):
    """Drives each wheel forward until its own sensor sees the line.
    When both stop, the robot is facing straight at the line.
    Then the gyro is reset to 0, so later turns start from a known angle."""
    DRIVE_BASE.stop()
    DRIVE_LEFT.run(speed)
    DRIVE_RIGHT.run(speed)
    left_done = False
    right_done = False
    while not (left_done and right_done):
        if not left_done and await LEFT_COLOR_SENSOR.reflection() < black:
            DRIVE_LEFT.hold()
            left_done = True
        if not right_done and await RIGHT_COLOR_SENSOR.reflection() < black:
            DRIVE_RIGHT.hold()
            right_done = True
        await wait(5)
    await wait(200)
    HUB.imu.reset_heading(0)
    DRIVE_BASE.reset()


async def turn_to_heading(target):
    """Uses the gyro to turn to an exact heading (0 = facing the squared line).
    Unlike turn(), this fixes any error left over from earlier moves."""
    await DRIVE_BASE.turn(target - HUB.imu.heading())


async def follow_line(distance_mm, speed=150, target=BLACK, gain=1.2):
    """Follows the edge of a line with the left sensor for distance_mm.
    Start with the sensor on the edge of the line (half black, half white).
    Wiggles too much: lower gain. Drifts off: raise gain. Steers wrong way: use -gain."""
    DRIVE_BASE.reset()
    while abs(DRIVE_BASE.distance()) < distance_mm:
        error = await LEFT_COLOR_SENSOR.reflection() - target
        DRIVE_BASE.drive(speed, gain * error)
        await wait(5)
    DRIVE_BASE.stop()


async def demo1():
    """Demo run: find a line, square up on it, then use the gyro and an
    attachment motor from that known position."""
    await set_drivebase()
    DRIVE_BASE.use_gyro(True)
    await print_reflection()

    print("Driving to the line")
    await drive_to_line()

    print("Backing up and squaring on the line")
    await DRIVE_BASE.straight(-40)
    await square_on_line()
    print("Squared. Heading reset to", HUB.imu.heading())

    print("Moving the left attachment")
    await LEFT_ATTACHMENT.run_angle(300, 90)
    await LEFT_ATTACHMENT.run_angle(300, -90, then=Stop.COAST)

    print("Turning to heading 90 with the gyro")
    await DRIVE_BASE.straight(-50)
    await turn_to_heading(90)
    await DRIVE_BASE.straight(150)

    print("Turning back to heading 0 and returning")
    await turn_to_heading(0)
    await DRIVE_BASE.straight(-150)

    DRIVE_BASE.use_gyro(False)
    print("Done")


if __name__ == "__main__":
    run_task(demo1())
