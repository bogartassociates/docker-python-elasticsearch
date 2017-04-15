from setuptools import setup

setup(
    name='aworan',
    version='0.1',
    py_modules=['aworan'],
    install_requires=[
        'Click',
        'Elasticsearch'
    ],
    entry_points='''
        [console_scripts]
        aworan=aworan:cli
    ''',
)
