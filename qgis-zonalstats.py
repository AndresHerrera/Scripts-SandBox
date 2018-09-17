import qgis.analysis
import re

DEF_VIASCLASE='distancia_vias'
#Aqui definir patron de los nombres de las capas de deforestacion
DEF_DEFORESTACION='deforestacion_'

rasterlayer = []
for layer in QgsMapLayerRegistry.instance().mapLayers().values():
    if(layer.name()==DEF_VIASCLASE):
        print('Vector layer found: ' + layer.name())
        vectorlayer = layer
    if re.search(r'deforestacion_(?i)', layer.name()): 
        print('Raster layer found: ' + layer.name())
        rasterlayer.append(layer)

#iterate zonal stats 
for i in range(0, len(rasterlayer)):
    zonalstats = qgis.analysis.QgsZonalStatistics(vectorlayer,rasterlayer[i].source(),'r'+str(i)+'_')
    zonalstats.calculateStatistics(None)

print('Done ! ')





