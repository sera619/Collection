import sys
import os
from cx_Freeze import setup, Executable

files = ['DigitalClock.py','digital-7.ttf', 'icon.ico']

target = Executable(script='DigitalClock.py',
                    base = 'Win32GUI',
                    icon = 'icon.ico')

setup(
    name='DigitalClock',
    version='1.0.1',
    description="A small Stopwatch and clock for Microsoft Windows 10/11.",
    author="S3R43o3",
    copyright="S3R43o3",
    options={'build_exe': {'include_files': files}},
    executables= [target]
)