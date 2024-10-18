# from conda_build.skeletons.pypi import get_requirements
# from pkg_resources import require
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements from a requirements file
    '''
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("/n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'elpapx',
    author_email = 'n00058329@upn.pe',
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')
)