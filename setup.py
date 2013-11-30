import os

from setuptools import setup, find_packages

version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.txt')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''

long_description = (
    README
    + '\n'
    + CHANGES
    + '\n'
)

requires = []

entry_points = {
    'console_scripts': [
        'miraclelight = miraclelight:run',
    ],
}

setup(
    name='miraclelight',
    version=version,
    description="Testing With Precure.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='',
    author='Jiro Nejime',
    author_email='neji@drillbits.jp',
    url='https://github.com/drillbits/miraclelight',
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points=entry_points,
)
