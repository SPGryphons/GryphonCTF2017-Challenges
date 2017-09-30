#! /bin/bash
##
# Created for GryphonCTF 2017 Genesis
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Script misc
SCRIPT=`readlink -f "$0"`
SCRIPTPATH=`dirname "${SCRIPT}"`
cd $SCRIPTPATH

# Build image
docker build -t genesis .

# Return directory
cd -
