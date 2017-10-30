import numpy as np

#Converts from Latitude (degrees), Longitude (degrees), Altitude(meters) into 3D cartisian X,Y,Z points
#Assumes WGS-84 GPS semi-major and semi-minor axis values

def LLAtoXYZ(lat,lon,alt,major=6378137,minor=6356752.3142):
    phi_ = np.radians(lat)
    lambda_ = np.radians(lon)
    e2_ = ((major**2)-(minor**2))/(major**2)
    v_ = major/(np.sqrt(1-(e2_*(np.sin(phi_)**2))))
    x = (v_+alt)*(np.cos(phi_)*np.cos(lambda_))
    y = (v_+alt)*(np.cos(phi_)*np.sin(lambda_))
    z = (((1-e2_)*v_)+alt)*np.sin(phi_)
    return x,y,z
