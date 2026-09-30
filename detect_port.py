from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.tools import run_task, wait


PORTS = (Port.A, Port.B, Port.C, Port.D, Port.E, Port.F)
DETECTED_DEVICES = []


def detect_ports():
    """Identify and construct devices before multitasking starts."""
    for port in PORTS:
        try:
            motor = Motor(port)
            motor.angle()
            DETECTED_DEVICES.append((port, "motor", motor))
            continue
        except Exception:
            pass

        try:
            DETECTED_DEVICES.append((port, "color sensor", ColorSensor(port)))
        except Exception as error:
            print(port, "EMPTY OR UNSUPPORTED DEVICE:", error)


async def test_device(port, device_type, device):
    if device_type == "motor":
        print(port, "MOTOR, running two rotations")
        await device.run_angle(360, 720)
    else:
        print(port, "COLOR SENSOR, flashing three times")
        for _ in range(3):
            await device.lights.on(100)
            await wait(250)
            await device.lights.off()
            await wait(250)


async def run_tests():
    print("Testing ports A-F. Motors rotate twice; color sensors flash three times.")
    for port, device_type, device in DETECTED_DEVICES:
        await test_device(port, device_type, device)
    print("Port test complete.")


if __name__ == "__main__":
    detect_ports()
    run_task(run_tests())
