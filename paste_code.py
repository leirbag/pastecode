import httplib, urllib, sys, webbrowser, os
from optparse import OptionParser
#import pygtk
#pygtk.require('2.0')
#import gtk

# Verification des arguments
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file to be paste on rafb.net", metavar="FILE")
(options, args) = parser.parse_args()

if options.filename == None:
	print "Aucun fichier en entree"
	exit(0)


# Lecture du fichier a paster
#clipboard = gtk.clipboard_get()
#text = clipboard.wait_for_text()
#print text
ofi = open(options.filename, 'r')
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
if response.status != 302:
	print "Format de la reponse non gere !"
	exit(1)
print response.msg.values()[4]

# Ouvre le lien dans un navigateur
webbrowser.open(response.msg.values()[4])

# Ferme la connexion
conn.close()

