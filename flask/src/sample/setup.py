from setuptools import setup

setup(
    name='api',
    packages=['api'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'SQLAlchemy',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'Flask-Marshmallow',
        'PyMySQL',
        'marshmallow',
        'marshmallow-sqlalchemy',
        'flask-marshmallow',
    ],
    zip_safe=False,
)
