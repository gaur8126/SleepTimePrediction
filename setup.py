from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:

    requirements  = []

    with open(file_path) as obj_file:
        requirements = obj_file.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# if __name__ == "__main__":
#     file_path = "requirements.txt"
#     print(get_requirements(file_path))



setup(
    name="sleeltimeprediction",
    version='0.0.1',
    author='Lokesh',
    author_email='gaurlokesh1211@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)