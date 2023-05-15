from setuptools import setup

setup(
    name='solr_troubleshooting_framework',
    version='0.1',
    description='A simple but useful Apache Solr troubleshooting framework to start debuggin Apache Solr installation and settings issues.',
    url='https://github.com/lilocruz/solr-troubleshooting-framework',
    author='Michael Sanchez, Search Engineer @lucidworks',
    author_email='superlinux.michael5@gmail.com',
    license='GPLv3',
    packages=['stsf'],
    install_requires=[
        'requests',
    ],
    zip_safe=False
)