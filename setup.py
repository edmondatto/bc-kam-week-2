try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name="dojo",
    version="0.0.1",
    description='An application that automatically assigns random office & living spaces to new Andela staff & fellows',
    url="https://github.com/edmondatto/bc-kam-week-2",
    author="Edmond B. Atto",
    install_requires=['docopt'],
    packages=['app'],
    py_modules=['welcome'],
    entry_points={
        'console_scripts': [
            'dojo=app.main',
        ],
    },
    classifiers=(
        'Intended Audience :: Andela',
        'Natural Language :: English',
        'Programming Language :: Python'
        'Programming Language :: Python :: 3.6',
    ),
)
