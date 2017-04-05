# coding: utf-8
from gluon.contrib.webclient import WebClient

client = WebClient('http://172.21.101.31/M2L/', postbacks=True)

client.get('default/index')

data = dict(email='',
    password='passe',
    _formname='login')
client.post('default/user/login', data=data)

# Vérifie que la connexion est un succès

try :
    assert 'Too short'or 'Invalid email' in client.text
    print "Echec de connexion avec un champ vide: OK"
except Exception as e:
    print "Echec de la connexion avec un champ vide"

# DEBUG -------
#print '\ncontenu:\n', client.text
#print '\nsessions:\n', client.sessions
#print '\nheaders:\n', client.headers
#print '\ncookies:\n', client.cookies
#print '\nforms:\n', client.forms
#print
#for method, url, status, t in client.history:
#    print method, url, status, t