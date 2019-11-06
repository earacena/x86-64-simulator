# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: main.py
# File Description: This file contains the main routine of the simulator

# Components
from gui import GUI
from cpu import CPU
from cache import Cache
from tlb import TLB
from memory import Memory
from disk import Disk
from bus import Bus

def main():

    print("Initializing parameters/settings for simulator...")

    user_debug = input("[?] Enable debugging information [No]: ")
    if user_debug == "Yes":
        debug = True
    else:
        debug = False

    memory_size = input("[?] Size of main memory (bytes) [100]: ")
    virtual_memory_size = input("[?] Size of virtual memory (bytes) [8000]: ")
    cache_size  = input("[?] Size of cache (bytes)[40]: ")
    block_size = input("[?] Size of cache blocks (bytes)[4]: ")
    page_size   = input("[?] Size of disk pages (bytes)[32]: ")
    table_size = input("[?] Number of TLB table entries (bytes)[10]: ")
  
    # Initialize components with bus and debug flag
    bus    = Bus(debug)
    cpu    = CPU(debug)
    cache  = Cache(int(cache_size), int(block_size), debug)
    tlb    = TLB(int(table_size), debug)
    memory = Memory(int(memory_size), int(virtual_memory_size), debug)
    disk   = Disk(debug)
  
    menu   = GUI(bus, cpu, cache, tlb, memory, disk, debug)
    menu.menu_loop()

main()

