# Shared library for common functionality
# This module can be imported by other parts of the application
# to provide shared utilities and classes.

from .dbconnection import DatabaseConnection

# Expose key classes and functions at package level
__all__ = ['DatabaseConnection']