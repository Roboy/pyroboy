from setuptools import setup

setup(
    name='pyroboy',
    version='0.0.1',
    packages=['pyroboy'],
    py_modules=[],
    install_requires=['setuptools'],
    author='Alona Kharchenko',
    author_email='unicorn@roboy.org',
    maintainer='Alona Kharchenko',
    maintainer_email='unicorn@roboy.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD-3 License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Package containing Roboy interfaces.',
    license='BSD-3 License',
    test_suite='test',
    entry_points={
        # 'console_scripts': [
        #     'listener_py = listener_py:main',
        #     'talker_py = talker_py:main',
        # ],
    },
)
