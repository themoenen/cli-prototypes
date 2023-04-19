from setuptools import setup

setup(
    name='ibmad',  # Package name
    version='0.1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'ibmad = main:ibmad',  # <cli-command> = <filename>:<main-function>
        ],
    },
)
