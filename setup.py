import setuptools

setuptools.setup(
    name="nb_simple_speech",
    packages=['simple_speech'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'notebook'
    ],
    zip_safe=False
)