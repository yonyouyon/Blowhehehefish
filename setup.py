"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP_NAME = 'Blowfish'
APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'static/blowfish.icns'
}

setup(
    app=APP,
    name = APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)