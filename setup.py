from setuptools import setup

setup(name='alleles_fixation',
        version='1.0',
        description='A GUI program simulates alleles fixation',
        url='https://github.com/lorix-lpan/alleles-fixation',
        author='Lawrence Fei Pan',
        author_email='lawrence_pan@hot-shot.com',
        license='GPLv3',
        packages=['alleles_fixation'],
        install_requires=[
            'random',
            'PyQt5.QtWidgets'
        ],
        zip_safe=False)
