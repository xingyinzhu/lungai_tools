# -*- coding: utf-8 -*-
import os
import db
#-------------------------------------------------------------------------------
folder = "D:\\wheels\\"


#-------------------------------------------------------------------------------
def readWheelImageName(path):
    conn = db.connectsqlite()
    imagelist = os.listdir(path)
    for image in imagelist:
        imagename = image[0:image.find('.')]
        #print imagename;
        db.insertOneWheelIntoDB(conn, imagename)
    conn.commit()
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    readWheelImageName(folder)