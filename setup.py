from setuptools import setup

setup(
    name="math_quiz",
    version="1.0",
    py_modules=["math_quiz"],
    author="arshamelettu",
    author_email="arshamelettu@gmail.com",
    description="A simple math quiz game",
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz:math_quiz',  
        ],
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
