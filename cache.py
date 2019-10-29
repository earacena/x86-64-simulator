# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: cache.py
# File Description: This file contains the functions related to the Cache component

class Block:
    def __init__(self):
        self.ref_bit = 0
        self.tag = 0
        self.index = 0
        self.data = None

class Cache:
    def __init__(self):
        pass

     # Least Recently Used algorithms
      # insert
      # remove
      # find
