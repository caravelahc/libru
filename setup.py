from setuptools import find_packages, setup

setup(
    name='libru',
    version='0.1.2',
    packages=find_packages(exclude=['tests']),

    description='',
    url='https://github.com/caravelahc/libru',

    author='Caio Pereira Oliveira',
    author_email='caiopoliveira@gmail.com',

    license='GPL-3.0',

    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
    ),

    install_requires=[
        'requests',
        'pytz',
        'bs4',
        'lxml',
    ],

    entry_points={
        'console_scripts': ['ru=libru.cli:cli'],
    },
)
