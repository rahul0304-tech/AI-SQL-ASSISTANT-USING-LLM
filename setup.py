from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).parent
REQUIREMENTS = BASE_DIR / 'requirements.txt'
README = BASE_DIR / 'README.md'

def get_requirements():
    """Get requirements from requirements.txt file."""
    with open(REQUIREMENTS) as f:
        requirements = []
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if line and not line.startswith('#'):
                # Remove version specifiers
                req = line.split('>=')[0].strip()
                requirements.append(req)
        return requirements

def get_long_description():
    """Get long description from README.md file."""
    with open(README, encoding='utf-8') as f:
        return f.read()

setup(
    name='sql_assistant',
    version='0.1.0',
    description='An AI-powered SQL assistant using LangChain and various data sources',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/sql_assistant',
    packages=find_packages(exclude=['tests*']),
    install_requires=get_requirements(),
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.9.0',
            'flake8>=6.1.0',
            'isort>=5.12.0',
            'mypy>=1.5.0',
            'pre-commit>=3.4.0',
        ],
    },
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    include_package_data=True,
    package_data={
        'sql_assistant': [
            'prompts/*.yaml',
        ],
    },
)