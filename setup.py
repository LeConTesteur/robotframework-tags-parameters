import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    'robotframework',
    'pyaml',
    'argparse-from-jsonschema'
]

requirements_tests = [
    "requests_mock",
    "flake8",
    "coverage"
]

extras = {
    'tests': requirements_tests,
}

setuptools.setup(
    name="robotframework-tags-parameters",
    version="0.0.2",
    author="LeConTesteur",
    description="Can use and parse parameters from robotframework test tags",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeConTesteur/robotframework-tags-parameters",
    project_urls={
        "Bug Tracker": "https://github.com/LeConTesteur/robotframework-tags-parameters/issues",
    },
    classifiers=[ "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"],
    package_dir={"": "robotframework_tags_parameters"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = requirements,
    tests_require = requirements_tests,
    extras_require = extras,

)
