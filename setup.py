from setuptools import setup, find_packages

setup(
    name="GlobalVoiceMakerLib",
    version="0.1.0",
    author="Vessel-Legends",
    url="https://github.com/Vessel-Legends/GlobalVoiceMakerLib",
    description="A library implementation of GlobalVoiceMaker.",
    keywords=['voice-maker', 'library'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.8'
    ],
    python_requires='>=3.7',
    include_package_data=True
)