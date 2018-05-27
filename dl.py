import urllib2
import os

from colorama import init, Style, Fore

# All data
all = {
	'coffre': [
		{'iter': 4}
	],
	'objet': [
		{'name': 'bec', 'iter': 2, 'underscore': True},
		{'name': 'blood'},
		{'name': 'bolef5'},
		{'name': 'bouteille_vide'},
		{'name': 'cadavre_chenille'},
		{'name': 'carapace', 'iter': 2},
		{'name': 'chapeau', 'iter': 5},
		{'name': 'chardon'},
		{'name': 'coquille', 'iter': 6},
		{'name': 'cristal', 'iter': 9},
		{'name': 'dent', 'iter': 5},
		{'name': 'feuille', 'iter': 3},
		{'name': 'fiolevide'},
		{'name': 'fragment'},
        {'name': 'griffe'},
        {'name': 'grimoire'},
		{'name': 'jevx7i5doqbh'},
		{'name': 'lame_depeceur'},
		{'name': 'manche_mineur'},
		{'name': 'minerai','iter':11},
		{'name': 'p9jp2wnq9bsa'},
		{'name': 'patte'},
		{'name': 'peau', 'iter': 6},
		{'name': 'piece', 'iter': 1},
		{'name': 'pierre', 'iter': 12},
		{'name': 'pierre_golem'},
		{'name': 'plume_coq'},
		{'name': 'zj20ek71lkzk'},
	],
	'objetquete': [
		{'name': 'bousolle'},
		{'name': 'clef', 'iter': 10, 'underscore': True},
		{'name': 'gateau_noel', 'iter': 10, 'underscore': True, 'pad': True},
		{'name': 'parchemin','iter': 5},
	],
	'pnj': [
		{'name': 'pnj', 'iter': 200},
		{'name': 'swirl', 'iter': 20},
		{'name': 'gardeTP', 'iter': 20},
		{'name': 'paladin_varox'},
		{'name': 'jeune_guerrier'},
		{'name': 'bougie'},
		{'name': 'lynus'},
		{'name': 'moine_copiste'},
		{'name': 'tynus'},
		{'name': 'new_garde', 'iter': ['r', 'e', 'c'], 'underscore': True},
	],
	'pnjDetail': [
		{'name': 'bougie'},
		{'name': 'competence'},
		{'name': 'Eidola'},
		{'name': 'fille_couteau'},
		{'name': 'garde3_detail'},
		{'name': 'garde4_detail'},
		{'name': 'garde5_detail'},
		{'name': 'jeune_guerrier'},
		{'name': 'lynus'},
		{'name': 'moine_copiste'},
		{'name': 'paladin_varox'},
		{'name': 'pr_lactos'},
		{'name': 'soldat_arene'},
		{'name': 'Tynus'},
	],
	'potion': [
		{'name': 'bonbec', 'iter': 13},
		{'name': 'buffpot', 'iter': 8},
		{'name': 'carotte'},
		{'name': 'feuille', 'iter': 11},
		{'name': 'flacon'},
		{'name': 'gateau'},
		{'name': 'millefeuilleschamsrz6'},
		{'name': 'poisson', 'iter': 5},
		{'name': 'pomme', 'iter': 2},
		{'name': 'potion', 'iter': 50},
		{'name': 'potion_constit_majeure'},
		{'name': 'potion_dext_majeure'},
		{'name': 'potion_force_majeure'},
		{'name': 'potiron'},
		{'name': 'viande', 'iter': 7},
	],
	'competence': [
		{'name': 'skill', 'iter': 100, 'ext': ['png', 'gif']}
	],
	'classe': [
		{'name': 'manant', 'iter': ['m','f'], 'underscore': True},
		{'name': 'magicien', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'moine', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'guerrier', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'archer', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'franctireur', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'druide', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'barbare', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'paladin', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'pretre', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'geomancien', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'aquamancien', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'heros', 'iter': ['m', 'mr', 'me', 'mc', 'f', 'fr', 'fe', 'fc'], 'underscore': True},
		{'name': 'heros_m', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_mr', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_me', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_mc', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_f', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_fr', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_fe', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'heros_fc', 'iter': ['v', 'f', 'm', 'c', 'e'], 'underscore': True},
		{'name': 'bagnard','iter':2},
		{'name': 'balrog'},
		{'name': 'felin'},
		{'name': 'grenouille'},
		{'name': 'ogre'},
		{'name': 'metal'},
	],
	'arme': [
		{'name': 'amulette', 'iter':13, 'pad': True},
        #la faute est volontaire
        {'name': 'amuremort'},
        {'name': 'anneaufer'},
        {'name': 'anneauHallo'},
        {'name': 'arbalete','iter':7},
        {'name': 'arc','iter':16},
        {'name': 'armemort'},
        {'name': 'armure', 'iter':16},
        {'name': 'badgeduconscritrvk5'},
        {'name': 'bague', 'iter':9, 'pad': True},
        {'name': 'bague', 'iter':17},
        {'name': 'bague_bete_puissante'},
        {'name': 'bague_bete_sup'},
        {'name': 'bague_immortel'},
        {'name': 'baguerouge01lt5'},
        {'name': 'baguette', 'iter':4},
        {'name': 'bague', 'iter':7, 'pad': True},
        {'name': 'bague', 'iter':4},
        {'name': 'bas', 'iter':45},
        {'name': 'bas2_l'},
        {'name': 'bas8_l'},
        {'name': 'bas_tempete_scinti'},
        {'name': 'bas_tempete_sup'},
        {'name': 'baton', 'iter': 30},
        {'name': 'baton_bete_puissant'},
        {'name': 'baton_volcanos_scinti'},
        {'name': 'beret'},
        {'name': 'bonnet_noel','iter':['','2','_new']},
        {'name': 'botte_justice_leg'},
        {'name': 'botte_justice_sup'},
        {'name': 'botte_noel','iter':['','2','_new']},
        {'name': 'bottes', 'iter': 26},
        {'name': 'bottes', 'iter': 8,'pad':True},
        {'name': 'bottes07_l'},
        {'name': 'bottes08_l'},
        {'name': 'botte_sauvage_puiss'},
        {'name': 'boucle','iter':10},
        {'name': 'bouclier','iter':18},
        {'name': 'bottes11_l'},
        {'name': 'bottes14_l'},
        {'name': 'cacheoreilles'},
        {'name': 'canne_a_peche'},
        {'name': 'cape', 'iter': 8},
        {'name': 'capenoel'},
        {'name': 'cape_noel','iter':['2','_new']},
        {'name': 'capuche_chasseur_puissant'},
        {'name': 'capucheti9'},
        {'name': 'cas_consc'},
        {'name': 'cape', 'iter': 28},
        {'name': 'casque_de_justice_puissant'},
        {'name': 'champi'},
        {'name': 'chapeau', 'iter': 28},
        {'name': 'chapka', 'iter': 10},
        {'name': 'chaussons_volcano_scintillant'},
        {'name': 'chaussons_volcano_sup'},
        {'name': 'chaussure_chasseur_sup'},
        {'name': 'chaussures', 'iter': 12},
        {'name': 'bottes7_l'},
        {'name': 'chemise', 'iter': 2},
        {'name': 'citrouille'},
        {'name': 'cle', 'iter': 1},
        {'name': 'collier01', 'iter': ['a','g','m','p'], 'pad':True},
        {'name': 'collier', 'iter': 4, 'pad': True},
        {'name': 'collier_infini_scintillant'},
        {'name': 'collier_infini_sup'},
        {'name': 'colliermort'},
        {'name': 'collier_zephyr'},
        {'name': 'cor'},
        {'name': 'couronne', 'iter': 4},
        # la faute est volontaire
        {'name': 'coutea', 'iter': 10},
        {'name': 'couteau', 'iter': 1,'pad':True},
        {'name': 'crane', 'iter': 2},
        {'name': 'croix'},
        {'name': 'crosse', 'iter': 5},
        {'name': 'dague', 'iter': 2},
        {'name': 'defaut_torse'},
        {'name': 'echarpeduperenoeleg5'},
        {'name': 'epee', 'iter': 22},
        {'name': 'epee_justice_sup'},
        {'name': 'epee_justice_scin'},
        {'name': 'equip', 'iter': 61},
        {'name': 'escarpins01id3'},
        {'name': 'fronde', 'iter': 1, 'pad': True},
        {'name': 'gant', 'iter': 9, 'pad': True},
        {'name': 'gant', 'iter': 10},
        {'name': 'cape_noel', 'iter': ['', '2']},
        {'name': 'gants01gf6'},
        {'name': 'griffe', 'iter': 4},
        {'name': 'griffe'},
        {'name': 'grimoire', 'iter': 6},
        {'name': 'grimoiremort'},
        {'name': 'hache', 'iter': 11},
        {'name': 'hache_sauvage_pui'},
        {'name': 'hache_sauvage_sup'},
        {'name': 'hachette'},
        {'name': 'haut', 'iter': 30},
        {'name': 'haut8_l'},
        {'name': 'haut14_l'},
        #les fautes sont volontaires
        {'name': 'madail', 'iter': 10},
        {'name': 'marteau', 'iter': 10},
        {'name': 'masque', 'iter': 2, 'pad': True},
        {'name': 'masque_nature_scintillant'},
        {'name': 'masque_nature_sup'},
        {'name': 'masse', 'iter': 8},
        # la faute est volontaire
        {'name': 'mitain', 'iter': 10},
        {'name': 'ombrelle01tq1'},
        {'name': 'paire_pantoufle_puissante'},
        {'name': 'paire_pantoufle_sup'},
        {'name': 'pdtfnv1c2vk5'},
        {'name': 'pelle','iter':1},
        {'name': 'pelle', 'iter': 2,'pad':True},
        {'name': 'pendentif'},
        {'name': 'pendentif', 'iter':11,'pad':True},
        {'name': 'pied', 'iter': 2, 'pad': True},
        {'name': 'pierre', 'iter': 8},
        {'name': 'pioche'},
        {'name': 'pioche', 'iter': 2, 'pad': True},
        {'name': 'robebal2jd4'},
        {'name': 'sabre', 'iter': 4, 'pad': True},
        {'name': 'sandales', 'iter': 5},
        {'name': 'serpe'},
        {'name': 'teteabeillerouge'},
        {'name': 'tetechauvesouris'},
        {'name': 'tetereduite'},
        {'name': 'tetine'},
        {'name': 'tiare01qr5'},
        {'name': 'toge_pelerin_puissant'},
        {'name': 'toge_pelerin_sup'},
        {'name': 'tunique_aventurier'},

        #jpg
        #20039517vg7
        #arf_consc
        # arm_consc
        # consc_bouc
        # cons_pant
    ],
	'monstre/insecte': [
		{'name': 'lezard'},
		{'name': 'gecko', 'iter': 2},
		{'name': 'escargot', 'iter': 3},
		{'name': 'insecte', 'iter': 2, 'pad': True},
		{'name': 'fourmi', 'iter': 2},
		{'name': 'chenille', 'iter': 3},
		{'name': 'mouche', 'iter': 2},
		{'name': 'lezard', 'iter': 5},
		{'name': 'scarabe', 'iter': 9},
		{'name': 'cloporte', 'iter': 2},
		{'name': 'grenouille', 'iter': 2},
		{'name': 'araignee', 'iter': 5},
		{'name': 'abeille', 'iter': 3},
		{'name': 'abeille', 'iter': 1, 'pad': True},
		{'name': 'libellule', 'iter': 4},
	],
	'monstre/prison': [
		{'name': 'poisson'},
		{'name': 'prisonnier'},
	],
	'monstre/bizarre': [
		{'name': 'tortue'},
		{'name': 'galahaad'},
		{'name': 'epouvantail'},
		{'name': 'MudGolem'},
		{'name': 'fantome', 'iter': 1},
		{'name': 'elemental', 'iter': 13},
		{'name': 'ange', 'iter': 2},
	],
	'monstre/bestiaux': [
		{'name': 'chat3nd2'},
		{'name': 'chat1do2'},
		{'name': 'renard'},
		{'name': 'hog'},
		{'name': 'wolf'},
		{'name': 'lizardman'},
		{'name': 'serpentmer'},
		{'name': 'coq', 'iter': 2},
		{'name': 'serpent', 'iter': 4},
		{'name': 'poisson', 'iter': 3},
		{'name': 'goblin', 'iter': 1},
		{'name': 'demon', 'iter': 1},
		{'name': 'ours', 'iter': 6},
		{'name': 'chauve_souris', 'iter': 1},
	],
	'monstre/boss': [
		{'name': 'poisson'},
		{'name': 'herisson-lion'},
		{'name': 'bouquetin'},
		{'name': 'dragon'},
		{'name': 'ombre_ailee'},
		{'name': 'Gomina'},
		{'name': 'fv1006'},
		{'name': 'aigle'},
		{'name': 'yeti'},
	],
	'monstre/flore': [
		{'name': 'tournesol', 'iter': 2},
		{'name': 'champignon', 'iter': 4},
		{'name': 'champignon', 'iter': 3, 'pad': True},
		{'name': 'plantecarnivore', 'iter': 3},
		{'name': 'arbre', 'iter': 6},
	],
}

# Data to fetch
enabled = ['competence']
#enabled = all.keys()

new = 0
skip = 0
fail = 0

# Download a given file
def getFile (dir, name, ext='png'):
	global new, skip, fail
	fname = name + '.' + ext
	path = dir + '/' + fname
	
	try:
		if os.path.exists(path):
			skip += 1
			print Fore.MAGENTA + name + ' already exists, skipping'
			return
		response = urllib2.urlopen('http://data2.alidhan.net/img/' + dir + '/' + fname)
		new += 1
		if not os.path.exists(dir):
			os.makedirs(dir)
		with open(path, 'wb') as out:
			out.write(response.read())
			print Fore.GREEN + name
	except urllib2.HTTPError as e:
		fail += 1
		print Fore.RED + name
	except IOError:
		pass
		
# Build name from value in iter and formatting options
def nthItem (name, n, underscore=False, pad=False):
	if (underscore): name += '_'
	if (pad): name += '0'
	name += str(n)
	return name

# Main
init(autoreset=True)
for key in set(enabled):
	if key not in all: continue
	items = all[key]
	print '--- ' + key + ' ---'
	for item in items:
		exts = item['ext'] if 'ext' in item and isinstance(item['ext'], list) else ['png']
		for ext in exts:
			if 'iter' in item and item['iter']:
				values = []
				# Iterate over a list
				if isinstance(item['iter'], list):
					values = item['iter']
				# Iterate over a range
				elif isinstance(item['iter'], int):
					values = range(1, item['iter'] + 1)
				for n in values:
					getFile(key, nthItem(
						item['name'] if 'name' in item else '',
						n,
						item['underscore'] if 'underscore' in item else False,
						item['pad'] if 'pad' in item else False
					), ext)
			else:
				getFile(key, item['name'])
	print '--- ' + str(new) + ' files downloaded, ' + str(skip) + ' skipped, ' + str(fail) + ' failed ---'
