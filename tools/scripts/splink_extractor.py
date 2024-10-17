from PIL import Image
import os
import struct
import tempfile

indir = os.path.join(tempfile.gettempdir(),'sokoban')
outdir = '../../data/'

def save_png(fname, w, h, pal, data):
    print("%s: %dx%d" % (fname,w,h))
    im = Image.new("P", (w, h))
    im.putpalette(pal)
    im.putdata(data)
    im.save(fname, transparency=0)

def extract(outdir, gamedir, datafile, palfile, total=0, dofs=0, pofs=0):
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    data = open(os.path.join(gamedir,datafile),'rb').read()

    pdat = open(os.path.join(gamedir,palfile),'rb').read()[pofs:pofs+768]

    pal = [x*4 & 0xff for x in pdat]

    i = 0
    ofs = dofs

    while ofs<len(data):
        w,h,s = struct.unpack('<hhh', data[ofs:ofs+6])
        #print('ofs,w,h,s:', ofs, w, h, s)

        if not (0<h<=512 and 0<w<=512): 
            print(f'wrong width at 0x{ofs:x}, exiting')
            break

        ofs += 6
        save_png('%s/%03d.png' % (outdir, i), w,h,pal,data[ofs:ofs+s])
        ofs += s
        i += 1

        if i==total:
            break

    print(f'end offset: 0x{ofs:x}')


gamedir = os.path.join(indir,'fn','obj')

extract(outdir + 'fn/data', gamedir, 'data.dat', 'exp.col', 34)
extract(outdir + 'fn/data2', gamedir, 'data2.dat', 'exp.col')
extract(outdir + 'fn/data3', gamedir, 'data3.dat', 'exp.col')
extract(outdir + 'fn/data4', gamedir, 'data4.dat', 'exp.col')
extract(outdir + 'fn/font', gamedir, 'font.dat', 'exp.col')

gamedir = os.path.join(indir,'lens')

# we need unpacked lens.exe, use unpklite
extract(outdir + 'lens/data', gamedir, 'lens.exe', 'lens.exe', 34, 0x14e2, 0x854f)
extract(outdir + 'lens/font', gamedir, 'lens.exe', 'lens.exe', 0, 0x53db, 0x854f)
extract(outdir + 'lens/ghost', gamedir, 'lens.exe', 'lens.exe', 0, 0x854f+768, 0x854f)
