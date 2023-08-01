@echo off
set "ruta_carpeta=C:\proyectos\tests\transformImage"
set "ruta_carpetain=C:\proyectos\tests\transformImage\images_transformed"

for %%F in ("%ruta_carpeta%\*.jpg") do (
    exiftool -XResolution=300 -YResolution=300 -ResolutionUnit=inches -o "C:\proyectos\tests\transformImage\images_converted1\%%~nF_DPIMod.jpg" "%%F"
)