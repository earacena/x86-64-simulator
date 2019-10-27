# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: common.py
# File Description: This file contains usefule functions used throughout the
#                   project.


# Padded hex, just provide value and expected length
def phex(value, expected):
    return f"{value:#0{expected}x}"
