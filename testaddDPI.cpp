#include <iostream>
#include <exiv2/exiv2.hpp>
#include <bits/stdc++.h>

int main()
{
    std::string imagePath = "./transformedRezised.jpg";
    std::string imagePath1 = "./iamimg_tested.jpg";

    try
    {
        // Crear un nuevo conjunto de metadatos

        // exifData["Exif.Image.YResolution"] = Exiv2::Rational(300, 1);
        // exifData["Exif.Image.XResolution"] = Exiv2::Rational(300, 1);

        // Abrir la imagen usando Exiv2
        Exiv2::Image::AutoPtr image1 = Exiv2::ImageFactory::open(imagePath1);
        image1->readMetadata();
        Exiv2::ExifData &exifData1 = image1->exifData();

        Exiv2::Image::AutoPtr image = Exiv2::ImageFactory::open(imagePath);
        Exiv2::ExifData &exifData = image->exifData();
        
        if (!image.get())
        {
            std::cerr << "Error al abrir la imagen: " << imagePath << std::endl;
            return 1;
        }
        if (!image1.get())
        {
            std::cerr << "Error al abrir la imagen: " << imagePath << std::endl;
            return 1;
        }
        // exifData1["Exif.Image.YResolution"] = Exiv2::Rational(300,1);
        // exifData1["Exif.Image.XResolution"] = Exiv2::Rational(300, 1);
        // exifData1["Exif.Image.SamplesPerPixel"] = uint32_t(300);
        // exifData1["Exif.Image.ImageWidth"] = int32_t(960);
        // exifData1["Exif.Image.XResolution"] = int32_t(300);
        // exifData1["Exif.Image.Make"] = "";
        // exifData1["Exif.Image.Model"] = "";

        std::cout<< "PTMRMALKJDS" << std::endl;
        for (Exiv2::ExifData::const_iterator it = exifData1.begin(); it != exifData1.end(); ++it)
        {
            std::cout << it->key() << ": " << it->value().toString() << std::endl;
        }
        std::cout<< "PTMRMALKJDS" << std::endl;
        
        // exifData["Exif.Image.XResolution"] = int32_t(-2);
        //exifData["Exif.Image.SamplesPerPixel"] = uint16_t(300);
        // exifData["Exif.Image.ResolutionUnit"] = Exiv2::Rational(2.11,1);
        
        // Establecer los nuevos metadatos en la imagen
        image->setExifData(exifData1);
        image->writeMetadata();
        std::cout << "Metadatos agregados exitosamente a la imagen." << std::endl;
    }
    catch (const std::exception &ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    return 0;
}