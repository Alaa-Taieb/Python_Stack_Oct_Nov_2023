# Define a base character class
class Character:
    # Constructor
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.can_play = True



    # Instance Method
    # Returns True if Health > 0
    # Return False if Health < 1
    def is_alive(self):
        return self.hp > 0
    
    # Instance Method
    # Subtracts damage from health
    # Sets health to 0 incase it was negative 
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def set_can_play(self, status):
        self.can_play = status

    # Instance Method
    # Checks if attacker is dead :
    # False => Do nothing
    # True =>
    #           Create a variable named damage = attacker's attack power
    #           Call the take_damage method of the target passing in the damage as argument
    def attack(self, target):
        if self.is_alive() and self.can_play:
            damage = self.attack_power
            target.take_damage(damage)
        self.can_play = True

    
class Mage(Character):

    # Constructor
    # Calling the parent constructor (Initializing the 'name' , 'hp' and 'attack_power' attributes)
    # Initializing the 'spell_power' attribute
    def __init__(self, name, hp, attack_power, spell_power):
        super().__init__(name, hp, attack_power)
        self.spell_power = spell_power



    def cast_spell(self, target):
        if self.is_alive() and self.can_play:
            target.set_can_play(False)
            target.take_damage(self.spell_power / 5)


class Warrior(Character):

    def __init__(self, name, hp, attack_power, defense):
        super().__init__(name, hp, attack_power)
        self.defense = defense
        self.is_defending = False

    def defend(self):
        if self.is_alive() and self.can_play:
            self.is_defending = True

    def take_damage(self, damage):
        if self.is_defending:
            damage -= self.defense
            if damage < 0:
                damage = 0
            self.is_defending = False

            
        super().take_damage(damage)