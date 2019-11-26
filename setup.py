from setuptools import setup

setup(
    name='NovaBox',
    version='1.0.0',
    description='',
    url='https://github.com/supernova-project/nova-toolbox',
    author='p01arst0rm',
    author_email='polar@ever3st.com',
    license='MIT',
    packages=[
        'Toolbox'
    ],
    install_requires=[
        'gitoython'
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    zip_safe=False)