from pybricks.tools import multitask, run_task
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT


async def M2():
	DRIVE_BASE.use_gyro(True)
	await LEFT_ATTACHMENT.run_angle(180, -100)
	await DRIVE_BASE.straight(150)
	await DRIVE_BASE.straight(10)
if __name__ == "__main__":
	run_task(M2())
