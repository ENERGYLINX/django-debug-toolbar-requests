import sys
import subprocess
import shlex
from setuptools import find_packages, setup

import requests_toolbar

version = requests_toolbar.__versionstr__

# release a version, publish to GitHub and PyPI
if sys.argv[-1] == 'publish':
    command = lambda cmd: subprocess.check_call(shlex.split(cmd))
    command('git tag v' + version)
    command('git push --tags origin master:master')
    command('twine upload --repository-url https://upload.pypi.org/legacy/ dist/*')
    sys.exit()


setup(
    name='django-debug-toolbar-requests',
    version=version,
    packages=find_packages(),
    url='https://github.com/ENERGYLINX/django-debug-toolbar-requests',
    license=open('LICENSE').read(),
    author='Martin Voldrich',
    author_email='rbas.cz@gmail.com',
    description='Adds requests debuging information',
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Environment :: Web Environment'
    ]
)
