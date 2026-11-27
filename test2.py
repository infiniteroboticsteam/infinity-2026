from pybricks.tools import run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def main():
	DRIVE_BASE.use_gyro(False)
	await set_drivebase()

	#print("Driving forward 100 mm")
	DRIVE_BASE.settings(
		straight_speed=700,
		straight_acceleration=900,
		turn_rate=100,
		turn_acceleration=400,
	)
	await DRIVE_BASE.straight(-600)
	await wait(500)

if __name__ == "__main__":
	run_task(main()) 
