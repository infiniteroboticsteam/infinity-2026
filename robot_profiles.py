from pybricks.parameters import Axis, Direction, Port

# One profile per hub, keyed by the hub name you chose when installing the
# Pybricks firmware (the same name used in .vscode/launch.json).
# robot_config.py reads the connected hub's name and loads the matching profile.
#
# To add your robot: copy the "infinite-1" entry, rename the key to your hub
# name, and change the values to match your robot.
#
# hub_top_side / hub_front_side: which side of the hub faces up, and which
# faces the robot's driving direction. Sides use the hub's own axes: top is
# Axis.Z, front is Axis.X, left is Axis.Y; a minus sign means the opposite side
# (e.g. -Axis.X is the back). The gyro turns around hub_top_side, so it must be
# right for accurate turns.
#
# Each motor has a port and a default rotation direction: the way the motor
# turns for a positive speed or angle. Color sensors only need a port.
# Leave out any attachment or sensor your robot doesn't have (or set it to
# None); it will be None in robot_config.

PROFILES = {
    # coach chao's robot
    "infinite-1": {
        "hub_top_side": Axis.Z,
        "hub_front_side": - Axis.Y,
        "wheel_diameter": 56,  # mm
        "axle_track": 114,     # mm
        "drive_left": {"port": Port.C, "direction": Direction.COUNTERCLOCKWISE},
        "drive_right": {"port": Port.D, "direction": Direction.CLOCKWISE},
        "left_attachment": {"port": Port.A, "direction": Direction.COUNTERCLOCKWISE},
        "right_attachment": {"port": Port.B, "direction": Direction.COUNTERCLOCKWISE},
        "left_color_sensor": Port.E,
        "right_color_sensor": Port.F,
    },
}

# Used when the connected hub's name isn't listed above.
DEFAULT_PROFILE = "infinite-1"
