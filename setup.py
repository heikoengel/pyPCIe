from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Simple Python module to access PCIe devices'
LONG_DESCRIPTION = ""

# Setting up
setup(
        name="PyCIe",
        version=VERSION,
        author="Heiko Engel",
        author_email="<heikoengel@users.noreply.github.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'pcie'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX :: Linux",
        ]
)
