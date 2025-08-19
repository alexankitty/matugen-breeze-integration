#!/bin/env python3
import configparser
from pathlib import Path
import sys

kdeglobalpath = Path.home() / ".config/kdeglobals"
colortemplate = Path(__file__).parent.resolve() / "kde_colors"

sections = [
    "Colors:Buttons",
    "Colors:Complementary",
    "Colors:Header",
    "Colors:Selection",
    "Colors:Tooltip",
    "Colors:View",
    "Colors:Window",
    "General"
    ]

vars = [
    "DecorationFocus",
    "DecorationHover",
    "ForegroundActive",
    "AccentColor",
    "LastUsedCustomAccentColor"
]

config = configparser.ConfigParser()
config.optionxform = str
config.read(kdeglobalpath)

with open(colortemplate, "r") as f:
    color = f.read().strip()

for section in config.sections():
    for option in config[section]:
        if option in vars:
            config[section][option] = color
        if section == "Colors:Selection":
            if option == "BackgroundNormal":
                config[section][option] = color

with open(kdeglobalpath, "w") as configfile:
    config.write(configfile, space_around_delimiters=False)

