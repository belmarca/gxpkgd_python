from setuptools import setup

setup(
    name='gxpkgd_python',
    packages=['gxpkgd_python'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-ponywhoosh',
        'gunicorn',
        'python-dotenv',
        'requests',
        'sexpdata'
    ]
)
