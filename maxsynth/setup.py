# -*- coding: utf-8 -*-

import setuptools



setuptools.setup(
    name="maxsynth-ilp",
    version="2.0.0",                        # Update this for every new version
    description="Popper",
    include_package_data=True,
    # py_modules=['maxsynth_popper'],
    install_requires=[
        'clingo',
        'pyswip'
    ],                                             
    url="https://github.com/logic-and-learning-lab/Popper",
    packages=["maxsynth_popper"],
    package_dir={"maxsynth_popper": "popper"},
    package_data={"maxsynth_popper": ["uwrmaxsat", "lp/*.pl"]},
    # classifiers=(                                 # Classifiers help people find your
        # "Programming Language :: Python :: 3"    # projects. See all possible classifiers
    # ),
)
