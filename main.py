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

    debug = True

    memory_size = input("[?] Size of main memory (bytes): ")
    cache_size  = input("[?] Size of cache (bytes): ")
    page_size   = input("[?] Size of pages (bytes): ")
    

  
    # Initialize components with bus and debug flag
    bus    = Bus(debug)
    cpu    = CPU(debug)
    cache  = Cache(cache_size, block_size, debug)
    tlb    = TLB(table_size, debug)
    memory = Memory(bus, memory_size, virtual_memory_size, debug)
    disk   = Disk(debug)
  
    menu   = GUI(bus, cpu, cache, tlb, memory, disk)
    menu.menu_loop()

main()

