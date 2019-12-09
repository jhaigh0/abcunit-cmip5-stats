#!/usr/bin/env python

"""This script takes arguments from the command line and runs the script run_batch
for each of the models provided as an argument or for all models if none were
provided"""

import argparse
import subprocess
import os

from lib import defaults


def arg_parse_all():
    """Parses arguments given at the command line"""
    parser = argparse.ArgumentParser()
    stat_choices = ['min', 'max', 'mean']
    model_choices = defaults.models
    ensemble_choices = defaults.ensembles
    variable_choices = defaults.variables
    parser.add_argument('-s', '--stat', nargs=1, type=str, choices=stat_choices, required=True,
                        help=f'Type of statistic, must be one of: {stat_choices}', metavar='')
    parser.add_argument('-m', '--model', type=str, default=model_choices,
                        help=f'Institue and model combination to run statistic on, '
                             f'can be one or many of: {model_choices}. '
                             f'Default is all models.', metavar='', nargs='*')
    parser.add_argument('-e', '--ensemble', type=str, default=ensemble_choices,
                        help=f'Ensemble to run statistic on, can be one or many of: '
                             f'{ensemble_choices}. Default is all ensembles.', metavar='',
                        nargs='*')
    parser.add_argument('-v', '--var', choices=variable_choices, default=variable_choices,
                        help=f'Variable to run statistic on, can be one or many of: '
                             f'{variable_choices}. Default is all variables.', metavar='',
                        nargs='*')
    return parser.parse_args()


def loop_over_models(args):
    """Runs run batch for each of the models listed"""
    current_directory = os.getcwd()

    stat = str(args.stat).strip("[] \'")
    ensembles = str(args.ensemble).strip("[]").replace(",", "")
    vars = str(args.var).strip("[]").replace(",", "")

    # iterate over models
    for model in args.model:
        print(f"Running for {model}")
        # calls run_batch from command line
        cmd = f"{current_directory}/run_batch.py -s {stat} -m {model} -e " \
              f"{ensembles} -v {vars}"
        subprocess.call(cmd, shell=True)


def main():
    """Runs script if called on command line"""
    args = arg_parse_all()
    print(f"Finding {args.stat} of {args.var} for {args.model}, {args.ensemble}.")
    loop_over_models(args)



if __name__ == '__main__':
    main()
    