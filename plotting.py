import matplotlib.pyplot as plt
from thrust_analysis import load_file

def plot_thrust_curve(file):

    df = load_file(file)

    time = df["time_s"].values

    thrust = df["thrust_lbf"].values

    baseline = thrust[:20].mean()

    thrust_clean = thrust - baseline

    plt.figure(figsize=(10,6))

    plt.plot(time, thrust_clean)

    plt.axhline(0)

    plt.xlabel("Time (s)")
    plt.ylabel("Thrust (lbf)")

    plt.title("Simulated Rocket Motor")

    plt.grid()

    plt.show()
