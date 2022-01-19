import json
import glob
import unicodedata

encoding = 'utf-8'

# nota : le champ bat_tiers ne sert à rien : on a tout dans le champ bat_type > si ERP = le bâtiment reçoit du public
dc = {
        "sdp"    : "bat_sdp",
        "sub"    : "bat_sub",
        "sdis"   : "bat_surf_dispo",
        "sch"    : "bat_surf_chauf",
        "act"    : "bat_activite",
        "h"      : "bat_horaires",
        "pw"     : "bat_postes_travail",
        "agents" : "bat_agents", 
        "usagers": "bat_usagers", 
        "tiers"  : "bat_tiers_effectif",
        "cmax"   : "bat_capacite_max",
        "log"    : "bat_logement",
        "logocc" : "bat_logement_occupe"
    }
    
# amplitude horaire maximale de référence : 52 semaines à 60 heures par semaine, soit 3120 heures
ahm = 3120

def rmva(s):
    """
    suppression des caractères accentués et passage en minuscules
    review ?
    """
    try:
        s = str(s)
    except Exception as e:
        pass
    result = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return result.lower()

def conv(val):
    """
    transforme une chaine de caractère de type "2,5" en un flottant
    """
    try :
       val = float(val.replace(",","."))
    except Exception as e:
       pass
    return val

def getSite(nom):
    """
    nom : nom du site
    
    produit la liste clé/valeurs compilant données de site et données des divers bâtiments du site
    """
    site = {}
    # le site
    with open('{}.json'.format(nom), encoding=encoding) as json_data:
        all = json.load(json_data)
        site = all[nom]
        if "fiab" in all:
            site["fiab"] = all["fiab"]

    # les bâtiments
    for i in [1]:
        nomBat = '{}_{}'.format(nom,i)
        with open('{}.json'.format(nomBat), encoding=encoding) as json_data:
            all = json.load(json_data)
            site[nomBat] = all[nomBat]
            if "fiab" in all:
                site[nomBat]["fiab"] = all["fiab"]
    
    # sauvegarde  - pour l'instant ne sert à rien
    site_full = "SITE_{}.json".format(nom)
    with open(site_full, "w", encoding=encoding) as f:
        json.dump(site, f, indent=4, ensure_ascii=False)
                
    return site

def makeIndicateurs():
    """
    produit les indicateurs pour tous les sites et bâtiments du répertoire courant
    """
    # lecture des noms de site qui sont sur 11 caractères
    sites = []
    for file in glob.glob("*.json"):
        if "SITE" not in file:
            if file[:11] not in sites:
                sites.append(file[:11])
    #print(sites)
    for nom in sites:
        site = getSite(nom)
        # on récupère le nombre de bâtiments dans le site et les clés des bâtiments
        nb = 0
        batk = []
        for k in site:
            if nom.lower() in k.lower() :
                nb+=1
                batk.append(k)
        print("*****************************************************")
        print("nous avons {} bâtiment(s) dans le site {}".format(nb, nom))
        for i,k in enumerate(batk):
            print("bâtiment {}".format(i))
            print("nom : {}".format(k))
            d = site[k]
            print("indicateur d'intensité d'usage")
            print(indIntUsa(d))

def indIntUsa(b):
    """
    calcul de l'indicateur d'intensité d'usage
    
    bat : liste clé/valeur des données d'un bâtiment

    retourne une liste :
    s_ph   : SUB en m2 par poste de W ou SDP en m2 par occupant (collèges)
    sch_ph : surface chauffée en m2 par poste de W ou par occupant (collèges)
    %ouv   : ouverture du bâtiment
    %dis   : surface disponible sur SUB
    %occ   : taux d'occupation
    %occ_l : taux d'occupation des logements
    """
    result = {}
    
    # présence maximale sur le site
    # les valeurs saisies devaient être des entiers ?
    pm = 0
    for label in (dc["agents"], dc["usagers"], dc["tiers"]):
        try:
            pm += float(b[label])
        except Exception as e:
            pass
    
    # pour se prémunir des infections de saisie
    sdp    = conv(b[dc["sdp"]])
    sch    = conv(b[dc["sch"]])
    sub    = conv(b[dc["sub"]])
    pw     = conv(b[dc["pw"]])
    h      = conv(b[dc["h"]])
    sdis   = conv(b[dc["sdis"]])
    cmax   = conv(b[dc["cmax"]])
    log    = conv(b[dc["log"]])
    logocc = conv(b[dc["logocc"]])
    
    # m2 par habitant et m2 chauffés par habitant 
    result["s_ph"] = "NAN"
    result["sch_ph"] = "NAN"
    surf = sdp if "college" in rmva(b[dc["act"]]) else sub
    nb = pm if "college" in rmva(b[dc["act"]]) else pw
    try :
        result["s_ph"] = round (surf / nb , 2)
    except Exception as e:
        pass
    try :
        result["sch_ph"] = round (sch / nb , 2)
    except Exception as e:
        pass
    
    # pourcentage d'ouverture
    result["%ouv"] =  100 * h // ahm
    
    # pourcentage de disponibilité
    result["%sdis"] = "NAN"
    try :
        result["%sdis"] = 100 * sdis // sub
    except Exception as e:
        pass
    
    # taux d'occupation
    occ = 0
    for label in (dc["agents"], dc["tiers"]):
        try:
            occ += float(b[label])
        except Exception as e:
            pass
    result["%occ"] = "NAN"
    try:
        result["%occ"] = 100 * occ // cmax
    except Exception as e:
        pass
        
    # taux d'occupation des logements
    result["%occ_l"] = "NAN"
    try:
        result["%occ_l"] = 100 * logocc // log
    except Exception as e:
        pass
    
    return result
    
def getk(site):
    """
    site : liste clé/valeurs des données site et bâtiments d'un site
    
    affiche la liste des clés
    """
    print("      | |           ")
    print("   ___| | ___  ___  ")
    print("  / __| |/ _ \/ __| ")
    print(" | (__| |  __/\__ \ ")
    print("  \___|_|\___||___/ ")
    print("....de la table bâtiments :-)")
    print(site[batk[0]].keys())


makeIndicateurs()

