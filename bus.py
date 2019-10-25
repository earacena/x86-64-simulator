# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: bus.py
# File Description: This file contains the functions related to the Bus component

# Components linked
from cpu import CPU
from cache import Cache
from tlb import TLB
from memory import Memory
from disk import Disk

class Bus:
    def __init__(self, debug):

        self.debug_info = debug
        if self.debug_info == True:
            print("[Bus] initializing...")

        ### Initialization code ###
        self.cpu_link = None
        self.cache_link = None
        self.tlb_link = None
        self.memory_link = None
        self.disk_link = None
        ###########################

        if self.debug_info == True:
            print("[Bus] finished initializing...")
        
    # create link with CPU
    def link_cpu(self, cpu): 
        if self.debug_info == True:
            print("[Bus] linking with CPU...")
 
        cpu_link = cpu
        
        if self.debug_info == True and cpu_link is not None:
            print("[Bus] successfully linked with CPU...")

    # create link with Cache
    def link_cache(self, cache):  
        if self.debug_info == True:
            print("[Bus] linking with cache...")

        cache_link = cache
        
        if self.debug_info == True and cpu_link is not None:
            print("[Bus] successfully linked with cache...")

    # create link with TLB
    def link_tlb(self, tlb):  
        if self.debug_info == True:
            print("[Bus] linking with TLB...")

        tlb_link = tlb
        
        if self.debug_info == True and cpu_link is not None:
            print("[Bus] successfully linked with TLB...")

    # create link with memory
    def link_memory(self, memory):  
        if self.debug_info == True:
            print("[Bus] linking with memory...")

        memory_link = memory

        if self.debug_info == True and cpu_link is not None:
            print("[Bus] successfully linked with memory...")

    # create link with disk
    def link_disk(self, disk):
        if self.debug_info == True:
            print("[Bus] linking with disk...")

        disk_link = disk

        if self.debug_info == True and cpu_link is not None:
            print("[Bus] successfully linked with disk...")

    # communicate with another component and return requested information
    def communicate(component_caller, request, address):
        if self.debug_info == True:
            print("[Bus] caller:    ", component_caller)
            print("[Bus]   request: ", request)   
            print("[Bus]   address: ", address)
        
        ### Request handling ### 
        
        # CPU Requests

        ## cpu, memory access, virtual_addr  

        # Memory Requests
        
        # Cache Requests

        # TLB Requests

        # Disk Requests
  
        ########################

        if self.debug_info == True:
            print("[Bus] communication successful...")
