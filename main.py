"""
  Project: x86_64 Hardware Simulator
  Author: Emanuel Aracena Beriguete
  Filename: main.py
  File Description: This file contains the main routine of the simulator
"""

# Ensure python only uses python3 print function
from __future__ import print_function

# Components
from gui import GUI
from cpu import CPU
from cache import Cache
from tlb import TLB
from memory import Memory
from disk import Disk
from bus import Bus

def main():
    """ Main Routine """

    print("\n[.] Initializing parameters/settings for simulator...")
    print("[.] Values in brackets represent reccommended/tested values.")
    print("[.] Using untested values may result in unstable behavior.\n")
    # Ask for parameters
    user_debug = input("[?] Enable debugging information [No]: ")
    debug = (user_debug == "Yes")
    memory_size = input("[?] Size of main memory (bytes) [100]: ")
    virtual_memory_size = input("[?] Size of virtual memory (bytes) [8000]: ")
    cache_size = input("[?] Size of cache (bytes)[40]: ")
    block_size = input("[?] Size of cache blocks (bytes)[4]: ")
    page_size = input("[?] Size of disk pages (bytes)[32]: ")
    table_size = input("[?] Number of TLB table entries (bytes)[10]: ")

    # Initialize components with bus and debug flag
    bus = Bus(debug)
    cpu = CPU(debug)
    cache = Cache(int(cache_size), int(block_size), debug)
    tlb = TLB(int(table_size), debug)
    memory = Memory(int(memory_size), int(virtual_memory_size), debug)
    disk = Disk(int(page_size), debug)

    # Initialize GUI
    menu = GUI(bus, cpu, cache, tlb, memory, disk, debug)
    menu.menu_loop()

main()
