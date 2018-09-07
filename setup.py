import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='sandboxcli',
        version='0.0.1',
        packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': [
                'sandboxcli=sandboxcli.main:main',
            ],
        },
    )
