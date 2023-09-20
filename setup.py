import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    'robotframework',
    'robotframework-jsonlibrary',
    'pyaml',
    'argparse-from-jsonschema >= 0.0.5'
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
    version="0.0.3",
    author="LeConTesteur",
    description="Can use and parse parameters from robotframework test tags",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeConTesteur/robotframework-tags-parameters",
    project_urls={
        "Bug Tracker": "https://github.com/LeConTesteur/robotframework-tags-parameters/issues",
    },
    classifiers=[ "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"],
    package_dir={"TagsParameters": "robotframework_tags_parameters"},
    packages={"TagsParameters"},
    python_requires=">=3.8",
    install_requires = requirements,
    tests_require = requirements_tests,
    extras_require = extras,

)
