"""
    Project: x86_64 Hardware Simulator
    Author: Emanuel Aracena
    Filename: cache.py
    File Description: This file contains the functions related to the Cache component
"""

# Force python to use Python3 print function
from __future__ import print_function

# Components
from bus import Bus

class Block:
    """ This class represents data stored as cache blocks. """
    def __init__(self):
        self.timer = 0
        self.valid = 0
        self.tag = 0
        self.index = 0
        self.data = "No data here"

class Cache:
    """ This class represents a cache component. """
    def __init__(self, cache_size, block_size, debug):
        """ Initialize the cache component. """
        self.debug_info = debug

        if self.debug_info is True:
            print("[Cache] initializing...")

        ### Initialization code ###
        self.cache_size = cache_size
        self.block_size = block_size
        self.num_of_blocks_used = 0
        self.max_number_of_blocks = int(self.cache_size / self.block_size)
        self.cache = [Block()] * int(self.cache_size / self.block_size)
        self.bus = Bus(self.debug_info)
        ###########################

        #### Performance Stats ####
        self.hits = 0
        self.misses = 0
        self.replacements = 0
        ###########################

        if self.debug_info is True:
            print("[Cache] finished initializing...")
            print("[Cache] Max number of blocks '", self.max_number_of_blocks, "'...")

    # return true if full, false otherwise
    def is_full(self):
        """ Return true if cache is full, false otherwise. """
        return self.num_of_blocks_used == self.max_number_of_blocks

    # LRU , return least recently used block's position
    def LRU(self):
        """ Return the oldest, least recently used block. """
        if self.debug_info is True:
            print("[Cache] Looking for least recently used block...")

        oldest_time = 0
        oldest_block_number = None

        for index, block in enumerate(self.cache):
            if block.timer >= oldest_time:
                oldest_time = block.timer
                oldest_block_number = index

        if self.debug_info is True:
            print("[Cache] LRU block found...")
            print("[...]      block data : ", self.cache[oldest_block_number].data)
            print("[...]      block timer: ", self.cache[oldest_block_number].timer)

        return oldest_block_number

    # Least Recently Used algorithms
    # insert, insert data into a block in position of previous LRU
    def insert(self, data):
        """ Insert a new block in the LRU block's position. """
        if self.debug_info is True:
            print("\n[Cache] inserting block...")
            print("[...]        Data: ", data)
            print("[...] Current Cache table: ")
            self.print_cache()

        if self.is_full() is True:
            # Swap blocks if full
            print("[...] Cache full...")
            lru_block = self.LRU()

            if self.debug_info is True:
                print("[Cache] LRU block to be replaced: ")
                print("[...]    data: ", self.cache[lru_block].data)
                print("[...]   timer: ", self.cache[lru_block].timer)

            self.cache[lru_block] = Block()
            self.cache[lru_block].valid = 1
            self.cache[lru_block].data = data

            self.print_cache()
        else:
            # Otherwise, place into an open spot
            print("[...] Cache has empty slots...")
            position = self.find_empty_spot()
            self.cache[position] = Block()
            self.cache[position].data = data
            self.cache[position].valid = 1
            self.num_of_blocks_used = self.num_of_blocks_used + 1

    def find_empty_spot(self):
        """ Find an empty spot in cache. Return index. """
        for index, block in enumerate(self.cache):
            if block.valid == 0:
                return index
        return 0

    def find_block(self, address):
        """ Returns "HIT" or "MISS" depending on if data is present. """
        if self.debug_info is True:
            print("[Cache] looking for block with address '" + str(address) + "'...")

        for block in self.cache:
            if block.data[0] == address:
                return block.data[1]

        # If this point reached, return Miss
        return "MISS"

    def look_for_block_addr_in_tlb(self, address, callee, callee_name):
        """ If data was missing, and find and store. """
        if self.debug_info is True:
            print("[Cache] Looking for new block in TLB...")

        block_address = self.bus.communicate("cache", callee, callee_name,
                                             "TLB, physical address of virtual", address)
        return block_address

    def retrieve_block(self, address, callee, callee_name):
        """ Use bus to get block with specified address. Return block. """
        if self.debug_info is True:
            print("[Cache] Retrieving missing block...")
        block = self.bus.communicate("cache", callee, callee_name, "memory, give block", address)
        self.insert([address, block])

    def update_timer(self):
        """ Update the timers for all blocks in memory, increment by 1. """
        for block in self.cache:
            block.timer = block.timer + 1

    def print_stats(self):
        """ Print the hit ratio, miss ratio, and replacement ratios. """
        print("[Cache] Printing cache statistics:")
        total = self.hits + self.misses + self.replacements

        # Avoid dividing by 0
        if total == 0:
            total = 1

        print("[...]    hit ratio:         ", (self.hits / (total)))
        print("[...]    miss ratio:        ", (self.misses / (total)))
        print("[...]    replacement ratio: ", (self.replacements / (total)))

    def print_cache(self):
        """ Print the contents of the cache. """
        counter = 0
        print("[Cache] Printing contents of cache:")
        print("[...] Set | B1 timer | B1 data\t| B2 timer | B2 data\t")
        for i in range(0, len(self.cache)-1, 2):
            block1 = self.cache[i]
            block2 = self.cache[i+1]
            print("[...] ", counter, " | ", block1.timer, " | ", block1.data, " | ",
                  block2.timer, " | ", block2.data)
            counter = counter + 1

def main():
    """ Unit test. """
    debug = True
    cache_size = 50       # smaller than main memory
    block_size = 5        # smaller than cache, two blocks per set

    cache = Cache(cache_size, block_size, debug)

    # populate the cache with data
    cache.insert(["0xAAAA", 100])
    cache.update_timer()
    cache.insert(["0xBBBB", 200])
    cache.update_timer()
    cache.insert(["0xCCCC", 300])
    cache.update_timer()
    cache.insert(["0xDDDD", 400])
    cache.update_timer()
    cache.insert(["0xEEEE", 500])
    cache.update_timer()
    cache.insert(["0xFFFF", 600])
    cache.update_timer()
    cache.insert(["0x0000", 700])
    cache.update_timer()
    cache.insert(["0x1111", 800])
    cache.update_timer()
    cache.insert(["0x2222", 900])
    cache.update_timer()
    cache.insert(["0x3333", 1000])
    cache.update_timer()
    print("")
    cache.print_cache()

    # test swapping LRU
    cache.insert(["0x4444", 1100])

    # test finding data based on virtual address
    print("\n[TEST] Looking for data with address '0xEEEE'...")
    data = cache.find_block("0xEEEE")
    print("[...] Data found/Status: ", data)

    # test finding data that isnt present, SHOULD RETURN "MISS"
    print("\n[TEST] Looking for data with address '0xGGGG'...")
    data = cache.find_block("0xGGGG")
    print("[...] Data found/Status: ", data)
