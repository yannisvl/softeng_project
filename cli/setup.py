from setuptools import setup


setup(
        name='energy_app',
        version='1.0',
        py_modules=['energy_group044'],
        install_requires=[
            'Click',
        ],
        entry_points='''
            [console_scripts]
            energy_group044=energy_group044:cli
        ''',

)

