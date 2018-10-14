import pyautogui, time

varZahl="99"
varRunde=1
varRotx, varRoty =600, 353
varSchwarzx, varSchwarzy =683, 353
varSetzenx, varSetzeny=varSchwarzx, varSchwarzy
varZeitspanne=6
varBilder="D:\\zahlen\\"
varZahlFarbeRot = ["1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36"]
varZahlFarbeSchwarz = ["2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35"]
#bild = []
#bild_io = []
#	# bild als io laden (byteio)


try:
	while True:
		for schleifenzahl in range(0, 37):
			if pyautogui.locateCenterOnScreen(varBilder+str(schleifenzahl)+'.png', region=(10,400,222,280), grayscale=True):
				varZahl=str(schleifenzahl)
				time.sleep(varZeitspanne)
				break

		if varZahl < "99":
			print (varZahl)
			if varZahl in varZahlFarbeRot:
				varFarbe="rot"
				print ("Farbe Rot")
			if varZahl in varZahlFarbeSchwarz:
				varFarbe="schwarz"
				print ("Farbe Schwarz")
			
			if varZahl == "0":
				varFarbe="gruen"
				print ("Farbe gruen")
				
			if varFarbe == "rot":
				varRunde=varRunde+1
				if varRunde < 1:
					varRunde=1
				pyautogui.click(varSetzenx, varSetzeny, clicks=varRunde)
				pyautogui.moveTo(915, 560)
				time.sleep(1)
				pyautogui.click()
			if varFarbe == "schwarz":
				varRunde=varRunde-1
				if varRunde < 1:
					varRunde=1
				pyautogui.click(varSetzenx, varSetzeny, clicks=varRunde)
				pyautogui.moveTo(915, 560)
				time.sleep(1)
				pyautogui.click()
			if varFarbe == "gruen":
				varRunde=varRunde+1
				pyautogui.click(varSetzenx, varSetzeny, clicks=varRunde)
				pyautogui.moveTo(915, 560)
				time.sleep(1)
				pyautogui.click()
				
			
			varFarbe="nix"
			varZahl= "99"
	
except KeyboardInterrupt:
	print('\nEnde.')