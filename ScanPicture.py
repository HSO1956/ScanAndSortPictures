#ScanPicture.py
import os
import logging
import shutil
from PIL import Image, ExifTags
from GPSPhoto import gpsphoto
from geopy.geocoders import Nominatim
from geopy.location import Location

if __name__ == "__main__":
    logging.basicConfig(filename='Logfile.log', level=logging.DEBUG)
    SaveToSql=False
    try:
        undefined=0
        Total=0    
        geolocator = Nominatim(user_agent="geoapiExercises")
        rootdir = "W:\photos"
        rootdir = "J:\photos"   # sur la clef USB
        
        for subdir, dirs, files in os.walk(rootdir):
            i=0
            for file in files:
                if file.find("jpg") >2 or file.find("JPG") >2:
                    Total=Total+1
                    print("Total=",Total," With GPS= ",Total-undefined)
                    myImage = subdir + os.sep + file
                    myYear=os.path.basename(myImage) [:4]
                   
                    try:
                        data = gpsphoto.getGPSData(myImage)
                        Latitude=str(data['Latitude'])
                        Longitude=str(data['Longitude'])
                        location = geolocator.reverse(Latitude+","+Longitude)
                        TargetDir ="J:/Sorted/WithGPS/"+myYear
    
                    except:
                        #----------------------------------------------
                        # Il n'y a pas de données GPS
                        #----------------------------------------------
                        TargetDir ="J:/Sorted/NoGPS/"+myYear
                        undefined=undefined+1
                    finally:
                        # Le répertoire n'existe pas
                        if not os.path.exists(TargetDir):
                            os.makedirs(TargetDir)
                        # Move file
                        try:
                            shutil.move(myImage,TargetDir)
                        except:
                            pass    
                else:
                    #---------------------------------
                    #   Ce n'est pas un fichier JPG
                    #---------------------------------
                    pass

                
        print("Total    = ",Total)
        print("Undefined= ",undefined)
        print("Defined  = ",Total-undefined)
        print("Done.......")
        exit()
    except Exception as e:

        logging.DEBUG(str(e))
        pass

    finally:
        print("Terminé")

            