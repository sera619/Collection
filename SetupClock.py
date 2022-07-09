import sys
import os
from cx_Freeze import setup, Executable
from DigitalClock import version

files = ['DigitalClock.py','digital-7.ttf', 'icon.ico']

target = Executable(script='DigitalClock.py',
                    base = 'Win32GUI',
                    icon = 'icon.ico')

setup(
    name='DigitalClock',
    version=version,
    description="A small Stopwatch and clock for Microsoft Windows 10/11.",
    author="S3R43o3",
    copyright="S3R43o3",
    options={'build_exe': {'include_files': files}},
    executables= [target]
)