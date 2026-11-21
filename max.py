from pybricks.tools import run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def main():

	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=500,
		straight_acceleration=900,
		turn_rate=100,
		turn_acceleration=400,
	)
	DRIVE_BASE.use_gyro(True)
	#driving there
	#await DRIVE_BASE.arc(-500, 79)
	await DRIVE_BASE.arc(-500, 200)
	"""return
	await DRIVE_BASE.arc(90, 80)
	
	DRIVE_BASE.settings(
		straight_speed=700,
		straight_acceleration=900,
		turn_rate=100,
		turn_acceleration=400,
	)
	DRIVE_BASE.use_gyro(False)
	
	#ramming the tree
	await DRIVE_BASE.straight(700)
	await wait(500)
	
	#await DRIVE_BASE.straight(20)
	#await DRIVE_BASE.straight(-20)
	#await DRIVE_BASE.straight(20)
	#await DRIVE_BASE.straight(-20)
	#await DRIVE_BASE.straight(20)
	#await DRIVE_BASE.straight(-20)
	#await DRIVE_BASE.straight(20)
	#await DRIVE_BASE.straight(-20)
	#await DRIVE_BASE.straight(20)
	#await DRIVE_BASE.straight(-20)
	
		
	DRIVE_BASE.settings(
		straight_speed=750,
		straight_acceleration=750,
		turn_rate=100,
		turn_acceleration=400,
	)
	DRIVE_BASE.use_gyro(False)
    #driving to the window
	await DRIVE_BASE.straight(-200)
	#await DRIVE_BASE.arc(85,90)
	return
	#ramming the window
	await DRIVE_BASE.straight(-145)
	return
	DRIVE_BASE.settings(
		straight_speed=900,
		straight_acceleration=900,
		turn_rate=900,
		turn_acceleration=900,
	)
	#driving home
	await DRIVE_BASE.arc(180,40)
	await DRIVE_BASE.arc(-200,90)
	await DRIVE_BASE.straight(650)
	"""
if __name__ == "__main__":
	run_task(main()) 
