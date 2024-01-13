from setuptools import setup, find_packages

setup(
    name='api_raizen',
    version='1.0.0',
    description='Test code for Raizen based on Flask-RESTPlus',
    url='https://github.com/sousachris/raizen',
    author='Christian Carvalho',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1'],
)