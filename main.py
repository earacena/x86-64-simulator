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
  
    # Initialize components with bus and debug flag
    bus    = Bus(debug)
    cpu    = CPU(bus, debug)
    cache  = Cache(bus, debug)
    tlb    = TLB(bus, debug)
    memory = Memory(bus, debug)
    disk   = Disk(bus, debug)
  
    # Link components with bus
    bus.link_cpu(cpu)
    bus.link_cache(cache)
    bus.link_tlb(tlb)
    bus.link_memory(memory)
    bus.link_disk(disk)
   
    menu   = GUI(bus, cpu, cache, tlb, memory, disk)
    menu.menu_loop()

main()
