from setuptools import find_packages,setup 
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(path) as f:
        requirements= f.readlines()
        requirements = [i.replace("\n","") for i in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name = 'mlproject',
    version = '0.0.1',
    author='DevJebez',
    author_email='jebezoswald.2965@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)
