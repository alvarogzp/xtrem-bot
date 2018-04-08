from setuptools import setup, find_packages

from xtrem import project_info

setup(
    name=project_info.name,

    use_scm_version=True,

    description=project_info.description,

    url=project_info.url,

    author=project_info.author_name,
    author_email=project_info.author_email,

    license=project_info.license_name,

    packages=find_packages(),

    setup_requires=[
        'setuptools_scm'
    ],

    install_requires=[
        'telegram-bot-framework'
    ],

    python_requires='>=3',
)
