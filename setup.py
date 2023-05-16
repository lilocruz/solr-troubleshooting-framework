from setuptools import setup, find_packages

setup(
    name="stsf",
    version="0.1.5",
    url='https://github.com/lilocruz/solr-troubleshooting-framework',
    author="Michael Cruz Sanchez",
    author_email="superlinux.michael5@gmail.com",
    license='GPLv3',
    description="A Python module for troubleshooting Apache Solr installations",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
)
