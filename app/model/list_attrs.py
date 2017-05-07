import h5py


def replace(left, right):
    data = left
    data[...] = right

filepath = 'test.h5'

f = h5py.File(filepath, 'r')

filepath = 'dummy_weights.h5'
g = h5py.File(filepath, 'r+')

# g['dense_1']['dense_1/kernel:0'] = f['layer_0']['param_0']
# g['dense_1']['dense_1/bias:0'] = f['layer_0']['param_1']
# g['dense_2']['dense_2/kernel:0'] = f['layer_3']['param_0']
# g['dense_2']['dense_2/bias:0'] = f['layer_3']['param_1']
# g['dense_3']['dense_3/kernel:0'] = f['layer_5']['param_0']
# g['dense_3']['dense_3/bias:0'] = f['layer_5']['param_1']
# g['dense_4']['dense_4/kernel:0'] = f['layer_8']['param_0']
# g['dense_4']['dense_4/bias:0'] = f['layer_8']['param_1']

replace(g['dense_1']['dense_1/kernel:0'], f['layer_0']['param_0'])
replace(g['dense_1']['dense_1/bias:0'], f['layer_0']['param_1'])
replace(g['dense_2']['dense_2/kernel:0'], f['layer_3']['param_0'])
replace(g['dense_2']['dense_2/bias:0'], f['layer_3']['param_1'])
replace(g['dense_3']['dense_3/kernel:0'], f['layer_5']['param_0'])
replace(g['dense_3']['dense_3/bias:0'], f['layer_5']['param_1'])
replace(g['dense_4']['dense_4/kernel:0'], f['layer_8']['param_0'])
replace(g['dense_4']['dense_4/bias:0'], f['layer_8']['param_1'])

f.close()
g.close()
