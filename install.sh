#!/bin/bash

# Global variables
# The package managers supported by this script
SUPPORTED_PMS=("apt-get", "pacman")
# Lists of packages with different names for different distro
PACKAGE_LIST_ARCH=("python-pyqt5" "cowsay")
PACKAGE_LIST_DEB=("python3-pyqt5")
# Name of the package manager
PACM=""
# Update package list, ex. sudo apt-get update
UPDATE_COMMAND="sudo"
# Install package(s), ex. sudo pacman -S python
INSTALL_COMMAND="sudo"
# Check if package is installed
CHECK_COMMAND=""

# Return True if the program is installed
# $1 => possible package manager name
have_installed() {
  [ -x "$(which $1)" ]
}

# Check what package manager is installed
# Assign value to PACM if it contains a empty string
check_package_manager(){
  if [[ "$PACM" == "" ]];then
    for i in ${SUPPORTED_PMS[@]};do
      if have_installed $i > /dev/null 2>&1;then
        PACM="$i"
        break
      fi
    done
  fi
}

# Filter the list of packages
# Then append the missing ones to the install command
# $1 => list of packages
determine_package(){
  local arr=("$@")
  local backup="$INSTALL_COMMAND"
  for i in ${arr[@]};do
    if ! eval "$CHECK_COMMAND $i" > /dev/null 2>&1;then
      INSTALL_COMMAND+=" $i"
    else
      continue
    fi
  done
  # If no missing packages, skip installation
  if [[ "$backup" == "$INSTALL_COMMAND" ]];then
    INSTALL_COMMAND=""
  fi
}

# Determine the install&update&check command according to the pm
determine_command(){
  if [[ "$PACM" == "apt-get" ]];then
    UPDATE_COMMAND+=" apt-get update"
    INSTALL_COMMAND+=" apt-get install"
    CHECK_COMMAND=" dpkg -s"
    determine_package "${PACKAGE_LIST_DEB[@]}"
  elif [[ "$PACM" == "pacman" ]];then
    UPDATE_COMMAND+=" pacman -Syu"
    INSTALL_COMMAND+=" pacman -S"
    CHECK_COMMAND="pacman -Q"
    determine_package "${PACKAGE_LIST_ARCH[@]}"
  else
    echo "error!"
    exit
  fi
}

check_package_manager
determine_command
eval "$INSTALL_COMMAND"
