# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: bus.py
# File Description: This file contains the functions related to the Bus component

# Components linked
class Bus:
    def __init__(self, debug):

        self.debug_info = debug
        if self.debug_info == True:
            print("[Bus] initializing...")

        ### Initialization code ###
        ###########################

        if self.debug_info == True:
            print("[Bus] finished initializing...")
        
    # communicate with another component and return requested information
    def communicate(self, component_caller, component_callee, callee_name, request, info):
        if self.debug_info == True:
            print("")
            print("[Bus] caller:    ", component_caller)
            print("[Bus] callee:    ", callee_name)
            print("[Bus]   request: ", request)   
            print("[Bus]   info:    ", info)
        
        ### Request handling ### 
        ret = None 
        # CPU Requests
        if component_caller == "cpu" and request == "virtual memory, print position":
            # Memory
            component_callee.print_virtual_with_position(info)
            ret = "N/A"

        if component_caller == "cpu" and request == "virtual memory, starting position":
            # ...,    Memory
            ret = component_callee.find_starting_address()

        if component_caller == "cpu" and request == "cache, give block":
            ret = cache.find_block(info)

        # Memory Requests
        if component_caller == "memory" and request == "disk, initial page number":
            ret = component_callee.initial_page_number

        if component_caller == "memory" and request == "disk, send page size":
            ret = component_callee.page_size

        if component_caller == "memory" and request == "disk, send page":
            ret = component_callee.load_page(int(info))

        if component_caller == "virtual memory" and request == "disk, all pages for mapping":
            ret = component_callee.storage        
        # Cache Requests

        # TLB Requests

        # Disk Requests
  
        ########################

        if self.debug_info == True:
            print("[Bus] communication response: ", ret)

        return ret
