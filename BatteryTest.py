
from pybricks.tools import run_task, wait

from robot_config import HUB


async def BatteryTest():
	voltage = HUB.battery.voltage()  # in mV
	min_voltage = 6500
	max_voltage = 8400

	percent = (voltage - min_voltage) * 100 / (max_voltage - min_voltage)
	percent = max(0, min(100, percent))

	print(f"Voltage: {voltage} mV")
	print(f"Battery: {percent:.0f}%")
	HUB.display.number(round(percent))

	while True:
		await wait(100)


if __name__ == "__main__":
	run_task(BatteryTest())
