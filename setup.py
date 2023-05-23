from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = 'Simple Python module to access PCIe devices'
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Setting up
setup(
    name="pyPCIe",
    version=VERSION,
    author="Heiko Engel",
    author_email="<heikoengel@users.noreply.github.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/heikoengel/pyPCIe",
    install_requires=[],
    keywords=['python', 'pcie'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ]
)
