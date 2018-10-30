@echo off
dir *.shp
for %%x in (*.shp) do ogr2ogr -s_srs EPSG:4326 -t_srs EPSG:3115 ../MagnaOeste/3115_%%x %%x
dir *.shp
for %%a in (*.shp) do ogr2ogr -s_srs EPSG:4326 -t_srs Magna_Colombia_Cali_7393.prj ../MagnaCali/6249_%%a %%a