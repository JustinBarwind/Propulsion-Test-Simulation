import numpy as np
import pandas as pd
from scipy.integrate import trapezoid

def load_file(file):

    df = pd.read_csv(file)

    df = df.iloc[:, :3]

    df.columns = [
        "time_ms",
        "raw",
        "thrust_lbf"
    ]

    df["time_s"] = df["time_ms"] / 1000

    return df


def analyze_thrust(df):

    time = df["time_s"].values

    thrust = df["thrust_lbf"].values

    baseline = np.mean(thrust[:20])

    thrust_clean = thrust - baseline

    threshold = np.std(thrust_clean[:20]) * 2

    active = np.abs(thrust_clean) > threshold

    start = np.argmax(active)

    end = len(active) - np.argmax(active[::-1]) - 1

    burn_time = time[end] - time[start]

    peak = np.max(thrust_clean)

    impulse = trapezoid(thrust_clean, time)

    avg = impulse / burn_time

    return {
        "peak_thrust_lbf": peak,
        "burn_time_s": burn_time,
        "total_impulse_lbf_s": impulse,
        "average_thrust_lbf": avg
    }


def export_desmos(df):

    time = df["time_s"].values

    thrust = df["thrust_lbf"].values

    baseline = np.mean(thrust[:20])

    thrust_clean = thrust - baseline

    export_df = pd.DataFrame({
        "time_s": time,
        "thrust_lbf": thrust_clean
    })

    output = "./desmos_exports/desmos_data.csv"

    export_df.to_csv(output, index=False)

    print(f"\nDesmos export saved: {output}")
