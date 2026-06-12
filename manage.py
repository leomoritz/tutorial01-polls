#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""
Um utilitário de linha de comando que permite a você interagir com esse projeto Django de várias maneiras.
Você pode ler todos os detalhes sobre o manage.py em https://docs.djangoproject.com/pt-br/6.0/ref/django-admin/
"""
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
