"""Bayesian Optimisation for Function 1"""

from pathlib import Path

import numpy as np


def coalesce(value, default):
    """
    Set a value to the specified default if it is None.

    The same as R's null-coalescing operator.
    """
    return default if value is None else value


def load_data(
    subdir,
    base_dir=None,
    in_file_name=None,
    out_file_name=None,
):
    """
    Load initial data for Bayesian optimisation.

    Returns:
        X (numpy.ndarray): Input data.
        Y (numpy.ndarray): Output data.
    """

    # Load initial data

    # TODO: Handle file not found errors

    in_file_name = coalesce(in_file_name, 'initial_inputs.npy')
    out_file_name = coalesce(out_file_name, 'initial_outputs.npy')

    base_dir = coalesce(base_dir, Path(__file__).resolve().parents[0])
    base_dir = base_dir / 'initial_data'

    in_file_path = base_dir / subdir / in_file_name
    out_file_path = base_dir / subdir / out_file_name

    X = np.load(in_file_path)
    Y = np.load(out_file_path)

    return X, Y


def main():
    """
    Main function to orchestrate the code.
    """

    subdir = 'function_1'

    X, Y = load_data(subdir)

    # Print the loaded data shapes for verification
    print(f'\nLoaded input data shape:  {X.shape}')
    print(f'Loaded output data shape: {Y.shape}')

    # Print the loaded data
    print('\nInput data (X):')
    print(X)
    print('\nOutput data (Y):')
    print(Y)

    # Perform Bayesian optimisation using the loaded data
    # TODO: Implement the Bayesian optimisation logic here


if __name__ == '__main__':
    main()
