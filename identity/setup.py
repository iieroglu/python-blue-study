from setuptools import find_packages, setup
setup(
    name='identity',
    packages=find_packages(include=['identity']),
    version='0.1.0',
    description='identity library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)