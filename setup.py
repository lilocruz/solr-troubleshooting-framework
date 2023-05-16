from setuptools import setup, find_packages

setup(
    name="Solr-troubleshooting-framework",
    version="0.1",
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
        "Intended Audience :: Developers / Solr & Python Enthusiasts",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GPLv3 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
