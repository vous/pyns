from distutils.core import setup

setup(
    name='PyNS',
    version='0.1.1',
    author='Vous',
    author_email='maarja@outlook.com',
    packages=['pyns'],
    url='#',
    license='LICENSE.txt',
    description='A Wrapper for the Nation States API',
    long_description=open('README.txt').read(),
    install_requires=["mechanize", "beautifulsoup4"
    ],
)