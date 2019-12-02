import xarray as xr
import numpy as np


def test_xarray_open_bad_path_fail():
    fpath = '/badc/cmip5/data/cmip5/output1/MOHC/HadGEM2-ES/historical/mon/land/Lmon/r1i1p1/latest/rh/rh_Lmon_-190911.nc'

    try:
    	ds = xr.open_dataset(fpath)
    except IOError as exc:   #was FileNotFoundError
        pass


def test_xarray_open_good_path_success():
    fpath = '/badc/cmip5/data/cmip5/output1/MOHC/HadGEM2-ES/historical/mon/land/Lmon/r1i1p1/latest/rh/rh_Lmon_HadGEM2-ES_historical_r1i1p1_193412-195911.nc'
    ds = xr.open_dataset(fpath)


def test_create_and_save_netcdf_file_bad_dimension_length():
	try:
		ds = xr.Dataset({'test': (('x', 'y'), np.random.rand(4,4,5))},
                    coords={'x': [1,2,3, 4],
                            'y': [1,2,3,4],
                            'z': [1900-01-01, 1900-02-01, 1900-03-01, 1900-04-01, 1900-05-01]})
		ds.to_netcdf('example_dataset.nc')
	except ValueError as exc:
		pass


def test_create_and_save_netcdf_file_correct_dimension_length():        
	ds = xr.Dataset({'test': (('x', 'y', 'z'), np.random.rand(4,4,5))},
                    coords={'x': [1,2,3,4],
                            'y': [1,2,3,4],
                            'z': [1,2,3,4,5]})
        
	ds.to_netcdf('example_dataset.nc')
