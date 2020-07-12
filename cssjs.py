from sys import argv
def __compile__(filename,jsFile,cssFile):
	target=open(filename,'r')
	jsOut=open(jsFile,'w+')
	cssOut=open(cssFile,'w+')
	jsData=[]
	cssData=[]
	cssTrigered=False
	jsTrigered=False
	identifier=False
	for line in target.readlines():
		if line.startswith('/*JS*/'):
			jsTrigered=True
			cssTrigered=False
			identifier=True
		elif line.startswith('/*CSS*/'):
			cssTrigered=True
			jsTrigered=False
			identifier=True
		else:
			identifier=False
		if identifier:
			pass
		elif jsTrigered:
			jsData.append(line)
		elif cssTrigered:
			cssData.append(line)
	jsOut.write(''.join(jsData))
	cssOut.write(''.join(cssData))
	target.close()
	jsOut.close()
	cssOut.close()
	print("[cssjs] compiled {} and output are: {} and {}".format(filename,jsFile,cssFile))

if __name__=="__main__":
	__compile__(str(input("Target file: ")),str(input("Js file: ")),str(input("Css file: ")))
	