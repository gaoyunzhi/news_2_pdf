import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="readee",
    version="0.0.13",
    author="Yunzhi Gao",
    author_email="gaoyunzhi@gmail.com",
    description="Library for export webpage to reader mode html.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaoyunzhi/readee",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'bs4',
        'readability-lxml',
        'telegram_util>=0.0.20'
    ],
    python_requires='>=3.0',
)