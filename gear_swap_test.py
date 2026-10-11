from gear_swap_motor import calculate_simple_gear_ratio

# Checks the gear ratio math for simple chains and compound gears.
# Needs no motor, so it can run anywhere pybricks is importable.

def _close(a, b):
    return abs(a - b) < 1e-9

def _expect_ratio(label, gears, expected):
    ratio = calculate_simple_gear_ratio(gears)
    ok = _close(ratio, expected)
    print("PASS" if ok else "FAIL", label, gears, "ratio", ratio, "expected", expected)
    return ok

def _expect_error(label, gears):
    try:
        calculate_simple_gear_ratio(gears)
    except ValueError:
        print("PASS", label, gears, "raised ValueError")
        return True
    print("FAIL", label, gears, "did not raise ValueError")
    return False

def test_gear_ratios():
    results = [
        _expect_ratio("no gearing", None, 1),
        _expect_ratio("direct 1:1", [12, 12], 1),
        _expect_ratio("reduction", [8, 24], 3),
        _expect_ratio("speed up", [24, 8], 1 / 3),
        _expect_ratio("idler cancels", [8, 16, 24], 3),
        _expect_ratio("two idlers cancel", [8, 40, 16, 24], 3),
        # 8T -> 24T (3x), then 8T on the same axle as the 24T -> 40T (5x)
        _expect_ratio("compound", [8, (24, 8), 40], 15),
        # same teeth written as a chain: 24T and 8T are idlers, ratio is 40/8
        _expect_ratio("chain not compound", [8, 24, 8, 40], 5),
        _expect_ratio("two compounds", [8, (24, 8), (24, 12), 36], 3 * 3 * 3),
        _expect_ratio("list as compound", [8, [24, 8], 40], 15),
        _expect_error("one gear", [8]),
        _expect_error("bad compound", [8, (24, 8, 3), 40]),
    ]
    passed = sum(1 for r in results if r)
    print(passed, "of", len(results), "gear ratio tests passed")
    return passed == len(results)

# Turning the final gear by `target` degrees needs the motor to turn
# target * ratio degrees; print what each example would command.
def show_motor_angles():
    for gears in ([8, 24], [8, (24, 8), 40]):
        ratio = calculate_simple_gear_ratio(gears)
        print(gears, ": final gear 90 deg -> motor", 90 * ratio, "deg")

if __name__ == "__main__":
    test_gear_ratios()
    show_motor_angles()
