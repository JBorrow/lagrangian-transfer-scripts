"""
Runs the analyse script.
"""

import shared_variables
import subprocess

subprocess.call(
    [
        f"{shared_variables.environment_name}/bin/python",
        "-m",
        "analyse",
        "-i",
        shared_variables.parameters.snapshot_ini,
        "-f",
        shared_variables.parameters.snapshot_end,
        "-c",
        shared_variables.parameters.halo_catalogue_path,
        "-t",
        shared_variables.parameters.ltcaesar_notrunc,
        "-y",
        shared_variables.parameters.ltcaesar_yt,
        "-o",
        shared_variables.parameters.ltcaesar_otherhalofinder,
        "-l",
        shared_variables.parameters.ltcaesar_lagrangianregions,
        "-a",
        shared_variables.parameters.ltcaesar_aboveid,
        "-r",
        shared_variables.parameters.ltcaesar_virialradius
    ]
)

