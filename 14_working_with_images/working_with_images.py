############################################################################################################
############################################################################################################
# Pillow is a fork of PIL (Python Imaging Library) package
# 
############################################################################################################
############################################################################################################

from PIL import Image



def mac_example():
    mac = Image.open('example.jpg')
    print(type(mac))
    print(mac)
    print(f'{mac.filename} file is of size {mac.size}. It is of type {mac.format_description}')  
    mac.close()

def pencils_example():
    with Image.open('pencils.jpg') as Ip:
        print(Ip.size)
        # TOP Pencils
        x=0
        y=0
        w=1950/3
        h=1300/10
        Ip.crop((x,y,w,h)).show()

        # BOTTOM Pencils
        x=0
        y=1100
        w=1950/3
        h=1300
        Ip.crop((x,y,w,h)).show()

def mac_crop_example():
    with Image.open('example.jpg') as Ip:
        # print(Ip.size)
        # TOP Pencils
        halfway = 1993/2
        x=halfway-200
        w=halfway+200
        y=800
        h=1257
        Ip.crop((x,y,w,h)).show()

    

def mac_copy_paste_example():
    # with Image.open('example.jpg') as Ip:
    with Image.open('example.jpg') as Ip:
        # print(Ip.size)
        # TOP Pencils
        halfway = 1993/2
        x=halfway-200
        w=halfway+200
        y=800
        h=1257
        mac = Ip.crop((x,y,w,h))
        Ip.paste(im=mac, box=(0,0))
        Ip.show()
        Ip.resize((3000,1200))
        Ip.show()
        Ip.rotate(90).show()
 

if __name__ == "__main__":
    # mac_example()
    # pencils_example()
    # mac_crop_example()
    mac_copy_paste_example()