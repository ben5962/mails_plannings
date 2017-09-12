#import de modules au meme niveau mais en dehors du rep courant
from module_imports_de_cochon import importer_dossier_dans_path
repertoire_relatif_projet = '../..'
importer_dossier_dans_path('parse_email',repertoire_relatif_projet)
importer_dossier_dans_path('fileutils',repertoire_relatif_projet)

# utilisation de l import de cochon:
from module_objet_mail import Objet_mail
from module_utilitaire_fichier import copy_to

# imports normaux
from dateutil.parser import *
from pathlib import Path
import glob




            
p = Path('../copie_de_pertinent/').resolve()
for fichier_mail in p.glob('../copie_de_pertinent/*.eml'):
        
        m = Objet_mail(str(fichier_mail.resolve()))
        try:
                copy_to(fichier_mail, m.getNormalizedName(),'../pertinent normalisé')
        except FileNotFoundError:
                copy_to(fichier_mail, m.getNormalizedName(shorten=True),'../pertinent normalisé')
        
        
        
                
                


        
                   
        

