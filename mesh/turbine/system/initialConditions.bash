#!/bin/bash

diameter=0.22000 #m
radius=0.11000 #m
rotating_speed=1000 #rpm
rotor="turbine_rotor"

xMin=$(echo "5.0 * $diameter" | bc)
yMin=$(echo "5.0 * $diameter" | bc)
zMin=$(echo "5.0 * $diameter" | bc)

xMax=$(echo "15.0 * $diameter" | bc)
yMax=$(echo "5.0 * $diameter" | bc)
zMax=$(echo "5.0 * $diameter" | bc)

