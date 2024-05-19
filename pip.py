# Python PIP

# Check if PIP is Installed
"""
pip --version
"""

# Download a Package
"""
pip install camelcase
"""

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

# Remove a Package
"""
pip uninstall camelcase
"""

# List Packages
"""
pip list
"""
