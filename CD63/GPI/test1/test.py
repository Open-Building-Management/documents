import json

encoding = 'utf-8'

site = {}
nom = "63000_CLE41"

# le site
with open('{}.json'.format(nom), encoding=encoding) as json_data:
    site = json.load(json_data)[nom]

# les bâtiments
for i in [1]:
    nomBat = '{}_{}'.format(nom,i)
    with open('{}.json'.format(nomBat), encoding=encoding) as json_data:
        site[nomBat] = json.load(json_data)[nomBat]

site_full = "SITE_{}.json".format(nom)
with open(site_full, "w", encoding=encoding) as f:
    json.dump(site, f, indent=4, ensure_ascii=False)

nb = 0
batk = []
for k in site:
    if "site" not in k.lower() :
        nb+=1
        batk.append(k)
        
print("nous avons {} bâtiment(s) dans ce site".format(nb))

for i,k in enumerate(batk):

    print("bâtiment {}".format(i))
    print("nom : {}".format(k))
    d = site[k]
    bat_occupation=0
    for label in ("Bat_agents", "Bat_usagers", "Bat_tiers"):
        try:
            bat_occupation+=float(d[label])
        except Exception as e:
            pass

    print("nombre d'occupants : {}".format(bat_occupation))

    surcha = float(d["Bat_surf_chauf"].replace(",","."))
    
    print("surface chauffée : {} m2".format(surcha))
    
