"""
Runs the analyse script.
"""

import shared_variables
import subprocess

if shared_variables.parameters.ltcaesar_otherhalofinder:
    halo_catalogue = shared_variables.parameters.halo_catalogue_pickle_name
else:
    halo_catalogue = shared_variables.parameters.halo_catalogue_path

subprocess.call(
    [
        f"{shared_variables.parameters.code_location}/{shared_variables.environment_name}/bin/python",
        "-m",
        "analyse",
        "-i",
        f"{shared_variables.parameters.snapshot_ini}",
        "-f",
        f"{shared_variables.parameters.snapshot_end}",
        "-c",
        f"{halo_catalogue}",
        "-t",
        f"{shared_variables.parameters.ltcaesar_notrunc}",
        "-y",
        f"{shared_variables.parameters.ltcaesar_yt}",
        "-o",
        f"{shared_variables.parameters.ltcaesar_otherhalofinder}",
        "-l",
        f"{shared_variables.parameters.ltcaesar_lagrangianregions}",
    ]
)

