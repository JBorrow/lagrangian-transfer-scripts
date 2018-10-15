"""
Shared variables throughout scripts.
"""

import yaml

environment_name = "simba_env"

class Parameters(object):
    def __init__(self, handle):
        self.raw_data = yaml.load(handle)

        self.parse()

        return

    def parse(self):
        self.snapshot_ini = self.raw_data["snapshots"]["ini"]
        self.snapshot_end = self.raw_data["snapshots"]["end"]

        self.halo_catalogue_type = self.raw_data["halo_catalogue"]["type"]
        self.halo_catalogue_run_caesar = self.raw_data["halo_catalogue"]["run_caesar"]
        self.halo_catalogue_path = self.raw_data["halo_catalogue"]["path"]
        self.halo_catalogue_pickle_name = self.raw_data["halo_catalogue"]["pickle_name"]

        return
    
        
try:
    with open("parameters.yml", "r") as f:
        parameters = Parameters(f)
except FileNotFoundError:
    pass
