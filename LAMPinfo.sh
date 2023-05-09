#!/bin/bash

#Script to display installed Linux, Apache, MySQL, PHP (LAMP) version.

# Output Apache version
echo "Apache version:"
apache2 -v
echo

# Output MySQL version
echo "MySQL version:"
mysql --version
echo

# Output PHP version
echo "PHP version:"
php -v
