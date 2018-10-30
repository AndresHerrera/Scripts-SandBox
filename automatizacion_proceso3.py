import os
from os.path import basename
import shutil
import processing

mergepath =  r'C:\Users\C40-05\Dropbox\DatosFelipeBonilla\Merged'
exportpathmagnasirgas =  r'C:\Users\C40-05\Dropbox\DatosFelipeBonilla\MagnaSirgas' 

filestomerge =[]
for dir_entry in os.listdir(exportpathmagnasirgas):
    dir_entry_path = os.path.join(exportpathmagnasirgas, dir_entry)
    if os.path.isfile(dir_entry_path):
        if dir_entry_path[-11:]=='polygon.shp':
            print(dir_entry_path)
            filename = basename(dir_entry_path).replace(" ", "")
            filestomerge.append(dir_entry_path)

mergedFileName =  os.path.join(mergepath, 'Merge'+'_'+'psa_prjects.shp')
mergeLayers=processing.runalg('qgis:mergevectorlayers', filestomerge ,mergedFileName)
print('[OK] MERGED FILES')

