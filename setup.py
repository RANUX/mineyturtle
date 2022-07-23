import setuptools
import re, io

with open("README.md", "r") as fh:
    long_description = fh.read()

# get version from package's __version__
__version__ = re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
        io.open('mineyturtle/__init__.py', encoding='utf_8_sig').read()
    ).group(1)

setuptools.setup(
    name="mineyturtle",
    version=__version__,
    author="Alexander Razzhivin",
    author_email="admin@docode.ru",
    description="The python interface to computertest minetest turtle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RANUX/mineyturtle",
    project_urls={
        "Documentation": "https://github.com/RANUX/mineyturtle"
    },
    packages=["mineyturtle"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment"
    ],
    python_requires='>=3.6',
)