from pybricks.parameters import Stop
from pybricks.pupdevices import Motor

def calculate_simple_gear_ratio(gears):
    """
    Returns motor_turns / final_gear_turns for a gear train (> 1 means the
    final gear turns slower than the motor, i.e. a reduction).

    `gears` lists the gears from the motor to the final gear, in order.
    Each entry is one of:

      int          a gear (tooth count) that meshes with the entry before
                   and the entry after it. This is a simple chain; every
                   mesh multiplies the ratio by driven/driver, so idler
                   gears cancel out.

      (in, out)    a compound gear: two gears fixed on the SAME axle, so
                   they always turn together. `in` meshes with the entry
                   before, `out` meshes with the entry after. The axle
                   itself adds no ratio, only the meshes do.

    The first entry is the gear on the motor and the last is the final gear.
    Use a plain int for those two (a tuple's `in` on the first entry or `out`
    on the last entry is ignored).

    Examples:
      [8, 24]                   8T on motor drives 24T:         ratio 3
      [8, 16, 24]               16T is an idler:                ratio 3
      [8, (24, 8), 40]          8T->24T, then 8T (on the same
                                axle as the 24T) -> 40T:        ratio 3 * 5 = 15

    Common mistake: [8, 24, 8, 40] means FOUR gears meshing in a line
    (ratio 5, the 24T and 8T are just idlers). If the 24T and 8T share an
    axle, write (24, 8) as one entry.

    None means no gearing (ratio 1).
    """
    if gears is None:
        return 1.0

    if len(gears) < 2:
        raise ValueError("At least two gears are required for a ratio calculation.")

    overall_ratio = 1.0
    previous_out = None
    for gear in gears:
        if isinstance(gear, (tuple, list)):
            if len(gear) != 2:
                raise ValueError("A compound gear must be (in_teeth, out_teeth).")
            gear_in, gear_out = gear
        else:
            gear_in = gear_out = gear

        if previous_out is not None:
            # this gear meshes with the previous one: driven / driver
            overall_ratio *= gear_in / previous_out
        previous_out = gear_out
    return overall_ratio

#this class allows to change the gear configuration of a motor
#without creating a new motor object
class GearSwapMotor(Motor):
    def __init__(self, port, positive_direction):
        self.port = port
        self.init_positive_direction = positive_direction
        self.gears = None
        self.gear_ratio = 1
        self.direction_x = 1

        super().__init__(self.port, self.init_positive_direction)
        print("Motor initialized with positive direction", positive_direction)

    # gears: see calculate_simple_gear_ratio for how to write a chain
    # (ints) and compound gears ((in, out) tuples)
    def reconfigure(self, positive_direction, gears):
        print("direction comparison:", self.init_positive_direction == positive_direction)
        if self.init_positive_direction == positive_direction:
            self.direction_x = 1
        else:
            self.direction_x = -1

        #print("new direction x:", self.direction_x)
        #print("Motor reconifigured with positive direction", positive_direction)
        #print("direction X:", self.direction_x)
        self.gears = gears
        #print("reset gears to ", self.gears)
        self.gear_ratio = calculate_simple_gear_ratio(self.gears)

    
    async def run_angle(self, speed, rotation_angle,  
                  then: Stop = Stop.HOLD,
                    wait: bool = True, reset_angle=True):
        if reset_angle:
            super().reset_angle()
        
        calc_speed = speed*self.gear_ratio
        calc_angle = self.direction_x*rotation_angle*self.gear_ratio

        #print("target angle", rotation_angle, "speed", speed,
        #      "direction_x", self.direction_x,
        #      ", calculated angle", calc_angle, "and speed", calc_speed  )    
        await super().run_angle(speed = calc_speed,
                          rotation_angle = calc_angle,
                          then = then,
                          wait = wait
                          )
