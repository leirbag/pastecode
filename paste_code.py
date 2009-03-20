import httplib, urllib, sys, webbrowser

# Verification des arguments
if len(sys.argv) != 2:
	print "error with argument size"
	exit(1)

# Lecture du fichier a paster
ofi = open(sys.argv[1], 'r')
buffer = ofi.read()

type = "C++"

# Parametrage selon le formulaire distant
params = urllib.urlencode({'lang': type, 'text': buffer})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

# Connexion au site
conn = httplib.HTTPConnection("rafb.net:80")
conn.request("POST", "/paste/paste.php", params, headers)

# Recupere et affiche le resultat
response = conn.getresponse()
if response.status != 302
	print "Format de la reponse non gere !"
	exit(1)
print response.msg.values()[4]

# Ouvre le lien dans un navigateur
webbrowser.open(response.msg.values()[4])

# Ferme la connexion
conn.close()

