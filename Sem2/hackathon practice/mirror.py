from PIL import Image

with Image.open(r'C:\Users\HP\Desktop\Untitled10.png') as img:
    mirror_img=Image.new('RGB',img.size)

    # mechanism for left and right inversion
    
    for x in range(img.width):
        for y in range(img.height):
            pixel=img.getpixel((x,y))
            mirror_img.putpixel((img.width-1-x,y),pixel)

    mirror_img.show()

    # mechanism for up and down inversion

    for x in range(img.width):
        for y in range(img.height):
            pixel=img.getpixel((x,y))
            mirror_img.putpixel((x,img.height-1-y),pixel)
    mirror_img.show()

