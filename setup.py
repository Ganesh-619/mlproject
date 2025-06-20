from setuptools import find_packages,setup

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)-> list[str]:

    "this function will return the requirements as list"
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements
]
        
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements        
        





setup(
    name='mlproject',
    version='0.1',
    author='ganesh',
    author_email='lunavathganesh415@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[]  # or use get_requirements() if defined
)
