import datetime
import numpy as np
import geojson

def parse_dship(fname, encoding='latin-1', delimiter=';'):
    """Parses WERUM DSHIP data

    """
    f = open(fname,encoding =  encoding)
    # First line is sensors    
    l = f.readline()
    print(l)
    print()
    sensors = l.split(delimiter)
    # Second line is something
    l = f.readline()
    # Third line is units
    l = f.readline()    
    units = l.split(delimiter)    
    data = {}
    header = l[:]
    for i,s in enumerate(sensors):
        print(s)
        data[s] = {'data':[],'unit':units[i]}

    # The index with the time information
    time_ind = 0
    time_fmt = '%Y/%m/%d %H:%M:%S'
    # Now the data begins
    while True:
        d = f.readline()
        if(len(d) == 0):
            break

        ds = d.split(delimiter)
        for i,s in enumerate(sensors):
            # the time axes
            if(i == time_ind):
                ttmp = datetime.datetime.strptime(ds[i],time_fmt)
                data[s]['data'].append(ttmp)
            else:
                try: 
                    dtmp = float(ds[i])
                except:
                    dtmp = np.NaN

                data[s]['data'].append(dtmp)                

    
    return data


def dship2geojson(data,lonkey,latkey):
    """ Writes a geojson file from a parsed dship dataset. Required a the key for latitude and longitude
    """


