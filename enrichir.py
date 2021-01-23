import re,sys,os,string
pathfichier=os.getcwd()
text=['posologie','intraveineuse','unité','grade','poste','remplissage par','uree','creat','pneumologie unité','dyspnée stade','hémoglobine glyquée','hémoglobine','avp en','umrecherche cnrs','puis','aides nombre','pneumologie','unite']

fich=open('corpus-medical.txt','r',encoding='utf-8')
fich2=open('subst.dic','r',encoding='utf-16')
if os.path.isfile(pathfichier+"\subst_enri.dic"):
	os.remove(pathfichier+"\subst_enri.dic")
fichier=open("subst_enri.dic",'a',encoding='utf-16')
if os.path.isfile(pathfichier+"\infos2.txt"):
	os.remove(pathfichier+"\infos2.txt")
info=open("infos2.txt",'a',encoding='utf-8')

var=fich.readlines()
var2=fich2.read()
fich2.close()
fich.close()

liste2=[]
liste=[]
lignes=[]

j=0
k=0
li=var2.replace(',.N+subst','')
li=li.split('\n')
for i in li:
	print(i)
	liste.append(i)

for i in var:
	j=j+1
	i=i.replace(u'\xa0', u' ')
	i=i.replace(' ',' ')
	x=re.search("^-?\s?(\w{3,}\s?[A-Za-zè-é]+?)\s:?\s?(\d+|,)+\s?(\d+)?(unité|sachets/jour|/j|matin|µg|mg|ml|g|cp|mmol|amp|\n|UI|le matin)", i,re.I)
	if (x and x.group(1) and x.group(1).lower() not in text):
		print(k,' ',x.group(1)) 
		fichier.write(str(x.group(1))+'\n')
	if (x and x.group(1).lower() not in text):
		k=k+1
		lignes.append(j)
		l=re.sub(' \d| mg|\d|mg|ø','',x.group(1).lower())
		if l not in liste2 and l not in liste:
			liste2.append(l)

j=0
for i in var:
    j=j+1
    i= i.replace(u'\xa0', u' ')
    i=i.replace(' ',' ')
    x=re.search("([A-Za-zè-é\-]{3,}[\s-]?[A-Za-zè-é0-9]+?)\s?:?\s(/jour|/j|matin|µg|mg|ml|g|cp|mmol|amp)?\s?:?\s?(\d-\d-\d)", i,re.I)
    if x : 
        k=k+1
        print(k,' ',x.group(1))
        fichier.write(str(x.group(1))+'\n')
        l=re.sub(' \d| mg|\d|mg|ø','',x.group(1).lower())
        if l not in liste2 and l not in liste :
            liste2.append(l)
j=0
for i in var:
    j=j+1
    i= i.replace(u'\xa0', u' ')
    i=i.replace(' ',' ')
    x=re.search("([A-Za-zè-é\-]{3,}[\s-]?[A-Za-zè-é0-9]+?)\s?:?\s(/jour|/j|matin|µg|mg|ml|g|cp|mmol|amp)?\s?:?\s?(\d\.\d\.\d)", i,re.I)
    if x : 
        k=k+1
        print(k,' ',x.group(1))
        fichier.write(str(x.group(1))+'\n')
        l=re.sub(' \d| mg|\d|mg','',x.group(1).lower())
        if l not in liste2 and l not in liste:
            liste2.append(l)
print(k)
fichier.close()

print(len(liste2))

if os.path.isfile(pathfichier+"\subst.dic"):
	os.remove(pathfichier+"\subst.dic")
fichier=open("subst.dic",'a',encoding='utf-16')
nbentite=0
nbtotal=0
for j in list(string.ascii_lowercase):
	nbentite=0
	print(len(liste2))
	for k in liste2:
		v=0
		print(k[0],j)
		if k[0]==j:
			nbentite=nbentite+1
	nbtotal=nbtotal+nbentite
	info.write(str(nbentite)+"\n")
info.write("Nombre total d'entite: "+str(nbtotal))
info.close()

for i in liste:
	liste2.append(i)

liste2.sort()
for i in liste2:
    fichier.write(i+",.N+subst\n")
fichier.close()