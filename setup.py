import setuptools

setuptools.setup(
    name='cars-app',
    version='0.0.1',
    entry_points={
        'console_scripts': ['run-app=app.main:run']
    },
    packages=setuptools.find_packages(include=['app', 'utils', 'test']),
    package_data={'config': ['*.yaml'], 'raw_data': ['cars.json'], 'output': ['*.csv'], 'logs': ['*.log']},
    install_requires=[
        'numpy==1.21.6',
        'pandas==1.3.5',
        'python-dateutil==2.8.2',
        'pytz==2022.1',
        'PyYAML==5.4.1',
        'six==1.16.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)