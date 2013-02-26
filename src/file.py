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
def renameWheelImageName(path , postfix):
    imagelist = os.listdir(path)
    for image in imagelist:
        imagename = image[0:image.find('.')] + postfix + image[image.find('.'):]
        print image + " " + imagename
        image = os.path.join(path,image)
        imagename = os.path.join(path,imagename)
        os.rename(image, imagename)
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    #readWheelImageName(folder)
    renameWheelImageName("D:\\400\\", "_big")