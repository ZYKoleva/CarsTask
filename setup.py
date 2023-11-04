from setuptools import setup, find_packages

setup(
    name='cars',
    version='0.1.0',
    entry_points={
        'console_scripts': ['run-app=app.main:run']
    },
    packages=find_packages(include=['app', 'utils']),
    package_data={'config': ['*.yaml'], 'raw_data': ['cars.json'], 'output': ['*.csv'], 'logs': ['*.log']},
    install_requires=[
        'numpy==1.26.1',
        'pandas==2.1.2',
        'pyaml==23.5.8',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'PyYAML==6.0.1',
        'six==1.16.0',
        'tzdata==2023.3'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)