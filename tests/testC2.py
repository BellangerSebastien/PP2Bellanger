# coding: utf-8
from gluon.contrib.webclient import WebClient

client = WebClient('http://172.21.101.31/M2L/',postbacks=True)

client.get('default/index')

data1 = dict(email='lucille.berbier@aikido-lorraine.fr',
            password='passe',
            _formname='login')
client.post('default/user/login', data=data1)

client.post('default/user/logout')


# Vérifie que la connexion est un succès

try :
    assert 'Déconnecté' in client.text
    print "Test de Déconnexion : OK"
except Exception as e:
    print "Echec test de Déconnexion"


# DEBUG -------
#print '\ncontenu:\n', client.text
#print '\nsessions:\n', client.sessions
#print '\nheaders:\n', client.headers
#print '\ncookies:\n', client.cookies
#print '\nforms:\n', client.forms
#print
#for method, url, status, t in client.history:
#    print method, url, status, t