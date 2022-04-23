lista = [1, 55, 2, 8, 99]

mi_diccionario = {'clave1':1, 'clave2': 44, 'clave3': 2, 'clave4': 8, 'clave5': 99}

mi_diccionario['clave3']#2

mi_diccionario['clave1'] = 22

mi_diccionario['nuevacalve'] = 77

del(mi_diccionario['clave5'])

mi_diccionario.clear()
mi_diccionario.copy()

otro_diccionario = mi_diccionario.copy()

mi_diccionario.get('clave4')

mi_diccionario.has_key('clave3')# si existe

mi_diccionario.items()
[('clave1', 1), ('clave2', 55)]

mi_diccionario.keys()

mi_diccionario.values()

