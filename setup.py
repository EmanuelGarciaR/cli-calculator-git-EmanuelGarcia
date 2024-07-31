from setuptools import setup

setup(
    name='cli-calculator-git-EmanuelGarcia',
    version='0.1',
    packages=['app', 'tests'],
    url='',
    license='MIT License',
    author='Emanuel Garcia Rios',
    author_email='emanuelgarciarios@gmail.com',
    description='A simple CLI Calculator',

    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        calc=app.calculator:calc
    '''
)