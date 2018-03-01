import glob
import os

# for filename in sorted(glob.glob('*.txt')):

for filename in sorted(glob.glob('*.txt')):
	sourceEncoding='utf-16'
	targetEncoding='utf-8'
	source = open(filename)
	target = open('/home/ileam/SNMPClaro/Guatemala/Excels/'+filename,'w')

	target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))