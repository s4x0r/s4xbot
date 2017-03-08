class weapon():
    def __init__(self, name, durability, min_dmg, max_dmg, value, description):
        self.name = name
        self.durability = durability
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.value = value
        self.description = description

#weapons
weapons = {}

weapons['Fist']=weapon('Fist', -1, 1, 10, -1, 'Your bare fists')
weapons['Stone Sword']=weapon('Stone Sword', 50, 5, 15, 20, 'A sword cut from stone. It\'s quite heavy')
weapons['Iron Sword']=weapon('Iron Sword', 100, 7, 20, 50, 'A Sword forged out of iron. it\'s quite shiny')
