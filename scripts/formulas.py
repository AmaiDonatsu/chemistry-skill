import argparse
import sys
from math import sqrt, pi

# Constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)
N_A = 6.02214076e+23  # Avogadro constant (mol^-1)
R = 8.314462618  # Gas constant (J/(mol·K))


def brownian_motion(t, T, eta, r):
    """
    Calculates the distribution of particles in Brownian motion.
    t: time (s)
    T: temperature (K)
    eta: viscosity (Pa·s)
    r: particle radius (m)
    """
    D = k_B * T / (6 * pi * eta * r)
    return D * t

def main():
    parser = argparse.ArgumentParser(description="Skill Chemical Formulas Script")
    subparsers = parser.add_subparsers(dest="formula", help="Formula to execute")

    # Subparser for brownian_motion
    bm_parser = subparsers.add_parser("brownian_motion", help="Calculate Brownian Motion Diffusion")
    bm_parser.add_argument("t", type=float, help="Time (s)")
    bm_parser.add_argument("T", type=float, help="Temperature (K)")
    bm_parser.add_argument("eta", type=float, help="Viscosity (Pa·s)")
    bm_parser.add_argument("r", type=float, help="Particle radius (m)")

    args = parser.parse_args()

    if args.formula == "brownian_motion":
        result = brownian_motion(args.t, args.T, args.eta, args.r)
        print(f"Result (Diffusion * Time): {result}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
