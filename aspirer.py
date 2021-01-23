import re, os, urllib , urllib.request, string, sys
from socket import *

pathfichier=os.getcwd()
if os.path.isfile(pathfichier+"\subst.dic"):
	os.remove(pathfichier+"\subst.dic")
fichier=open("subst.dic",'a',encoding='utf-16')

if os.path.isfile(pathfichier+"\infos.txt"):
	os.remove(pathfichier+"\infos.txt")
info=open("infos.txt",'a',encoding='utf-8')

ip = str(gethostbyname(gethostname()))
debut = sys.argv[1].upper()
fin = sys.argv[2].upper()
port = sys.argv[3]
nbtotal=0
for i in list(string.ascii_uppercase):
	if i >= debut and i<= fin:
		url = "http://"+ip+":"+str(port)+"/vidal/vidal-Sommaires-Substances-"+i+".htm";
		print(url)
		info.write("Le nombre d'entite pour "+i+": ")
		nbentite = 0
		with urllib.request.urlopen(url) as page:
			s=page.read().decode("utf-8",'ignore')
			x = re.findall("<a href=\"Substance/.+>.+</a>",s)
			l=[]
			for j in x:
				print(j)
			for j in x:
				r=re.search("<a href=\"Substance/.+>(.+)</a>",j)
				l.append(r.group(1))
			for j in l:
				print(j)
				fichier.write(j+",.N+subst\n")
				nbentite = nbentite+1
				nbtotal = nbtotal+1
		info.write(str(nbentite)+"\n")
info.write("Nombre total d'entite: "+str(nbtotal))
info.close()
fichier.close()