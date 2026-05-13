import numpy as np
import pandas as pd
from datetime import datetime
from config import MOTOR

def simulate_motor():

    dt = 0.005

    time_s = np.arange(0, 3, dt)

    thrust = []

    for t in time_s:

        # before ignition
        if t < MOTOR["ignition_delay_s"]:
            f = 0

        # ramp up
        elif t < 0.3:

            ramp = (
                (t - MOTOR["ignition_delay_s"])
                /
                (0.3 - MOTOR["ignition_delay_s"])
            )

            f = MOTOR["peak_thrust_lbf"] * ramp

        # burn decay
        elif t < MOTOR["burn_time_s"]:

            decay_time = t - 0.3

            f = (
                MOTOR["peak_thrust_lbf"]
                *
                np.exp(-2 * decay_time)
            )

        # burnout
        else:
            f = 0

        thrust.append(f)

    thrust = np.array(thrust)

    # sensor noise
    thrust += np.random.normal(
        0,
        MOTOR["noise_std"],
        len(thrust)
    )

    # fake ADC/raw values
    raw = thrust * 100 + np.random.normal(0, 5, len(thrust))

    time_ms = (time_s * 1000).astype(int)

    df = pd.DataFrame({
        "time_ms": time_ms,
        "raw": raw,
        "thrust_lbf": thrust
    })

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"./rocket_data/sim_{timestamp}.csv"

    df.to_csv(filename, index=False)

    print(f"\nSimulation saved: {filename}")

    return filename
