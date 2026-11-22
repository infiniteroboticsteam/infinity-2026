from pybricks.tools import multitask, run_task, wait
from pybricks.parameters import Stop
from library import set_drivebase
from robot_config import DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT

async def M1_M2():
	DRIVE_BASE.use_gyro(True)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=400,
		straight_acceleration=200,
		turn_rate=600,
		turn_acceleration=600,
	)
	
	print("Driving forward 680 mm while moving the attachment")
	await multitask(
		LEFT_ATTACHMENT.run_angle(180, 127),
		DRIVE_BASE.straight(657),
	)
	
	print("Turning 20 degrees")
	await DRIVE_RIGHT.run_angle(360, 285)
	
	print("Turning 55 degrees Completed")
	
	await DRIVE_BASE.turn(40)

	print("Turning 40 degrees back Completed")
	
	await DRIVE_BASE.curve(-1600, -19.5)
	print("Turning -55 degrees back Completed")
	 
	set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=500,
		straight_acceleration=600,
		turn_rate=200,
		turn_acceleration=300,
	)
	print("Driving backward 514 mm toward the next task")
	#await DRIVE_BASE.straight(-575)
	
	#await DRIVE_BASE.turn(-50.5)
	await DRIVE_BASE.turn(-58.5)
	await LEFT_ATTACHMENT.run_angle(-180, 120)
	DRIVE_BASE.settings(
		straight_speed=500,
		straight_acceleration=600,
		turn_rate=200,
		turn_acceleration=200,
	)
	await DRIVE_BASE.straight(180)
	await multitask(
		LEFT_ATTACHMENT.run_angle(90, 18),
		DRIVE_BASE.straight(100),
	)
	await wait(500)
	DRIVE_BASE.settings(
		straight_speed=650,
		straight_acceleration=200,
		turn_rate=200,
		turn_acceleration=200,
	)
	await multitask(
		LEFT_ATTACHMENT.run_angle(160, 56),
		DRIVE_BASE.straight(-200),
	)

	await DRIVE_BASE.curve(-400, -60)
	#await DRIVE_BASE.straight(100)
	print("Return complete")
	
	
	

if __name__ == "__main__":
	run_task(M1_M2())