import h5py

filepath = 'test.h5'

f = h5py.File(filepath, 'r+')

layer_names = ['layer_' + str(i) for i in range(10)]

f.attrs['layer_names'] = layer_names

f.close()