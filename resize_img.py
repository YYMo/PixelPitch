from PIL import Image
from resizeimage import resizeimage
import os

EXT_LIST = ['jpg', 'png', 'jpeg']
WIDTH_LIST = [600, 320, 480, 1080, 720]

def recur(abs_path, width):
    print "enter: " + abs_path
    dirs = os.listdir(abs_path)
    for f in dirs:
        path = abs_path + '/' + f

        if os.path.isdir(path):
            recur(path, width)
        elif os.path.isfile(path):
            print f
	    flag = True
            for w in WIDTH_LIST:
                if ('_p' + str(width)) in f:
                    flag = False
	    if flag: 
            	resize_width(width, path)

def get_file_ext(file_name):
    ext = file_name.split(".")[-1]
    name = file_name[:len(file_name) - 1 - len(ext)]
    return name, ext

def resize_width(width, file_name):
    name, ext = get_file_ext(file_name)
    if ext not in ['jpg', 'png', 'jpeg']:
        return 
    fd_img = open(file_name, 'r')
    img = Image.open(fd_img)
    w, h = img.size
    if w <= width:
        return
    img = resizeimage.resize_width(img, width)
    img.save(name + '_p' + str(width) + '.' + ext, img.format)
    fd_img.close()


if __name__ == "__main__":
    dir = os.path.dirname(os.path.realpath(__file__))
    path = dir + '/pixelpitch/images/'
    recur(path, 480)
