from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except IOError:
    README = ''

version = "0.0.2"

setup(
    name='tgext.rq',
    version=version,
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='turbogears2.extension',
    author='Leonardo Baptista',
    author_email='leonardoobaptistaa@gmail.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages = ['tgext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "TurboGears2 >= 2.0",
        "rq >= 1.0"
    ],
    entry_points={
        'gearbox.commands': [
            'rq = tgext.rq.commands:RQCommand'
        ],
    },
)
