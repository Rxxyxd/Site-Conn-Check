from setuptools import setup, find_packages

setup(
    name='site_conn_check',
    version='1.0.1',
        zip_safe=False,
    author="Joshua Abbey",
    author_email="Joshuaabbey2022@gmail.com",
    description="Package to check status code and response time of websites",
    long_description="A CLI that requests the header of a website to determine its Status Code and response time and visualizes the data in a dataframe",
    packages=["site_conn_check"],
    install_requires=[
        'certifi==2023.5.7',
        'charset-normalizer==3.1.0',
        'decorator==5.1.1',
        'idna==3.4',
        'numpy==1.24.3',
        'pandas==2.0.2',
        'python-dateutil==2.8.2',
        'pytz==2023.3',
        'requests==2.31.0',
        'six==1.16.0',
        'tabulate==0.9.0',
        'tzdata==2023.3',
        'validators==0.20.0',
    ],
    license='LICENCE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            # command 
            'site_conn_check = site_conn_check.main:main',
        ]
    }
)