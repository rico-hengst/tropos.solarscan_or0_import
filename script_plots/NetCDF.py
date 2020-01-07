#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:30:44 2019

@author: bayer
"""
import netCDF4 as nc4
from datetime import datetime
import js

def netCDF_file(d_bts1day,i8date,netCDF_path, cfjson ):
    
    """define the netCDF path where the file should be generated"""
    netCDF_path = "/home/bayer/uv/netCDF/"
    file_out=netCDF_path+str(i8date[:]) + '.nc'
    f = nc4.Dataset(file_out,'w', format='NETCDF4') #'w' stands for write 
    """create dimensions"""    
#    print(len(cfjson['dimensions']))
    print(cfjson['dimensions'])
    print('XXXXXXX')
    print(cfjson['variables'].items())
    print(cfjson['dimensions'].values())
    """Creating the dimensions in the NetCDF file from the JSON file"""
    for x,y in cfjson['dimensions'].items(): 
        if y!=-1:
            f.createDimension(x,y)
            print(f.dimensions)
        elif y==-1:
            f.createDimensions(x,None)
    print(f.dimensions)
    exit()

#The value at object["variables"]["tmp2m"]["data"][k,j,i] is at time[k], latitude[j] and longitude[i]."""
#        f = js.create_cf_file(file_out,cfjson['dimensions'][d]:cfjson['dimensions'].values())#atts=cfjson.attributes, 
#                               dims={'time':d_bts1day["seconds"].size,'longitude':1, 
#                                     'latitude':1, 'wavelength':d_bts1day["wvl"].size})   
    """Building variables"""
    for x in cfjson['variables']:
        f.createVariable(x,cfjson['variables']['type'].values())
        x.data[:]=d_bts1day[x]
        print(f.variables)
#    f.createVariable('time','longitude','latitude','UVA','UVB','uvind','uvint',
#                          'spectrum','wavelength')    
    for v in f.variables.keys():
        if v in cfjson.variables:
            f[v].setncatts(cfjson.variables[v].attributes)
#            if v in d_bts1day.variables:
#                v[:]=d_bts1day[v]
#            print(f.groups)
#            print(f.dimensions)
#            print(f.time)
    f.close()
    
    ###################This should be read from the json file ################
    """creat a group:
    A netCDF group is basically a directory or folder within the netCDF dataset. 
    This allows you to organize data as you would in a unix file system."""
#    uv_grp = f.createGroup('uv_radiometer_data')  
    
    """create dimensions"""
#    uv_grp.createDimension('lon', 1)
#    uv_grp.createDimension('lat', 1)
#    uv_grp.createDimension('time', d_bts1day["seconds"].size)
#    uv_grp.createDimension('wvl', d_bts1day["wvl"].size)
#            
    """Building variables"""
#    time = uv_grp.createVariable('Time', 'i4', 'time')
#    longitude = uv_grp.createVariable('Longitude', 'f4', 'lon')
#    latitude = uv_grp.createVariable('Latitude', 'f4', 'lat') 
#    UVA=uv_grp.createVariable('UVA','f4',('time', 'lon', 'lat'))
#    UVB=uv_grp.createVariable('UVB','f4',('time', 'lon', 'lat'))
#    uvind=uv_grp.createVariable('uvind','f4',('time', 'lon', 'lat'))
#    uvint=uv_grp.createVariable('uint','f4',('time', 'lon', 'lat'))
#    spectrum=uv_grp.createVariable('spectrum','f4',('wvl','time','lon','lat'))
#    wavelength = uv_grp.createVariable('wvl', 'f4', ('wvl','lon','lat'))
#    print(f)
#    print(uv_grp)
#
    """Passing data into variables"""
#    longitude[:]=12.928 
#    latitude[:]=51.526 
#    UVA[:,0,0]=d_bts1day["uva"]
#    UVB[:,0,0]=d_bts1day["uvb"]
#    uvind[:,0,0]=d_bts1day["uvind"]
#    uvint[:,0,0]=d_bts1day["uvint"]
#    wavelength[:,0,0]=d_bts1day["wvl"]
#    spectrum[:,:,0,0]=d_bts1day["spect"]
#    time[:]=d_bts1day["seconds"]
#    
    """adding comments and units"""
#    f.height='80m above see level'
#    today = datetime.today()
#    f.history = "Created " + today.strftime("%d/%m/%y")
#    time.units = 'in UT seconds from zero hours on day given by DATE'
#    UVA.units = 'mW/m²'
#    UVB.units = 'mW/m²'
#    uvind.warning = 'This index depends only on the wavelength!'
#    ###########################################################################
    

