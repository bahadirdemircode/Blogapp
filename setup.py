import sys
from setuptools import setup

# Genel bağımlılıklar
requirements = [
    "django",
    "gunicorn",
    "asgiref",
    "dj-database-url",
    "django-ckeditor",
    "django-js-asset",
    "pillow",
    "python-dateutil",
    "pytz",
    "sqlparse",
    "termcolor",
    "typing_extensions",
    "tzdata",
    "urllib3",
    "waitress",
]

# Eğer Windows ortamındaysan, pywin32 ve pypiwin32 eklenir
if sys.platform == "win32":
    requirements.append("pywin32")
    requirements.append("pypiwin32")

setup(
    name="blogapp",
    version="1.0",
    install_requires=requirements,
)
