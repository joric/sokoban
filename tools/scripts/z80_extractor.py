from PIL import Image
import os
import struct
import tempfile

indir = os.path.join(tempfile.gettempdir(),'sokoban')
outdir = '../../data/'

z80_palette = [
    [0x00, 0x00, 0x00],  # Black
    [0x00, 0x00, 0xD7],  # Blue
    [0xD7, 0x00, 0x00],  # Red
    [0xD7, 0x00, 0xD7],  # Magenta
    [0x00, 0xD7, 0x00],  # Green
    [0x00, 0xD7, 0xD7],  # Cyan
    [0xD7, 0xD7, 0x00],  # Yellow
    [0xD7, 0xD7, 0xD7],  # White
    [0x00, 0x00, 0x00],  # Bright Black
    [0x00, 0x00, 0xFF],  # Bright Blue
    [0xFF, 0x00, 0x00],  # Bright Red
    [0xFF, 0x00, 0xFF],  # Bright Magenta
    [0x00, 0xFF, 0x00],  # Bright Green
    [0x00, 0xFF, 0xFF],  # Bright Cyan
    [0xFF, 0xFF, 0x00],  # Bright Yellow
    [0xFF, 0xFF, 0xFF]   # Bright White
]

def getZ80Colors(c):
    bright = (c >> 6) & 1;
    fg = z80_palette[ ((c >> 0) & 7 ) + bright*8 ]
    bg = z80_palette[ ((c >> 3) & 7 ) + bright*8 ]
    return fg, bg

def bits_to_pixels_ext(byte_data, pal, width=16, height=16):
    pixel_data = []
    byte_index = 0
    for y in range(height):
        row = []
        pofs = y // 8 * width // 8
        for x in range(0, width, 8):
            byte = byte_data[byte_index]
            byte_index += 1
            for bit in range(8):
                if x + bit < width:  # Ensure not to go out of bounds
                    bit_value = (byte >> (7 - bit)) & 1
                    c = pal[pofs]
                    fg,bg = getZ80Colors(c)
                    alpha = 255 if bit_value==1 else 0
                    pixel_value = (*fg,alpha) if bit_value == 1 else (*bg,alpha)
                    row.append(pixel_value)
            pofs += 1
        pixel_data.extend(row)
    return pixel_data

def save_png_bits_ext(fname, w, h, pal, data, trans=0):
    print("%s: %dx%d" % (fname,w,h))
    im = Image.new("RGBA", (w, h))
    data = bits_to_pixels_ext(data, pal, w,h)
    im.putdata(data)
    im.save(fname)

def extract_sprites(outdir, datafile, ofs=0, limit=0, trans=0):
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    data = open(datafile,'rb').read()

    pal = [128]*768
    pal[:3] = [0,0,0]

    i = 0
    while ofs<len(data):
        h,w = struct.unpack('<BB', data[ofs:ofs+2])

        print('ofs,w,h:', ofs, w, h)
        if not (0<h<=32 and 0<w<=32): 
            print(f'wrong width at 0x{ofs:x}, exiting')
            break

        ofs += 2
        s = h*8 * w
        zpal = data[ofs+s:ofs+s+w*h]
        #print('palette', zpal)
        save_png_bits_ext('%s/%03d.png' % (outdir, i), w*8, h*8, zpal, data[ofs:ofs+s], trans=trans)
        ofs += s + w*h
        i += 1
        if i==limit: break

def bits_to_pixels(byte_data, width=16, height=16):
    pixel_data = []
    byte_index = 0
    for y in range(height):
        row = []
        for x in range(0, width, 8):
            byte = byte_data[byte_index]
            byte_index += 1
            for bit in range(8):
                if x + bit < width:  # Ensure not to go out of bounds
                    bit_value = (byte >> (7 - bit)) & 1
                    pixel_value = 1 if bit_value == 1 else 0
                    row.append(pixel_value)
        pixel_data.extend(row)
    return pixel_data

def save_png_bits(fname, w, h, pal, data, clip, color, trans=0, shade=0):
    print("%s: %dx%d" % (fname,w,h))
    im = Image.new("P", (w, h))

    if color:
        fg,bg = getZ80Colors(color)
        pal[0:3] = bg
        pal[3:6] = fg

    if shade:
        fg,bg = getZ80Colors(shade)
        pal[6:9] = fg

    im.putpalette(pal)

    # clip means get width from the first byte (font format)
    width = data[0] if clip else 0
    if width:
        data = [0]+list(data[1:])

    data = bits_to_pixels(data,w,h)

    if shade:
        data = [(2 if x>0 else 0) if i<len(data)//2 else x   for i,x in enumerate(data)]


    im.putdata(data)

    if width:
        im = im.crop((0, 0, width, h))

    im.save(fname, transparency=trans)

def extract_font(outdir, datafile, ofs, size=(2,2), limit=128, clip=False, color=0, trans=0, shade=0):
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    data = open(datafile,'rb').read()

    pal = [0]*768

    i = 0
    while ofs<len(data):
        h,w = size
        if w==1: clip=False
        print('ofs,w,h:', ofs, w, h)
        s = h*8 * w
        save_png_bits('%s/%03d.png' % (outdir, i), w*8, h*8, pal, data[ofs:ofs+s], clip, color, trans, shade)
        ofs += s
        i += 1
        if i==limit: break

gamedir = os.path.join(indir,'dw')
datafile = os.path.join(gamedir,'dizzy_wh.trd')

extract_sprites(outdir+'dw/sprites', datafile, 19678, limit=23, trans=0)
extract_font(outdir+'dw/font', datafile, 15318, size=(2,2), clip=True, limit=96, trans=0, color=7, shade=2)
extract_font(outdir+'dw/font2', datafile, 15318, size=(2,2), clip=True, limit=96, trans=0, color=7, shade=3)
extract_font(outdir+'dw/anim', datafile, 15318 + 96*32, size=(2,2), limit=32, color=6)
extract_font(outdir+'dw/sysfont', os.path.join(gamedir,'48.ROM'), 15616, size=(1,1), limit=96, trans=0, color=7)
