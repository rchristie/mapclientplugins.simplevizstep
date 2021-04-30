from setuptools import setup, find_packages
import sys, os, io

# List all of your Python package dependencies in the
# requirements.txt file

def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")

readme = readfile("README.rst")[3:]  # skip title
# For requirements not hosted on PyPi place listings
# into the 'requirements.txt' file.
#requires = readfile("requirements.txt")
requires = [
    # minimal requirements listing
    "opencmiss.zinc >= 3.3",  # not yet on pypi - need manual install from opencmiss.org
    "opencmiss.zincwidgets >= 2.0.2"
]
license = readfile("LICENSE")

setup(name=u'mapclientplugins.simplevizstep',
      version='0.0.0',
      description='',
      long_description=readme + license,
      classifiers=[],
      author=u'Richard Christie',
      author_email='',
      url='',
      license='APACHE',
      packages=find_packages(exclude=['ez_setup',]),
      namespace_packages=['mapclientplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
