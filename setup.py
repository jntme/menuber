from setuptools import setup, find_packages

NAME = "menuber"
DESCRIPTION = "Making cli menuing easier."

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='%s' % NAME,
    version='0.0.1',
    description=DESCRIPTION,
    long_description=readme,
    author='Jonathan Meier',
    author_email='mail@jntme.ch',
    url='https://github.com/jntme/%s' % NAME,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)