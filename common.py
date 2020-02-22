"""
    Project: x86_64 Hardware Simulator
    Author: Emanuel Aracena Beriguete
    Filename: common.py
    File Description: This file contains usefule functions used throughout the
                      project.
                      Note: phex() uses python 3.6+ format syntax.
"""

def phex(value, expected):
    """ Returns radded hex, just provide value and expected length. """
    return f"{value:#0{expected}x}"
