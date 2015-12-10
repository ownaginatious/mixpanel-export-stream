from distutils.core import setup

setup(
    name='mixpanel_export',
    packages=['mixpanel_export'],
    version='0.2',
    description='A streaming library for reading raw event data from Mixpanel\'s export API',
    author='Dillon Dixon',
    author_email='dillondixon@gmail.com',
    url='https://github.com/ownaginatious/mixpanel-export-stream',
    download_url='https://github.com/ownaginatious/mixpanel-export-stream/tarball/0.1',
    license='MIT',
    keywords=['mixpanel', 'export', 'stream'], # arbitrary keywords
    classifiers=[],
    install_requires=[
        'requests'
    ]
)
