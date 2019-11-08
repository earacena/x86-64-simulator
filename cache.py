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
        self.data = "No data here"      # data requested by CPU, for example: value of DWORD PTR [rbp-4]


## Two-way associative set
#class Set:
#    def __init__(self):
#        self.block1 = Block()
#        self.block2 = Block()      

class Cache:
    def __init__(self, cache_size, block_size, debug):
        self.debug_info = debug

        if self.debug_info == True:
            print("[Cache] initializing...")
        
        ### Initialization code ###
        self.cache_size  = cache_size
        self.block_size  = block_size
        #self.num_of_sets = num_of_sets 
        self.num_of_blocks_used = 0
        self.max_number_of_blocks = int(self.cache_size / self.block_size)
        # set (10 bytes)  - block 1 (5 bytes) | block 2 (5 bytes)
        self.cache = [Block()] * int(self.cache_size / self.block_size)
        ###########################
        
            
        if self.debug_info == True:
            print("[Cache] finished initializing...")
            print("[Cache] Max number of blocks '", self.max_number_of_blocks, "'...")
    
    # return true if full, false otherwise
    def is_full(self):
        return self.num_of_blocks_used == self.max_number_of_blocks

    # LRU , return least recently used block's position
    def LRU(self):
        if self.debug_info == True:
            print("[Cache] Looking for least recently used block...")

        oldest_time = 0
        oldest_block_number = None

        for index, block in enumerate(self.cache):
            if block.timer >= oldest_time:
                oldest_time = block.timer
                oldest_block_number = index
                
        # Once oldest time is marked, find first block with that time
         
        
        # Look in cache for LRU
        if self.debug_info == True:
            print("[Cache] LRU block found...")
            print("[...]      block data : ", self.cache[oldest_block_number].data)
            print("[...]      block timer: ", self.cache[oldest_block_number].timer)
        
        return oldest_block_number

    # Least Recently Used algorithms
    # insert, insert data into a block in position of previous LRU
    def insert(self, data): 
        if self.debug_info == True:
            print("\n[Cache] inserting block...")
            print("[...]        Data: ", data)
            print("[...] Current Cache table: ")
            self.print_cache()

        # swap blocks
        if self.is_full() == True:
            print("[...] Cache full...")
            lru_block = self.LRU()


            if self.debug_info == True:
                print("[Cache] LRU block to be replaced: ", )
                print("[...]    data: ", self.cache[lru_block].data)
                print("[...]   timer: ", self.cache[lru_block].timer) 
            
            self.cache[lru_block] = Block()
            self.cache[lru_block].valid = 1
            self.cache[lru_block].data = data

            self.print_cache()
        # find empty spot
        else:
            spot = False
            print("[...] Cache has empty slots...")
            position = self.find_empty_spot()
            self.cache[position] = Block()
            self.cache[position].data = data
            self.cache[position].valid = 1
            self.num_of_blocks_used = self.num_of_blocks_used + 1
            
            

    def find_empty_spot(self):
        for index, block in enumerate(self.cache):
            if block.valid == 0:
                return index            

    # returns "HIT" or "MISS" depending on if data is present
    def find_block(self, address):
        if self.debug_info == True:
            print("[Cache] looking for block with address '" + address + "'...")
        
        for block in self.cache:
            if block.data[0] == address:
                return block.data[1]

        # If this point reached, return Miss
        return "MISS" 


    # If data was missing, and find and store
    def look_for_block_addr_in_tlb(self, address, callee, callee_name):
        if self.debug_info == True:
            print("[Cache] Looking for new block in TLB...")
        
        block_address = self.bus.communicate("cache", callee, callee_name, 
                                             "TLB, physical address of virtual", address)

    def update_timer(self):
        for block in self.cache:
            block.timer = block.timer + 1

    def print_cache(self):
        counter = 0
        print("[Cache] Printing contents of cache:")
        print("[...] Set | B1 timer | B1 data\t| B2 timer | B2 data\t")
        for i in range(0, len(self.cache)-1, 2):
              block1 = self.cache[i]
              block2 = self.cache[i+1]
              print("[...] ", counter, " | " , block1.timer, " | ", block1.data, " | ",
                    block2.timer, " | ", block2.data)
              counter = counter + 1
            

def main():
    debug = True
    cache_size  = 50       # smaller than main memory
    block_size  = 5        # smaller than cache, two blocks per set

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
    data = cache.find_block("0xEEEE")
    print("\n[TEST] Looking for data with address '0xEEEE'...")
    print("[...] Data found/Status: ", data)
    
    # test finding data that isnt present, SHOULD RETURN "MISS"
    data = cache.find_block("0xGGGG")
    print("\n[TEST] Looking for data with address '0xGGGG'...")
    print("[...] Data found/Status: ", data) 
