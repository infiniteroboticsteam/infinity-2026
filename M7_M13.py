from pybricks.tools import multitask, run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def M7_M13():
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=300,
		straight_acceleration=500,
		turn_rate=600,
		turn_acceleration=600,
	)
	DRIVE_BASE.use_gyro(True)
	
	#await DRIVE_BASE.straight(100)
	
	await DRIVE_BASE.curve(280,92)
	#await DRIVE_BASE.straight(370)
	
	#await DRIVE_BASE.turn(32 )
	#await DRIVE_BASE.straight(270)
	
	await DRIVE_BASE.straight(570)
	
	await DRIVE_BASE.straight(-200)
	await DRIVE_BASE.turn(20)
	await DRIVE_BASE.straight(150)
	
	await multitask(
		LEFT_ATTACHMENT.run_target(360, 50),
		RIGHT_ATTACHMENT.run_target(360, 40),
		DRIVE_BASE.arc(800,-90),
	)
	#await DRIVE_BASE.straight(-340)
	#await DRIVE_RIGHT.run_angle(300,360)
	#await DRIVE_BASE.turn(-25)
	#await DRIVE_BASE.straight(-200)
	# await DRIVE_BASE.curve(-500,30)
	
if __name__ == "__main__":
	run_task(M7_M13())
