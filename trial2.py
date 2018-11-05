# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:29:31 2018

@author: amith.ms
"""

import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import os
from stl.mesh import Mesh
from stl.base import BaseMesh
from stl.base import RemoveDuplicates
cwd = os.getcwd()


def test_remove_all_duplicate_polygons():
    
    

    mesh = Mesh(your_mesh, remove_duplicate_polygons=False)
    assert mesh.data.size == 9
    Mesh.remove_duplicate_polygons(mesh.data, RemoveDuplicates.NONE)

    mesh = Mesh(your_mesh, remove_duplicate_polygons=RemoveDuplicates.ALL)
    assert mesh.data.size == 9

    assert (your_mesh.points[0][0:3] == your_mesh.v0[0]).all()
    assert (your_mesh.points[0][3:6] == your_mesh.v1[0]).all()
    assert (your_mesh.points[0][6:9] == your_mesh.v2[0]).all()
    



#def test_valid_ascii(tmpdir, speedups):
#    tmp_file = 'pistons1.stl'
#    with open(tmp_file,'w+') as fh:
#        fh.write(tmp_file)
#        fh.seek(0)
#        mesh.Mesh.from_file(str(tmp_file), fh=fh, speedups=speedups)
#    
#test_valid_ascii(cwd, 'speedups')        
#        
#def zero_runs(a):  # from link
#    iszero = np.concatenate(([0][0], np.equal(a, 0).view(np.int8), [0]))
#    absdiff = np.abs(np.diff(iszero))
#    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
#    return ranges

# Using an existing stl file:
your_mesh = mesh.Mesh.from_file("pistons.stl")
Mesh.remove_duplicate_polygons(mesh.data, RemoveDuplicates.NONE)
mesh = Mesh(your_mesh, remove_duplicate_polygons=RemoveDuplicates.ALL)



# =============================================================================
# To Plot the object using mathplotlib
# =============================================================================
# Create a new plot
#figure = pyplot.figure()
#axes = mplot3d.Axes3D(figure)
#
## Load the STL files and add the vectors to the plot
##axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors[0:3500][:][:]))
#axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors[0:2000][:][:],edgecolor='k'))
#
## Auto scale to the mesh size
#scale = your_mesh.points.flatten(-1)
#axes.auto_scale_xyz(scale, scale, scale)
#
## Show the plot to the screen
#pyplot.show()
#runs = zero_runs(np.diff(your_mesh))
# =============================================================================
# 
# =============================================================================



#print(your_mesh.points)# mesh points
#X=your_mesh.x
#Y=your_mesh.y
#Z=your_mesh.z
#
#data=np.column_stack((X[:][0],Y[:][0],Z[:][0]))
#figure = pyplot.figure()
#axes = mplot3d.Axes3D(figure)
#
#axes.add_collection3d(mplot3d.art3d.Poly3DCollection(data.vectors))
#
## Auto scale to the mesh size
#scale = your_mesh.points.flatten(-1)
#axes.auto_scale_xyz(scale, scale, scale)
#
## Show the plot to the screen
#pyplot.show()
#
#X=your_mesh.x
#X=X.flatten()
#
#Y=your_mesh.y
#Y=Y.flatten()
#
#Z=your_mesh.z
#Z=Z.flatten()
#
#
## =============================================================================
## To print all coordinates,  As show in pdf
## =============================================================================
##for i,j,k in zip(X,Y,Z):
##    print(i,j,k)
#
## =============================================================================
## To save all coordinates , an optimized way
## =============================================================================
#
#data=np.column_stack((X,Y,Z))
##print(data)
#np.savetxt('data.csv', data, fmt='%.8f', delimiter=',', header=" #X,  #Y,  #Z")## to strore the vertices of the model in csv file