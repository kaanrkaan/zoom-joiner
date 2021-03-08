from distutils.core import setup
import py2exe, webbrowser, datetime, time, os, sys

setup(
    options = {'py2exe': {'bundle_files': 3, 'compressed': True}},
    console = [{
        "script":"zoomj.py",
        "icon_resources": [(1,"app.ico")],
    }],
    zipfile = None
)