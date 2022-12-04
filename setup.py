from setuptools import setup, find_packages

setup(
    name='snowflake',
    version='0.0.1',
    description='My public snowflake package from private github repo',
    author='Md Shiful Islam',
    author_email='saifulantur@gmail.com',
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
    zip_safe=False
)