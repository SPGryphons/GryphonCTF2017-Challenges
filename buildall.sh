#! /bin/bash
##
# Created for GryphonCTF 2017
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Set a nice option
shopt -s globstar

# Remove previous containers
docker rm -f `docker ps -qa`

# Run all scripts except thee
for script in challenges/**/[br]*.sh; do
    parent=`dirname "${script}"`
    filename=`basename "${script}"`
    cd "${parent}"
    bash ./"${filename}"
    cd -
done

# Print out all containers with port bindings
docker ps --format 'table {{.Names}}\t{{.Ports}}'
