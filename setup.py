import os
from io import open
from setuptools import setup


# Load package info, without importing the package
basedir = os.path.dirname(os.path.abspath(__file__))
package_info_path = os.path.join(basedir, "dwave", "inspector", "package_info.py")
package_info = {}
try:
    with open(package_info_path, encoding='utf-8') as f:
        exec(f.read(), package_info)
except SyntaxError:
    execfile(package_info_path, package_info)


# Package requirements, minimal pinning
install_requires = [
    'dimod>=0.8.17',
    'dwave-system>=0.8.1',
    'dwave-cloud-client>=0.6.2',
    'Flask>=1.1.1',
]

# Package extras requirements
extras_require = {
    'test': ['coverage', 'mock'],

    # backports
    ':python_version < "3.7"': ['importlib_resources']
}

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

packages = ['dwave', 'dwave.inspector']

setup(
    name=package_info['__package_name__'],
    version=package_info['__version__'],
    author=package_info['__author__'],
    author_email=package_info['__author_email__'],
    description=package_info['__description__'],
    long_description=open('README.rst', encoding='utf-8').read(),
    url=package_info['__url__'],
    license=package_info['__license__'],
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=classifiers,
    zip_safe=False,
)
