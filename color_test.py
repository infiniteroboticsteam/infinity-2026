from pybricks.parameters import Button, Color
from pybricks.tools import run_task, wait

from robot_config import HUB, HUB_NAME, LEFT_COLOR_SENSOR, PROFILE_NAME, RIGHT_COLOR_SENSOR

# Shows what the color sensors see, so you can slide colored mats or paper
# under the robot and check the readings.
#   Left button:   show the left sensor on the hub
#   Right button:  show the right sensor on the hub
#   Center button: stop the program
# The selected sensor's color is shown as a letter on the light matrix and as
# the hub's button light color. Every change on either sensor is printed.

# Colors the sensor detects by default, and the letter shown for each on the
# hub's light matrix.
COLOR_NAMES = [
    (Color.RED, "RED", "R"),
    (Color.YELLOW, "YELLOW", "Y"),
    (Color.GREEN, "GREEN", "G"),
    (Color.BLUE, "BLUE", "B"),
    (Color.WHITE, "WHITE", "W"),
    (Color.NONE, "NONE", "-"),
]

def describe_color(color):
    for known, name, letter in COLOR_NAMES:
        if color == known:
            return name, letter
    return str(color), "?"

def show_on_hub(color, letter):
    HUB.display.char(letter)
    if color == Color.NONE:
        HUB.light.off()
    else:
        HUB.light.on(color)

async def color_test(read_ms=100):
    print("Color test for hub", HUB_NAME, "using profile", PROFILE_NAME)
    sensors = {"Left": LEFT_COLOR_SENSOR, "Right": RIGHT_COLOR_SENSOR}
    for name, sensor in sensors.items():
        if sensor is None:
            print(name, "color sensor: not in profile, skipped")
    sensors = {name: sensor for name, sensor in sensors.items() if sensor is not None}
    if not sensors:
        print("No color sensors in profile")
        return

    for sensor in sensors.values():
        await sensor.lights.on(100)

    selected = "Left" if "Left" in sensors else "Right"
    print("Showing", selected, "sensor. Left/right button to switch, center to stop.")
    last_names = {}
    while True:
        pressed = HUB.buttons.pressed()
        if Button.LEFT in pressed and "Left" in sensors:
            selected = "Left"
        elif Button.RIGHT in pressed and "Right" in sensors:
            selected = "Right"

        for name, sensor in sensors.items():
            color = await sensor.color()
            color_name, letter = describe_color(color)
            if color_name != last_names.get(name):
                print(name, "color sensor sees", color_name)
                last_names[name] = color_name
            if name == selected:
                show_on_hub(color, letter)
        await wait(read_ms)


if __name__ == "__main__":
    run_task(color_test())
