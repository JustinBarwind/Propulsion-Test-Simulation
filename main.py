from motor_model import simulate_motor

from thrust_analysis import (
    load_file,
    analyze_thrust,
    export_desmos
)

from plotting import plot_thrust_curve

if __name__ == "__main__":

    # generate simulated motor test
    file = simulate_motor()

    # load simulated data
    df = load_file(file)

    # analyze thrust
    results = analyze_thrust(df)

    print("\n===== SIMULATION RESULTS =====\n")

    for k, v in results.items():
        print(f"{k}: {v}")

    # export for Desmos
    export_desmos(df)

    # plot thrust curve
    plot_thrust_curve(file)
