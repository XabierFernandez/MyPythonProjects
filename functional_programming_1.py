import collections

Scientist = collections.namedtuple('Scientist', [
	'name',
	'field',
	'born',
	'nobel',
])

Scientist(name='Ada Lovelace', field='math', born= 1815, nobel=False)

ada =Scientist(name='Ada Lovelace', field='math', born= 1815, nobel=False)
print(ada.name)
#ada.name = 'Xabier Lovelace' #Tuple is inmutable can't chage de value of key name
#but I can do a new copy with the same variablename
ada =Scientist(name='Xabier Lovelace', field='math', born= 1815, nobel=False)
print(ada.name)
