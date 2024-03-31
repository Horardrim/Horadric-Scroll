from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='Horadric Scroll',
    version='1.0.0',
    description='Practice of leet code with python.',
    long_description=readme,
    author='TalRasha',
    author_email='524948250@qq.com',
    url='https://github.com/Horardrim/Horadric-Scroll',
    license='',
    install_requires= [
        'setuptools>=69.2.0'
    ],
    packages=find_packages(
        where='.',
        exclude=('tests')
    )
)
