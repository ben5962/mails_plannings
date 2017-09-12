Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Utilisateur\Documents\GitHub\mails_plannings\normaliser_noms_mail_dedupliquer_mails\module_imports_de_cochon.py 
>>> p = Path('.')
>>> p
WindowsPath('.')
>>> p.name
''
>>> p.cwd()
WindowsPath('C:/Users/Utilisateur/Documents/GitHub/mails_plannings/normaliser_noms_mail_dedupliquer_mails')
>>> p.cwd().endswith('mail')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    p.cwd().endswith('mail')
AttributeError: 'WindowsPath' object has no attribute 'endswith'
>>> p.cwd().name
'normaliser_noms_mail_dedupliquer_mails'
>>> import sys
>>> print(sys.path)
['C:\\Users\\Utilisateur\\Documents\\GitHub\\mails_plannings\\normaliser_noms_mail_dedupliquer_mails', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
>>> sys.append(p / ..)
SyntaxError: invalid syntax
>>> sys.append(p / '..')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sys.append(p / '..')
AttributeError: module 'sys' has no attribute 'append'
>>> sys.path.append(p / '..')
>>> print(sys.path)
['C:\\Users\\Utilisateur\\Documents\\GitHub\\mails_plannings\\normaliser_noms_mail_dedupliquer_mails',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages',
 WindowsPath('..')]
>>> sys.path.append(str(p / '..'))
>>> print(sys.path)
['C:\\Users\\Utilisateur\\Documents\\GitHub\\mails_plannings\\normaliser_noms_mail_dedupliquer_mails',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32',
 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages',
 WindowsPath('..'),
 '..']
>>> str(p.cwd())
'C:\\Users\\Utilisateur\\Documents\\GitHub\\mails_plannings\\normaliser_noms_mail_dedupliquer_mails'
>>> p_voulu = p.
SyntaxError: invalid syntax
>>> p_voulu = p/'..'
>>> str(p_voulu.cwd())
'C:\\Users\\Utilisateur\\Documents\\GitHub\\mails_plannings\\normaliser_noms_mail_dedupliquer_mails'
>>> sys.path.append(p_voulu.cwd())
>>> print(sys.path())
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(sys.path())
TypeError: 'list' object is not callable
>>> print(sys.path)
['C:\\Users\\Utilisateur\\Documents\\GitHub\\mails_plannings\\normaliser_noms_mail_dedupliquer_mails', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages', WindowsPath('..'), '..', WindowsPath('C:/Users/Utilisateur/Documents/GitHub/mails_plannings/normaliser_noms_mail_dedupliquer_mails')]
>>> sys.path.append(str(p_voulu.cwd()))
>>> print(sys.path)
['C:\\Users\\Utilisateur\\Documents\\GitHub\\mails_plannings\\normaliser_noms_mail_dedupliquer_mails', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\Utilisateur\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages', WindowsPath('..'), '..', WindowsPath('C:/Users/Utilisateur/Documents/GitHub/mails_plannings/normaliser_noms_mail_dedupliquer_mails'), 'C:\\Users\\Utilisateur\\Documents\\GitHub\\mails_plannings\\normaliser_noms_mail_dedupliquer_mails']
>>> p_voulu.cwd()
WindowsPath('C:/Users/Utilisateur/Documents/GitHub/mails_plannings/normaliser_noms_mail_dedupliquer_mails')
>>> p_voulu = p / '..'
>>> p_voulu = p / '..'
>>> p_voulu.cwd()
WindowsPath('C:/Users/Utilisateur/Documents/GitHub/mails_plannings/normaliser_noms_mail_dedupliquer_mails')
>>> p_voulu = p \ '..'
SyntaxError: unexpected character after line continuation character
>>> p_voulu = p.joinpath('..')
>>> print(p_voulu)
..
>>> 
