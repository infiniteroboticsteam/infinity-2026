from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

from gear_swap_motor import GearSwapMotor, calculate_simple_gear_ratio
from robot_profiles import DEFAULT_PROFILE, PROFILES

# Initialize variables.
SPEED = 700
ACCELERATION = 700
TURN_SPEED = 700
TURN_ACCELERATION = 700

# Pick the profile for this hub. Ports, directions and hub orientation live in
# robot_profiles.py, one profile per hub.
HUB_NAME = PrimeHub().system.name()

if HUB_NAME in PROFILES:
    PROFILE_NAME = HUB_NAME
else:
    PROFILE_NAME = DEFAULT_PROFILE
    print("No profile for hub", HUB_NAME, "- using", DEFAULT_PROFILE)
print("Loading robot profile:", PROFILE_NAME)
PROFILE = PROFILES[PROFILE_NAME]

# Set up the hub. The orientation can only be set when the hub is created,
# so it is created again now that the profile is known.
HUB = PrimeHub(top_side=PROFILE["hub_top_side"], front_side=PROFILE["hub_front_side"])

# Set up the drive base.
DRIVE_LEFT = Motor(PROFILE["drive_left"]["port"], PROFILE["drive_left"]["direction"])
DRIVE_RIGHT = Motor(PROFILE["drive_right"]["port"], PROFILE["drive_right"]["direction"])
DRIVE_BASE = DriveBase(DRIVE_LEFT, DRIVE_RIGHT,
                       PROFILE["wheel_diameter"], PROFILE["axle_track"])

# Set up the attachments and sensors; missing ones are None.
def _gear_swap_motor(key):
    config = PROFILE.get(key)
    return GearSwapMotor(config["port"], config["direction"]) if config else None

def _color_sensor(key):
    port = PROFILE.get(key)
    return ColorSensor(port) if port else None

LEFT_ATTACHMENT = _gear_swap_motor("left_attachment")
RIGHT_ATTACHMENT = _gear_swap_motor("right_attachment")

# default configuration: no gears
# you can change the configuration in your program, e.g.,
# LEFT_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE, [12, 36])
# after changing the configuration, you may want to reset the angle
# LEFT_ATTACHMENT.reset_angle(0)

LEFT_COLOR_SENSOR = _color_sensor("left_color_sensor")
RIGHT_COLOR_SENSOR = _color_sensor("right_color_sensor")

#bl = HUB.battery.level()
#print(f"Battery Level: {level}%")
