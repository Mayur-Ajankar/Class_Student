#mL aplicaion as a package 

from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    
    """
    this function will return th list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name='class_student',
    version='0.0.1',
    author='Mayur',
    author_email='mayurajankar151998@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)