#ScanPicture.py
import os
import csv
from PIL import Image, ExifTags
from GPSPhoto import gpsphoto
from geopy.geocoders import Nominatim



if __name__ == "__main__":
    fichier = open("W:\photos\data.txt", "w")
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    rootdir = "W:\photos"
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            myImage = subdir + os.sep + file
            try:
                data = gpsphoto.getGPSData(myImage)
                print(data['Latitude'], data['Longitude'])
                Latitude=str(data['Latitude'])
                Longitude=str(data['Longitude'])
                #Latitude = "25.594095"
                #Longitude = "85.137566"
  
                location = geolocator.reverse(Latitude+","+Longitude)
                # Display
                Lieu=location
                # La localisation a été trouvée
                fichier.write(myImage+" : "+Lieu.address)
            except:
                fichier.write(myImage+": --------")
    fichier.close()