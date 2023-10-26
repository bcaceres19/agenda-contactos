from setuptools import setup, find_packages

setup(
    name='agenda-de-contactos',
    version='0.0.1',
    description='En este repositorio, encontrarás una aplicación de código abierto diseñada para gestionar y organizar tus contactos telefónicos de manera eficiente.',
    author_1='Brahian Caceres',
    author_email_1='bacg20044@gmail.com',
    author_2='',
    author_email_2='',
    url='https://github.com/bcaceres19/agenda-contactos.git',
    packages=find_packages(),
    install_requires=[
        'pip',
        'packaging'
    ],
    entry_points={
        'console_scripts': [
            'pip install -r requirements.txt = agenda-contactos:Compilar todas las dependencias para el proyecto',
            'pip-compile = agenda-contactos:Compilar el requirements.in por si hay nuevas dependencias'
        ],
    },
)
