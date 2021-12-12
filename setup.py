from setuptools import setup, find_packages

setup(
    name='vnstock_data',
    version='0.1',
    author='Vu Thanh Dat',
    author_email='vuthanhdat.contact@gmail.com',
    description='A package for accessing Vietnam stock market data',
    long_description='',
    long_description_content_type="text/markdown",
    url='https://github.com/vuthanhdatt/vnstock-data-python',
    project_urls = {
        "Bug Tracker": "https://github.com/vuthanhdatt/vnstock-data-python/issues"
    },
    license='MIT',
    packages=find_packages(),
    install_requires=['requests','beautifulsoup4','pandas'],
)