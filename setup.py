"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import py2app.recipes
import py2app.build_app

from setuptools import setup, find_packages

pkgs = find_packages(".")

class recipe_plugin(object):
    @staticmethod
    def check(py2app_cmd, modulegraph):
        local_packages = pkgs[:]
        local_packages += ['pygame']
        return {
            "packages": local_packages,
        }

py2app.recipes.my_recipe = recipe_plugin

APP = ['gridblast.py']
DATA_FILES = []
OPTIONS = {
    'includes':'pygame',
    'iconfile':'gridblast.icns',
    'plist': {
        'NSRequiresAquaSystemAppearance': 0
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    py_modules=['block', 'enemy'],
    packages=pkgs
)
