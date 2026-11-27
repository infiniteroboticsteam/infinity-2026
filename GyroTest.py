from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Axis
from pybricks.robotics import DriveBase

# Match top_side and front_side to how your hub is mounted
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)

left_motor = Motor(Port.D, Direction.CLOCKWISE)
right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
drive_base.use_gyro(True)  # Required for gyro straight driving

drive_base.straight(500)
drive_base.straight(-500)