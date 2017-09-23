#!/usr/bin/env python3
#code is dirty for speed
import subprocess
from sys import argv
from tempfile import NamedTemporaryFile
from PIL import Image,ImageDraw,ImageFont

#### Get text to make into image
string = r'''DISPLAY=:0 wmctrl -l | awk '{ printf("%s: ",$2);   for (i = 4; i <= NF; i++) printf("%s ", $i);   printf("\n"); }' | sort '''
out = subprocess.check_output(string, subprocess.STDOUT,shell=True).decode()

spaces = subprocess.check_output('i3-msg -t get_workspaces | jq -r ".[].name"',
        subprocess.STDOUT,shell=True).decode()

workspaces = {ind:v for ind,v in enumerate(spaces.split('\n'))}
#eg {0:'1',1:'3'}

outtext = ''
maxlines = 30
linecounter = 0

for line in out.split('\n'):
    if line.rstrip() is not "" and 'texttoimage' not in line :
        spl = line.split(':')
        outtext += workspaces[int(spl[0])] + ": " + ":".join(spl[1:]) + "\n"
        linecounter += 1
        if linecounter > maxlines:
            outtext += "Too many windows!\n"

outtext = outtext[:-1]
#remove trailing newline

#with open('/tmp/wmctrllist','w') as f:
#    f.write('\n'.join(outtext))

###Make and display image
fontsize = 18
width = 800
height = round(fontsize *len(outtext.split('\n')) *1.2 + 40)

#i should probably use mktemp but whatever
out_imfile = NamedTemporaryFile(prefix='texttoimage_',suffix='.gif')
out_txtfile = NamedTemporaryFile(prefix='txtforimgify_',suffix='.gif')
#font_location = expanduser("~/.fonts/Hack/Hack-Regular.ttf")
#speed > best practices
font_location = "/home/username/.fonts/Hack/Hack-Regular.ttf"

backcolor = (44,62,80) #RGB
forecolor = (224,224,224)

im = Image.new('RGB', (width,height),color=backcolor)
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(font_location, fontsize)
draw.text((20, 20),outtext,forecolor,font=font)
im.save(out_imfile.name)

subprocess.run(('gifview',out_imfile.name))

#subprocess.run('rm /tmp/wmctrllist',shell=True)
