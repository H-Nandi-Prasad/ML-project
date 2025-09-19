from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements_lst=[]
    with open('requirements.txt','r') as file:
        requirements=file.readlines()
        for requirement in requirements:
            requirement=requirement.strip()
            if requirement and requirement!=HYPEN_E_DOT:
                requirements_lst.append(requirement)
    return requirements_lst

setup(
    name='mlproject',
    version='0.0.1',
    author='Nandi',
    author_email='nandiprasadhyati@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)