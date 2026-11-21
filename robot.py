from pybricks.parameters import Color
from pybricks.tools import multitask, run_task, wait

from M12_ForestElder import M12
from M13_KeystoneSpecies import M13
from M14_SeedsOfRenewal import M14
from M15_BiocentricArchitecture import M15
import M3_M4 as M3_M4
from M4_LuckyLeaves import M4
from M5_ReachingRoots import M5
from M6_M11_LeafcutterFrenzy_V2 import M6_M11
from M7_Mycelium import M7
from M7_M13 import M7_M13
from M9_ResearchPlatform_R import M9
from RobotMotorReset import ArmReset
from BatteryTest import BatteryTest
from library import set_drivebase, print_drivebase_settings
from ui import add_program, user_interface

from M1_DroneSurvey import M1
from M1_M2 import M1_M2
from M3_FlipTheRock import M3
#from run1 import run1
#from run2 import run2
#from run3 import run3
#from run4 import run4
#from run5 import run5
#from run6 import run6

async def main():
    # Import from xbox_teleop the teleop function if you want to use
    # the telop mode and add the telop program
    
    # Blank,  done to make code multitask
    # Needed due to how the blocks work
    await multitask(
        wait(0),
    )
    # Print to consule the default drivebase settings
    await print_drivebase_settings()
    # Override these settings. Note pybricks is conservative with speeds.
    # The default speeds are about 40% of what the motors can handle
    # You probably can double the default speeds in the robot_config file.
    # Conversely the accelration values pybricks creates tend to be too high
    # If your wheels slip your distances will be off. Lower accelration as needed
    # in the robot_config file to eliminate wheel slipage. These values will depend on wheel choice, center of gravity of your robot and robot weight.
    await set_drivebase()
    # Add the programs (Missons) below they will appear in the order placed
    # Missions will need to be imported, see example missions/utility programs
    # below
    #await add_program(M1, '1', Color.GREEN)
    await add_program(M1_M2, '1', Color.VIOLET) 
    await add_program(M3, '2', Color.YELLOW)
    await add_program(M5, '3', Color.RED)
    await add_program(M9, '4', Color.RED)
    await add_program(M6_M11, '6', Color.RED) #Move From Left home to Right Home
    await add_program(M7_M13, 'A', Color.RED) #mycelium
    #await add_program(M13, 'B', Color.RED) #keystone species
    await add_program(M12, 'C', Color.RED) #forest elder
    await add_program(M15, 'D', Color.RED) #biocentric architecture
    await add_program(M14, 'E', Color.RED) #seeds of renewal
    await add_program(ArmReset, 'R', Color.RED)
    await add_program(BatteryTest, 'T', Color.RED)
    #await add_program(run4, '5', Color.BLUE)
    #await add_program(run6, '6', Color.RED)

    # Launch the user interface
    await user_interface()


if __name__ == "__main__":
    run_task(main())