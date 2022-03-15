from setuptools import setup, find_packages

exec(open('package_cool_name/__version__.py').read())
setup(
    name='package_cool_name',
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    description='A minimal python project to use as cheatsheet for new projects:',
    author='Lorenzo Cerrone',
    url='https://github.com/lorenzocerrone/python-project-cookie-cutter',
    author_email='lorenzo.cerrone@iwr.uni-heidelberg.de',
)