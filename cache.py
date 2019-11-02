# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: cache.py
# File Description: This file contains the functions related to the Cache component

class Block:
    def __init__(self):
        self.timer = 0
        self.valid = 0
        self.tag = 0
        self.index = 0
        self.data = None      # data requested by CPU, for example: value of DWORD PTR [rbp-4]


## Two-way associative set
class Set:
    def __init__(self):
        self.block1 = Block()
        self.block2 = Block()

class Cache:
    def __init__(self, cache_size, block_size, num_of_sets, debug):
        self.debug_info = debug

        if self.debug_info == True:
            print("[Cache] initializing...")
        
        ### Initialization code ###
        self.cache_size  = cache_size
        self.block_size  = block_size
        self.num_of_sets = num_of_sets 

        # set (10 bytes)  - block 1 (5 bytes) | block 2 (5 bytes)
        self.cache = [None] * ((self.cache_size / self.block_size) / self.num_of_sets)
        ###########################
        
            
        if self.debug_info == True:
            print("[Cache] finished initializing...")

    # Least Recently Used algorithms
    # insert, insert data into a block in position of previous LRU
    def insert(self, data, position): 
        if self.debug_info == True:
            print("[Cache] inserting block in LRU position:")
            print("[Cache]        Data: ", data)
            print("[Cache]    Position: ", position)


    # LRU , return true if least recently used block
    def LRU(self):
        if self.debug_info == True:
            print("[Cache] Looking for least recently used block...")
        
        # Look in cache for LRU
        if self.debug_info == True:
            print("[Cache] LRU block found...")
            # print block.data, block timer.
        

    # returns "HIT" or "MISS" depending on if data is present
    def find_block(self, data):
        if self.debug_info == True:
            print("[Cache] looking for block with data '" + data + "'...")

    # If data was missing, and cache is full, replace LRU
    def replace_block(self, address):
        if self.debug_info == True:
            print("[Cache] Replacing LRU with new block...")



def main():
    debug = True
    cache_size  = 50       # smaller than main memory
    block_size  = 5        # smaller than cache, two blocks per set
    num_of_sets = 2

    cache = Cache(cache_size, block_size, num_of_sets, debug)

