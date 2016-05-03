from setuptools import setup, find_packages
from io import open
import versioneer

setup(
    name='mixpanel_export',
    packages=find_packages(exclude=["tests"]),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='A streaming library for reading raw event '
                'data from Mixpanel\'s export API',
    author='Dillon Dixon',
    author_email='dillondixon@gmail.com',
    url='https://github.com/ownaginatious/mixpanel-export-stream',
    license='MIT',
    keywords=['mixpanel', 'export', 'stream'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    install_requires=[line.strip()
                      for line in open("requirements.txt", "r",
                                       encoding="utf-8").readlines()],
)
