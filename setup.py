import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mesghal-user-provider",  # Replace with your own username
    version="0.0.2",
    author="Ali Modares",
    author_email="s.a.modares.h@gmail.com",
    description="mesghal user model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alimodares2003/ms_user_provider.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyJWT==1.7.1',
    ],
)
