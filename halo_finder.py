"""
Runs the halo finder if required, else runs the correct script to parse it.
"""

import shared_variables
import subprocess

if shared_variables.parameters.halo_catalogue_run_caesar:
    subprocess.call(["caesar", shared_variables.parameters.snapshot_end])


if shared_variables.parameters.halo_catalogue_type == "velociraptor":
    subprocess.call(
        [
            f"{shared_variables.parameters.code_location}/{shared_variables.environment_name}/bin/python",
            f"{shared_variables.parameters.code_location}/lagrangian-transfer/scripts/parse_halo_centers_velociraptor.py",
            shared_variables.parameters.snapshot_end,
            shared_variables.parameters.halo_catalogue_path,
            shared_variables.parameters.halo_catalogue_pickle_name,
        ]
    )
elif shared_variables.parameters.halo_catalogue_type == "velociraptor-particles":
    # For this you need to have ran the tools available at
    # https://github.com/JBorrow/simba-velociraptor-tools
    subprocess.call(
        [
            f"{shared_variables.parameters.code_location}/{shared_variables.environment_name}/bin/python",
            f"{shared_variables.parameters.code_location}/lagrangian-transfer/scripts/parse_velociraptor.py",
            shared_variables.parameters.halo_catalogue_path,
            shared_variables.parameters.snapshot_end,
            shared_variables.parameters.halo_catalogue_pickle_name,
        ]
    )
elif shared_variables.parameters.halo_catalogue_type == "ahf":
    subprocess.call(
        [
            f"{shared_variables.parameters.code_location}/{shared_variables.environment_name}/bin/python",
            f"{shared_variables.parameters.code_location}/lagrangian-transfer/scripts/parse_halo_centers.py",
            shared_variables.parameters.snapshot_end,
            shared_variables.parameters.halo_catalogue_path,
            shared_variables.parameters.halo_catalogue_pickle_name,
        ]
    )
elif shared_variables.parameters.halo_catalogue_type == "caesar":
    pass
else:
    raise AttributeError(
        "Please pass to halo_catalogue:type velociraptor, ahf, or caesar"
    )
