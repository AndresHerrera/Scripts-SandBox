import os
from os.path import basename
import shutil
import processing

exportpath =  r'C:\Users\C40-05\Dropbox\DatosFelipeBonilla\Export'
exportpathmagna =  r'C:\Users\C40-05\Dropbox\DatosFelipeBonilla\MagnaCali' 
exportpathmagnasirgas =  r'C:\Users\C40-05\Dropbox\DatosFelipeBonilla\MagnaSirgas' 
data = {}

for dir_entry in os.listdir(exportpath):
    dir_entry_path = os.path.join(exportpath, dir_entry)
    if os.path.isfile(dir_entry_path):
        if dir_entry_path[-11:]=='polygon.shp':
            print(dir_entry_path)
            filename = basename(dir_entry_path).replace(" ", "")
            print(filename)
            projectedFileName =  os.path.join(exportpathmagna, 'Cali'+'_'+filename)
            projectedFileNameMS =  os.path.join(exportpathmagnasirgas, 'MagnaSirgas'+'_'+filename)
            print(projectedFileName)
            salidaRep=processing.runalg('qgis:reprojectlayer', dir_entry_path ,'+proj=tmerc +lat_0=3.441883333 +lon_0=-76.5205625 +k=1 +x_0=1061900.18 +y_0=872364.63 +a=6379137 +b=6357748.961329674 +units=m +no_defs ',projectedFileName)
            print('[OK] REPROJECTED TO MAGNA-CALI')
            salidaRepSirgas=processing.runalg('qgis:reprojectlayer', dir_entry_path ,'+proj=tmerc +lat_0=4.596200416666666 +lon_0=-77.07750791666666 +k=1 +x_0=1000000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ',projectedFileNameMS)
            print('[OK] REPROJECTED TO MAGNA-SIRGAS')