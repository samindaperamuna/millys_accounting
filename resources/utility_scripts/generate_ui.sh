#!/usr/bin/env bash

# Convert the UI files into the corresponding Python file.
fName=null

for path in ../qml/*;
do
    fName=$(basename ${path%.*})
    pyuic5 -o ../../generated/"$fName"'.py' "$path";
done
