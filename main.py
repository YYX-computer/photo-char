from PIL import Image
inPath = input('path for process:')
WIDTH = int(input('How long you want for width:'))
HEIGHT = int(input('How long you want for height:'))
outPath = input('path for save:')
print('processing,please wait')
char = u'WM%&@-.'
demarcation = 128
def limit(x,start,end):
	if(x <= start):
		return start
	if(x >= end):
		return end
	return x
def getchar(r,g,b):
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	std = float(demarcation / len(char))
	return char[limit(int(gray / std),0,len(char) - 1)]
if(__name__ == '__main__'):
	img = Image.open(inPath).convert('RGB')
	img = img.resize((WIDTH,HEIGHT),Image.NEAREST)
	text = ''
	for i in range(HEIGHT):
		for j in range(WIDTH):
			r,g,b = img.getpixel((j,i))
			text += getchar(r,g,b)
		text += '\n'
	with open(outPath,'w') as file:
		file.write(text)
