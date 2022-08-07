from setuptools import setup, find_packages

from calendric_lib import __version__

import pypandoc

setup(
    name='calendric_lib',
    version=__version__,
    description = "Calendric-lib is a creative package for calendrical conversion operations in Python.",
    long_description = pypandoc.convert('README.md', 'rst'),
    url='https://github.com/saadbinmunir/Calendric-lib.git',
    author='Saad Bin Munir',
    author_email='saadmunir24@gmail.com',

    packages=find_packages(),
)
