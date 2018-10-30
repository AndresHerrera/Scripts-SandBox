import os
from os.path import basename
import shutil
import processing
path = r'C:\Users\C40-05\Dropbox\DatosFelipeBonilla\GPX' 
exportpath =  r'C:\Users\C40-05\Dropbox\DatosFelipeBonilla\Export' 
data = {}
for dir_entry in os.listdir(path):
    dir_entry_path = os.path.join(path, dir_entry)
    for dir_entry in os.listdir(dir_entry_path):
        dir_entry_path2 = os.path.join(dir_entry_path, dir_entry)
        if os.path.isfile(dir_entry_path2):
            fileName,fileExtension = os.path.splitext(dir_entry_path2)
            if fileExtension in ['.shp','.shx','.dbf']:
                parentfolder = (os.path.split(os.path.split(os.path.realpath(dir_entry_path2))[0])[1]).replace(" ", "")
                filename = basename(dir_entry_path2).replace(" ", "")
                #print(fileName+fileExtension)
                #print(parentfolder)
                #print(filename)
                #print(filename[:-4])
                newfile = os.path.join(exportpath, parentfolder+'_'+filename)
                shutil.copyfile(fileName+fileExtension, newfile)
                print('[OK] Copiado ...')
                print(newfile)
                if filename == 'track.shp':
                    newfilepolygon = os.path.join(exportpath, parentfolder+'_'+'polygon.shp')
                    output_polygon=processing.runalg('qgis:linestopolygons', fileName+fileExtension ,newfilepolygon)
                    print('[OK] Polygon Generated ')
                