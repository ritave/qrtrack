from setuptools import setup, find_packages

# No need to duplicate requirements in both files
with open('requirements.txt') as f:
    required = f.read().splitlines()
    required.remove('-e .')

setup(
    name='qrtrack',
    version='0.0.1.dev',
    author='QRTrackTeam',
    install_requires=required,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'qrtrack-deploy = qrtrack.deployment.deploy:main'
        ]
    }
)