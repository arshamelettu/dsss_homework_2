from setuptools import setup

setup(
    name="math_quiz",
    version="1.0",
    py_modules=["math_quiz"],
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="A simple math quiz game",
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz:math_quiz",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
