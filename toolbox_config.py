#!/usr/bin/env python

from colorama import*

import os
import json

config = {
    "couleur": Fore.MAGENTA,
    "command_colors": Fore.RED,
    "entry":">>>"
}

with open("toolbox_config.json", "w+") as json_file:
    json.dump(config, json_file)
