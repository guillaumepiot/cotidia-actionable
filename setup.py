import os

from setuptools import find_packages, setup


def package_files(dirs):
    paths = []
    for directory in dirs:
        for (path, directories, filenames) in os.walk(directory):
            # Only keep the last directory of the path
            path = path.replace(directory, directory.split("/")[-1])
            for filename in filenames:
                paths.append(os.path.join(path, filename))
    return paths

template_files = package_files([
    'cotidia/actionable/templates',
    'cotidia/actionable/static'
])

setup(
    name="cotidia-actionable",
    description="Actionable task plugin for Cotidia Admin.",
    version="1.1",
    author="Guillaume Piot",
    author_email="guillaume@cotidia.com",
    url="https://code.cotidia.com/cotidia/actionable/",
    packages=find_packages(),
    package_dir={'actionable': 'actionable'},
    package_data={
        'cotidia.actionable': template_files
    },
    namespace_packages=['cotidia'],
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
)
