"""
    Project: x86_64 Hardware Simulator
    Name: Emanuel Aracena
    Filename: bus.py
    File Description: This file contains the functions related to the Bus component
"""

# Force python to use Python3 print function
from __future__ import print_function


class Bus:
    """
        This class represents the component that handles communication between other
        components.
    """
    def __init__(self, debug):
        """ Initialize the bus component. """
        self.debug_info = debug

        if self.debug_info is True:
            print("[Bus] initializing...")

        ### Initialization code ###
        ###########################

        if self.debug_info is True:
            print("[Bus] finished initializing...")


    def communicate(self, component_caller, component_callee, callee_name, request, info):
        """
            Communicate between two components, calling methods of a callee component on
            behalf of a caller component.
        """
        if self.debug_info is True:
            print("\n[Bus] caller:    ", component_caller)
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
            ret = component_callee.find_block(info)

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
        if component_caller == "cache" and request == "TLB, physical address of virtual":
            ret = component_callee.find_physical_address(info)

        if component_caller == "cache" and request == "memory, give block":
            ret = component_callee.virtual_memory[int(info, 0)][1]

        # TLB Requests

        # Disk Requests

        ########################
        if self.debug_info is True:
            print("[Bus] communication response: ", ret)

        return ret
