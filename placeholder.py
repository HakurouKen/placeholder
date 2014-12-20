import re
import Image,ImageDraw
from cStringIO import StringIO

class Placeholder(object):
    hexRe = re.compile(r'^#?(?P<color>[0-9a-f]{6}|[0-9a-f]{3})$',re.IGNORECASE)
    rgbRe = re.compile(r'^(?P<color>rgb\((?P<red>\d+),(?P<green>\d+),(?P<blue>\d+)\))',re.IGNORECASE)
    def __init__(self,width=320,height=240,color='#333'):
        self.width = width
        self.height = height
        self.color = self.format_color(color)

    @classmethod
    def format_color(self,raw):
        color = raw.replace(' ','').lower()
        hex = re.match(Placeholder.hexRe,color)
        rgb = re.match(Placeholder.rgbRe,color)
        if hex:
            return '#' + hex.group('color')
        elif rgb:
            get_color = lambda color: '255' if int(color) > 255 else color
            red = get_color(rgb.group('red'))
            green = get_color(rgb.group('green'))
            blue = get_color(rgb.group('blue'))
            return 'rgb(' + red + ',' + green + ',' + blue + ')'
        return color

    def get_img(self):
        try:
            img = Image.new('RGB',(self.width,self.height),self.color)
        except:
            img = Image.new('RGB',(320,240),'grey')
	return img

    def get_binary(self):
        img = self.get_img()
        binary = StringIO()
        img.save(binary,format='PNG')
        return binary.getvalue()
