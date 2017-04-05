# coding: utf-8
from gluon.contrib.webclient import WebClient

client = WebClient('http://127.0.0.1:8000/M2L/',postbacks=True)

client.get('default/index')

data = dict(email='lucille.berbier@aikido-lorraine.fr',
            password='passe',
            _formname='login')
client.post('default/user/login', data=data)

# Vérifie que la connexion est un succès
fsssfs
try :
    assert 'Bienvenue Lucilksdjgfjksdgfksdgfjksdfle' in client.text
    print "Test connexion OK"
except Exception as e:
    print "Echec test de connexion C1"



# DEBUG -------
#print '\ncontenu:\n', client.text
#print '\nsessions:\n', client.sessions
#print '\nheaders:\n', client.headers
#print '\ncookies:\n', client.cookies
#print '\nforms:\n', client.forms
#print
#for method, url, status, t in client.history:
#    print method, url, status, t


