"""
Shared variables throughout scripts.
"""


environment_name = "simba_env"

try:
    import yaml

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

            self.ltcaesar_notrunc = self.raw_data["ltcaesar"]["notrunc"]
            self.ltcaesar_yt = self.raw_data["ltcaesar"]["yt"]
            self.ltcaesar_otherhalofinder = self.raw_data["ltcaesar"]["otherhalofinder"]
            self.ltcaesar_lagrangianregions = self.raw_data["ltcaesar"]["lagrangianregions"]
            self.ltcaesar_aboveid = self.raw_data["ltcaesar"]["aboveid"]
            self.ltcaesar_virialradius = self.raw_data["ltcaesar"]["virialradius"]

            try:
                self.code_location = self.raw_data["meta"]["code_location"]
            except:
                self.code_location = "."

            return
        
            
    try:
        with open("parameters.yml", "r") as f:
            parameters = Parameters(f)
    except FileNotFoundError:
        pass

except ModuleNotFoundError:
    pass
