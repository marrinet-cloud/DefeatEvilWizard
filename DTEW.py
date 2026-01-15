import random

victory_messages = [
    "🏆 Victory! {name} has defeated the Evil Wizard!",
    "✨ The Dark Wizard falls! {name} stands victorious!",
    "🔥 Against all odds, {name} has triumphed over evil!",
    "⚔️ {name} delivers the final blow and saves the realm!"
]

defeat_messages = [
    "💀 {name} has fallen. The Evil Wizard reigns supreme!",
    "☠️ Darkness prevails as {name} is defeated...",
    "🕯️ The hero {name} has failed. Evil spreads across the land.",
    "🌑 The wizard laughs as {name} collapses in defeat."
]

wizard_taunts = [
    "The Dark Wizard sneers: 'Is that all you've got?'",
    "The Dark Wizard laughs: 'You fight like a novice!'",
    "The Dark Wizard mocks you with a slow, threatening clap.",
    "The Dark Wizard smirks: 'Your efforts are meaningless.'",
    "The Dark Wizard growls: 'I will enjoy your defeat.'"
]

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.block_next = False

    def attack(self, opponent):
        if random.random() < 0.1:
            print(f"{self.name} attacks {opponent.name} but misses!")
            return

        damage = random.randint(self.attack_power - 5, self.attack_power + 5)

        if opponent.block_next:
            if random.random() < 0.5:
                print(f"{opponent.name} blocks the attack completely!")
                opponent.block_next = False
                return
            else:
                print(f"{opponent.name} partially blocks the attack!")

        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(15, 25)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} HP! "
              f"Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_strike(self, opponent):
        if random.random() < 0.1:
            print(f"{self.name}'s Power Strike missed!")
            return
        damage = self.attack_power + 15
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} uses Power Strike for {damage} damage!")

    def battle_cry(self):
        self.attack_power += 5
        print(f"{self.name} uses Battle Cry! Attack power increased.")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def fireball(self, opponent):
        if random.random() < 0.1:
            print(f"{self.name}'s Fireball missed!")
            return
        damage = random.randint(40, 55)
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} casts Fireball for {damage} damage!")

    def arcane_heal(self):
        heal_amount = random.randint(20, 35)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} uses Arcane Heal for {heal_amount} HP!")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)

    def quick_shot(self, opponent):
        print(f"{self.name} uses Quick Shot!")
        self.attack(opponent)
        self.attack(opponent)

    def evade(self):
        self.block_next = True
        print(f"{self.name} prepares to evade the next attack!")

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=22)

    def holy_strike(self, opponent):
        if random.random() < 0.1:
            print(f"{self.name}'s Holy Strike missed!")
            return
        damage = random.randint(35, 50)
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} uses Holy Strike for {damage} damage!")

    def divine_shield(self):
        self.block_next = True
        print(f"{self.name} activates Divine Shield!")

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
        self.minion = None

    def regenerate(self):
        heal_amount = random.randint(5, 10)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} regenerates {heal_amount} HP!")

    def dark_blast(self, player):
        if random.random() < 0.1:
            print(f"{self.name} casts Dark Blast but misses!")
            return
        damage = random.randint(25, 40)
        player.health -= damage
        player.health = max(player.health, 0)
        print(f"{self.name} casts Dark Blast for {damage} damage!")

    def summon_minion(self):
        if self.minion is None or self.minion.health <= 0:
            self.minion = Minion()
            print(f"{self.name} summons a Dark Minion!")
        else:
            print(f"{self.name}'s minion is already fighting!")

class Minion(Character):
    def __init__(self):
        super().__init__("Dark Minion", health=40, attack_power=10)

    def attack(self, opponent):
        if random.random() < 0.1:
            print(f"{self.name} attacks {opponent.name} but misses!")
            return

        damage = random.randint(self.attack_power - 3, self.attack_power + 3)

        if opponent.block_next:
            if random.random() < 0.5:
                print(f"{opponent.name} blocks the minion's attack completely!")
                opponent.block_next = False
                return
            else:
                print(f"{opponent.name} partially blocks the minion's attack!")

        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    choice = input("Enter your choice: ")
    name = input("Enter your character's name: ")

    if choice == '1':
        return Warrior(name)
    elif choice == '2':
        return Mage(name)
    elif choice == '3':
        return Archer(name)
    elif choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while player.health > 0 and wizard.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)

        elif choice == '2':
            if isinstance(player, Warrior):
                print("1. Power Strike\n2. Battle Cry")
                ability = input("Choose ability: ")
                if ability == '1':
                    player.power_strike(wizard)
                else:
                    player.battle_cry()

            elif isinstance(player, Mage):
                print("1. Fireball\n2. Arcane Heal")
                ability = input("Choose ability: ")
                if ability == '1':
                    player.fireball(wizard)
                else:
                    player.arcane_heal()

            elif isinstance(player, Archer):
                print("1. Quick Shot\n2. Evade")
                ability = input("Choose ability: ")
                if ability == '1':
                    player.quick_shot(wizard)
                else:
                    player.evade()

            elif isinstance(player, Paladin):
                print("1. Holy Strike\n2. Divine Shield")
                ability = input("Choose ability: ")
                if ability == '1':
                    player.holy_strike(wizard)
                else:
                    player.divine_shield()

        elif choice == '3':
            player.heal()

        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue

        else:
            print("Invalid choice.")
            continue

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            print(random.choice(wizard_taunts))

            action = random.choice(["attack", "dark_blast", "summon"])

            if action == "attack":
                wizard.attack(player)
            elif action == "dark_blast":
                wizard.dark_blast(player)
            elif action == "summon":
                wizard.summon_minion()

            if wizard.minion and wizard.minion.health > 0:
                print("The Dark Minion attacks!")
                wizard.minion.attack(player)

    if player.health <= 0:
        message = random.choice(defeat_messages)
        print(f"\n{message.format(name=player.name)}")
    else:
        message = random.choice(victory_messages)
        print(f"\n{message.format(name=player.name)}")

def main():
    while True:
        player = create_character()
        wizard = EvilWizard("The Dark Wizard")
        battle(player, wizard)

        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()