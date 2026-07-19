# Xavier Floyd
# 7/16/2026
# Final Project
# A simple text-based rpg game where the user build stats to fight the final boss

import random
import time
import sys

# ==========================================
# 🗺️ GAME STATE & DICTIONARIES
# ==========================================

# The central dictionary holding all characters (Actors)
actors = {
    "Player": {
        "name": "",
        "class": "",
        "health": 100,
        "max_health": 100,
        "defense": 10,
        "attack": 10,
        "magic": 10,
        "speed": 10
    },
    "Skelly": {
        "name": "Skelly the Jester 🃏",
        "health": 80,
        "max_health": 80,
        "defense": 15,
        "attack": 34,
        "magic": 28,
        "speed": 14
    },
    "Zavla": {
        "name": "Lich King Zavla 👑",
        "health": 200,
        "max_health": 200,
        "defense": 20,
        "attack": 50,
        "magic": 50,
        "speed": 18
    }
}

# The player's inventory tracking item usage
inventory = {
    "Cleric Potion": 0,    # Can hold up to 3 charges
    "Skeleton Key": False   # Can skip one fetch quest
}

# The database of 15 side quests tracking their details and rewards
quest_pool = {
    # Attack Reward Quests
    1: {"desc": "🟩 Slays a stray Slime blocking the trade road.", "type": "slay", "stat": "attack", "anti_stat": "magic", "amt": 12, "item": None, "dc": 5, "difficulty": "easy"},
    2: {"desc": "🥦 Slay a rogue Goblin Scout raiding camp supplies.", "type": "slay", "stat": "attack", "anti_stat": "magic", "amt": 15, "item": "Skeleton Key", "dc": 7, "difficulty": "easy"},
    3: {"desc": "🐗 Slay a wild Forest Boar threatening farmers.", "type": "slay", "stat": "attack", "anti_stat": "magic", "amt": 14, "item": "Cleric Potion", "dc": 8, "difficulty": "easy"},
    4: {"desc": "🦇 Slay the Blood-Sucking Bat Swarm nesting in the granary.", "type": "slay", "stat": "attack", "anti_stat": "speed", "amt": 16, "item": None, "dc": 10, "difficulty": "medium"},
    5: {"desc": "⚔️ Clear out a bandit hideout in the Whispering Woods.", "type": "slay", "stat": "attack", "anti_stat": "magic", "amt": 18, "item": "Skeleton Key", "dc": 10, "difficulty": "medium"},
    6: {"desc": "💥 Smash open a reinforced iron vault door holding stolen weapons.", "type": "fetch", "stat": "attack", "anti_stat": "speed", "amt": 15, "item": None, "dc": 12, "difficulty": "medium"},
    7: {"desc": "🐊 Hunt an armored giant alligator infesting the town docks.", "type": "slay", "stat": "attack", "anti_stat": "speed", "amt": 20, "item": None, "dc": 13, "difficulty": "medium"},
    8: {"desc": "🧊 Slay a rampaging Ice Golem blocking the mountain pass.", "type": "slay", "stat": "attack", "anti_stat": "magic", "amt": 22, "item": None, "dc": 14, "difficulty": "hard"},
    9: {"desc": "🦁 Subdue a corrupted manticore terrorizing mountain travelers.", "type": "slay", "stat": "attack", "anti_stat": "magic", "amt": 25, "item": "Cleric Potion", "dc": 16, "difficulty": "hard"},

    # Defense Reward Quests
    10: {"desc": "⛏️ Escort a dwarf miner safely out of a collapsed shaft.", "type": "fetch", "stat": "defense", "anti_stat": "speed", "amt": 12, "item": None, "dc": 5, "difficulty": "easy"},
    11: {"desc": "🎒 Return a lost backpack to an anxious traveling merchant.", "type": "fetch", "stat": "defense", "anti_stat": "attack", "amt": 14, "item": "Cleric Potion", "dc": 7, "difficulty": "easy"},
    12: {"desc": "💎 Deliver a flawless emerald to the blacksmith town.", "type": "fetch", "stat": "defense", "anti_stat": "speed", "amt": 15, "item": None, "dc": 8, "difficulty": "easy"},
    13: {"desc": "🧱 Assist a mason in rebuilding the collapsed city watchtower.", "type": "fetch", "stat": "defense", "anti_stat": "magic", "amt": 15, "item": None, "dc": 10, "difficulty": "medium"},
    14: {"desc": "⛈️ Protect a village shelter from a catastrophic thunderstorm.", "type": "fetch", "stat": "defense", "anti_stat": "attack", "amt": 16, "item": "Cleric Potion", "dc": 12, "difficulty": "medium"},
    15: {"desc": "🛡️ Break through a heavily armored Orc vanguard barricade.", "type": "slay", "stat": "defense", "anti_stat": "speed", "amt": 20, "item": None, "dc": 13, "difficulty": "medium"},
    16: {"desc": "🏰 Hold the frontline gate against a siege of skeleton warriors.", "type": "slay", "stat": "defense", "anti_stat": "speed", "amt": 22, "item": None, "dc": 15, "difficulty": "hard"},
    17: {"desc": "📦 Recover stolen cargo crates from river pirates.", "type": "fetch", "stat": "defense", "anti_stat": "magic", "amt": 24, "item": "Skeleton Key", "dc": 16, "difficulty": "hard"},
    18: {"desc": "🐉 Intercept a dragon's breath blast with a heavy tower shield.", "type": "slay", "stat": "defense", "anti_stat": "attack", "amt": 26, "item": "Cleric Potion", "dc": 18, "difficulty": "hard"},

    # Magic Reward Quests
    19: {"desc": "😈 Slay a Mischievous Imp pulling pranks on villagers.", "type": "slay", "stat": "magic", "anti_stat": "speed", "amt": 12, "item": None, "dc": 5, "difficulty": "easy"},
    20: {"desc": "🔮 Decipher ancient writings on a crumbling wayside shrine.", "type": "fetch", "stat": "magic", "anti_stat": "speed", "amt": 14, "item": None, "dc": 5, "difficulty": "easy"},
    21: {"desc": "🌾 Fetch rare Moon-Grass for a local herbalist.", "type": "fetch", "stat": "magic", "anti_stat": "attack", "amt": 15, "item": "Cleric Potion", "dc": 8, "difficulty": "easy"},
    22: {"desc": "⚡ Charge an ancient power pylon with controlled lightning spells.", "type": "fetch", "stat": "magic", "anti_stat": "attack", "amt": 15, "item": None, "dc": 8, "difficulty": "easy"},
    23: {"desc": "🔥 Extinguish a magical wildfire before it reaches the lumber mill.", "type": "fetch", "stat": "magic", "anti_stat": "speed", "amt": 16, "item": "Cleric Potion", "dc": 10, "difficulty": "medium"},
    24: {"desc": "🧪 Purify a poisoned town well using alchemical knowledge.", "type": "fetch", "stat": "magic", "anti_stat": "speed", "amt": 18, "item": None, "dc": 10, "difficulty": "medium"},
    25: {"desc": "🌀 Close an unstable elemental rift bursting in the courtyard.", "type": "slay", "stat": "magic", "anti_stat": "attack", "amt": 20, "item": "Skeleton Key", "dc": 12, "difficulty": "medium"},
    26: {"desc": "🧿 Banishing a demonic entity lurking inside an antique mirror.", "type": "slay", "stat": "magic", "anti_stat": "speed", "amt": 24, "item": "Skeleton Key", "dc": 14, "difficulty": "hard"},
    27: {"desc": "👁‍🗨 Slay a cursed Phantom Floating Eye near the graveyard.", "type": "slay", "stat": "magic", "anti_stat": "attack", "amt": 25, "item": None, "dc": 18, "difficulty": "hard"},

    # Speed Reward Quests
    28: {"desc": "🦉 Retrieve a lost owl familiar from the high canopy.", "type": "fetch", "stat": "speed", "anti_stat": "attack", "amt": 12, "item": None, "dc": 5, "difficulty": "easy"},
    29: {"desc": "🏃‍♂️ Catch a runaway clockwork courier tearing through the streets.", "type": "fetch", "stat": "speed", "anti_stat": "attack", "amt": 15, "item": "Skeleton Key", "dc": 7, "difficulty": "easy"},
    30: {"desc": "🍎 Gather Golden Apples from the top of the Sun-Hill.", "type": "fetch", "stat": "speed", "anti_stat": "magic", "amt": 15, "item": None, "dc": 7, "difficulty": "easy"},
    31: {"desc": "📜 Deliver an urgent war decree to the frontlines.", "type": "fetch", "stat": "speed", "anti_stat": "magic", "amt": 16, "item": None, "dc": 10, "difficulty": "medium"},
    32: {"desc": "🕊️ Chase down a thief who just snatched a noble's coin purse.", "type": "slay", "stat": "speed", "anti_stat": "magic", "amt": 16, "item": None, "dc": 12, "difficulty": "medium"},
    33: {"desc": "🕷 Slay an aggressive Giant Spider in a dark cave.", "type": "slay", "stat": "speed", "anti_stat": "attack", "amt": 18, "item": None, "dc": 12, "difficulty": "medium"},
    34: {"desc": "🗺️ Map out a shifting maze of sand dunes before a storm strikes.", "type": "fetch", "stat": "speed", "anti_stat": "attack", "amt": 20, "item": "Cleric Potion", "dc": 14, "difficulty": "hard"},
    35: {"desc": "🧗‍♂️ Scale a sheer cliffside to light the coastal warning beacon.", "type": "fetch", "stat": "speed", "anti_stat": "magic", "amt": 22, "item": None, "dc": 16, "difficulty": "hard"},
    36: {"desc": "🐎 Outrun a devastating mountain avalanche on horseback.", "type": "fetch", "stat": "speed", "anti_stat": "attack", "amt": 26, "item": "Skeleton Key", "dc": 18, "difficulty": "hard"}
}

anti_stat_messages = {
    "attack": [
        "⚠️ You tried to force it with brute strength, but this required precision! (Disadvantage applied)",
        "⚠️ Rash aggression is working against you here! (Disadvantage applied)"
    ],
    "magic": [
        "⚠️ The volatile nature of your magic is causing unexpected complications! (Disadvantage applied)",
        "⚠️ Mystical energies are backfiring in this environment! (Disadvantage applied)"
    ],
    "speed": [
        "⚠️ Rushing through has made you reckless and clumsy! (Disadvantage applied)",
        "⚠️ Moving too fast is causing critical mistakes! (Disadvantage applied)"
    ]
}

# Prints out text sequentially, character by character, to simulate typing.
def text_print(message, delay=0.02):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay) # Short pause to allow reading
    print()

# Displays the current health, stats, and non-empty items of the player.
def show_status():
    p = actors["Player"]
    print("\n=================== 📊 PLAYER STATUS ===================")
    print(f"👤 {p['name']} ({p['class']}) -> HP: {p['health']}/{p['max_health']} | ATK: {p['attack']} | DEF: {p['defense']} | MAG: {p['magic']} | SPD: {p['speed']}")
    print(f"🎒 Inventory: {dict((k,v) for k,v in inventory.items() if v > 0)}")
    print("=======================================================\n")

# Rolls two 20-sided dice and takes the lower result to calculate a penalized score.
def roll_with_disadvantage(stat_value):
    # Roll two dice (e.g., 1 to 20)
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    
    # Pick the worse one
    final_roll = min(roll1, roll2)
    total_score = final_roll + stat_value
    
    print(f"Rolled with Disadvantage: [{roll1}, {roll2}] -> Kept {final_roll}")
    return total_score

# ==========================================
# 🎭 CHARACTER CREATION
# ==========================================

# Prompts the player to name their character, choose a class, and pick a starting bonus item.
def character_creation():
    text_print("\n⚡ Waking up in a flash of divine validation... ⚡")
    text_print("Sage Malakor looks down at you: 'Ah, champion from Earth. The realm of Terra requires your skill!'")


    print("--- 🌟 CHARACTER CREATION 🌟 ---")
    
    name = input("\n\'📝 Reveal your name, traveler\': ").strip()
    actors["Player"]["name"] = name if name else "Hero"
    
    text_print(f"\n\'Welcome, {actors['Player']['name']}. Choose the 🛡️ Destiny you wish to uphold\':")
    print("1. Knight ⚔️   - Tanky, Reliable Armor, Low Spell Mastery")
    print("2. Wizard 🔮   - Heavy Magical Destructive Yield, Fragile Physical Framework")
    print("3. Rogue  🗡️   - High Speed, Striking Velocity, Agile Reflexes")
    
    choice = input("Select a class (1-3): ").strip()
    
    if choice == "1":
        actors["Player"]["class"] = "Knight"
        actors["Player"]["defense"] += 14
        actors["Player"]["attack"] += 6
        actors["Player"]["magic"] -= 8
        actors["Player"]["speed"] -= 4
    elif choice == "2":
        actors["Player"]["class"] = "Wizard"
        actors["Player"]["magic"] += 22
        actors["Player"]["attack"] -= 8
        actors["Player"]["defense"] -= 8
        actors["Player"]["speed"] -= 8
    else:
        actors["Player"]["class"] = "Rogue"
        actors["Player"]["speed"] += 10
        actors["Player"]["attack"] += 6
        actors["Player"]["defense"] -= 5
        actors["Player"]["magic"] -= 4

    text_print(f"\nThe old sage offers you a gift to aid your journey, {actors['Player']['class']}:")
    print("1. Cleric Potion 🧪 [Heals 50% health, can be used 3 times]")
    print("2. Skeleton Key 🔑  [Enables you to skip one fetch quest]")
    print("3. Growth Candy 🍬  [Instantly grants +10 to ALL base stats]")
    
    item_choice = input("Select your starting item (1-3): ").strip()
    
    if item_choice == "1":
        inventory["Cleric Potion"] = 3
        print("🎒 Added 3 Cleric Potions to your inventory.")
    elif item_choice == "2":
        inventory["Skeleton Key"] = True
        print("🎒 Added the Skeleton Key to your inventory.")
    else:
        print("🍬 You instantly eat the Growth Candy! You feel overwhelming power surge through you!")
        actors["Player"]["max_health"] += 6
        actors["Player"]["health"] += 6
        actors["Player"]["defense"] += 6
        actors["Player"]["attack"] += 6
        actors["Player"]["magic"] += 6
        actors["Player"]["speed"] += 6
        
    print("\n--- 📊 YOUR STARTING STATS ---")
    for key, value in actors["Player"].items():
        print(f"• {key.title()}: {value}")
    print("------------------------------\n")

# ==========================================
# ⚔️ COMBAT MECHANICS & UTILITIES
# ==========================================

# Consumes a potion to heal the player for half of their maximum health pool.
def use_potion():
    p_health = actors["Player"]["health"]
    p_max = actors["Player"]["max_health"]
    
    # Check if the player actually has any potions left to use
    if inventory["Cleric Potion"] <= 0:
        text_print("🧪 You check your pouch... Out of potions!")
        return False
        
    # Prevent consuming a potion if the player is already fully healthy
    if p_health >= p_max:
        text_print("💖 Your health is already full!")
        return False

    heal_amount = int(p_max * 0.50)
    actors["Player"]["health"] = min(p_health + heal_amount, p_max)
    inventory["Cleric Potion"] -= 1
    
    text_print(f"🧪 You drink a Cleric Potion! Restored {heal_amount} HP.")
    text_print(f"❤️ Current Health: {actors['Player']['health']}/{p_max} (Potions left: {inventory['Cleric Potion']})")
    return True

# Determines hit success and deducts calculated damage from the target's current health.
def calculate_damage(attacker_key, defender_key, attack_type):
    attacker = actors[attacker_key]
    defender = actors[defender_key]
    
    # An 80% accuracy check: if a number over 80 is rolled, the attack misses
    if random.randint(1, 100) > 80:
        text_print(f"💨 {attacker['name']}\'s attack missed completely!")
        return
    
    if attack_type == "magic":
        power = attacker["magic"]
        emoji = "✨"
    else:
        power = attacker["attack"]
        emoji = "⚔️"
        
    damage = power - defender["defense"]
    
    # Enforces a minimum structural damage floor of 5 so strong armor doesn't block everything
    if damage < 5:
        damage = 5
        
    defender["health"] -= damage
    if defender["health"] < 0:
        defender["health"] = 0
        
    text_print(f"{emoji} {attacker['name']} hits {defender['name']} for {damage} damage!")
    text_print(f"📊 {defender['name']} HP: {defender['health']}/{defender['max_health']}")

# Runs a standard turn-based encounter that continues until the player or enemy drops to 0 health.
def combat_loop(enemy_key):
    player = actors["Player"]
    enemy = actors[enemy_key]
    
    text_print(f"\n💥 BATTLE INITIATED: {player['name']} vs {enemy['name']}!")
    
    # Loop persists as long as both combatants remain conscious and have HP remaining
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\n--- {player['name']}: {player['health']} HP | {enemy['name']}: {enemy['health']} HP ---")
        
        action_chosen = False
        action = ""
        # Loop forces input processing until the user executes a valid command
        while not action_chosen:
            print("What will you do?")
            print("1. Physical Attack ⚔️")
            print("2. Magic Spell ✨")
            print("3. Drink Potion 🧪")
            choice = input("Choose an action (1-3): ").strip()
            
            if choice == "1":
                action = "attack"
                action_chosen = True
            elif choice == "2":
                action = "magic"
                action_chosen = True
            elif choice == "3":
                if use_potion():
                    action = "item"
                    action_chosen = True
            else:
                print("Invalid entry. Focus, hero!")

        # Compares speed stats to dictate which actor acts first during this combat step
        player_first = player["speed"] >= enemy["speed"]
        
        if player_first:
            if action != "item":
                calculate_damage("Player", enemy_key, action)
        else:
            # Dynamically chooses the enemy's offensive strategy based on their highest stat
            enemy_action = "magic" if enemy["magic"] > enemy["attack"] else "attack"
            calculate_damage(enemy_key, "Player", enemy_action)
            
        # Stop the combat round early if an entity dies during the initial strike
        if player["health"] <= 0 or enemy["health"] <= 0:
            break
            
        # Executes the response strike for the slower actor who has not yet acted
        if player_first:
            enemy_action = "magic" if enemy["magic"] > enemy["attack"] else "attack"
            calculate_damage(enemy_key, "Player", enemy_action)
        else:
            if action != "item":
                calculate_damage("Player", enemy_key, action)
                
    if player["health"] > 0:
        text_print(f"🏆 You defeated {enemy['name']}!")
        return True
    else:
        text_print(f"💀 You were bested by {enemy['name']}...")
        return False

# ==========================================
# 🗺️ RANDOMIZED SIDE QUESTLINES
# ==========================================

# Dynamically loops and picks random quest pools until the player logs 3 counted attempts or turns.
def side_quests():
    print("\n--- 🗺️ THE JOURNEY BEGINS ---")
    text_print("You set out across the wild lands of Terra to locate the Lich King\'s hidden tomb.")
    text_print("To build up your strength, you undertake 3 random adventurer contracts...")

    quest_num = 1
    free_refresh = 2
    
    # Loops continuously and won't stop until quest_num goes past 3.
    while quest_num <= 3:
        # Breaks the loop immediately if the player's health drops to 0 from failing challenges.
        if actors["Player"]["health"] <= 0:
            break
            
        # Picks a single completely random quest ID out of the entire pool for this specific loop turn.
        quest_id = random.choice(list(quest_pool.keys()))
        quest = quest_pool[quest_id]

        # Display quest information to user so they can make a meaningful decision
        statReward = quest['stat']
        diff = quest['difficulty']
        print(f"\n--- 📋 CONTRACT {quest_num}: {quest['desc']} | Difficulty: {diff.capitalize()} | Stat Reward: {statReward.capitalize()} ---")
        
        success = False
        # Evaluates if the quest type is a fetch and handles automatic items bypass using a skeleton key.
        if quest["type"] == "fetch" and inventory["Skeleton Key"]:
            print("🔑 Your Skeleton Key pulses with magical convenience!")
            use_key = input("Use the Skeleton Key to complete this quest automatically? (yes/no): ").strip().lower()
            if use_key == "yes":
                inventory["Skeleton Key"] = False
                text_print("🔑 The Skeleton Key bypasses the effort entirely! Quest complete!")
                success = True

        # User makes a decision of how they want to complete the side quest via picking which stat to use or refreshing
        if not success:

            show_status()
            
            if quest["type"] == "slay":
                print("1. Charge head-on into battle! ⚔️")
                print("2. Channel an incantation to blast them with magic! 🔮")
                print("3. Try to sneak attack from the shadows! 👤")
                print(f"4. Retreat to the safety of the guild to find a different quest. 🏃‍♂️ (Free Refreshes Left: {free_refresh} / 2)")
            else:
                print("1. Work hard and complete the task carefully. 🛠️")
                print("2. Cast a spell to conjure a magical solution! 🔮")
                print("3. Look around for a quick shortcut. 👀")
                print(f"4. Abandon the task and return to camp for a different quest. 🏃‍♂️ (Free Refreshes Left: {free_refresh} / 2)")
                
            questdecision = input("Choose your approach (1-4): ").strip()

            match questdecision:
                case "1":
                    contestStat = actors["Player"]["attack"] // 8
                    chosen_stat = "attack"
                    text_print(f"🎲 Rolling d20 using Attack with a modifier of +{contestStat} added to roll against a DC of {quest['dc']}...")
                    time.sleep(0.8)

                    if quest["anti_stat"] == chosen_stat:
                        print(random.choice(anti_stat_messages[chosen_stat]))
                        total_score = roll_with_disadvantage(contestStat)
                    else:
                        roll = random.randint(1, 20)
                        total_score = contestStat + roll
                        text_print(f"You rolled..... {total_score}")

                    if total_score >= quest["dc"]:
                        text_print("🌟 Success! You handled the contract like a professional.")
                        success = True
                    else:
                        text_print("❌ Failure! The task went sideways and you got hurt.")
                        text_print("💥 You take 15 damage!")
                        actors["Player"]["health"] -= 15
                        if actors["Player"]["health"] < 0:
                            actors["Player"]["health"] = 0
                case "2":
                    contestStat = actors["Player"]["magic"] // 8
                    chosen_stat = "magic"
                    text_print(f"🎲 Rolling d20 using Magic with a modifier of +{contestStat} added to roll against a DC of {quest['dc']}...")
                    time.sleep(0.8)

                    if quest["anti_stat"] == chosen_stat:
                        print(random.choice(anti_stat_messages[chosen_stat]))
                        total_score = roll_with_disadvantage(contestStat)
                    else:
                        roll = random.randint(1, 20)
                        total_score = contestStat + roll
                        text_print(f"You rolled..... {total_score}")

                    if total_score >= quest["dc"]:
                        text_print("🌟 Success! You handled the contract like a professional.")
                        success = True
                    else:
                        text_print("❌ Failure! The task went sideways and you got hurt.")
                        text_print("💥 You take 15 damage!")
                        actors["Player"]["health"] -= 15
                        if actors["Player"]["health"] < 0:
                            actors["Player"]["health"] = 0
                case "3":
                    contestStat = actors["Player"]["speed"] // 8
                    chosen_stat = "speed"
                    text_print(f"🎲 Rolling d20 using Speed with a modifier of +{contestStat} added to roll against a DC of {quest['dc']}...")
                    time.sleep(0.8)

                    if quest["anti_stat"] == chosen_stat:
                        print(random.choice(anti_stat_messages[chosen_stat]))
                        total_score = roll_with_disadvantage(contestStat)
                    else:
                        roll = random.randint(1, 20)
                        total_score = contestStat + roll
                        text_print(f"You rolled..... {total_score}")

                    if total_score >= quest["dc"]:
                        text_print("🌟 Success! You thought fast on your feet.")
                        success = True
                    else:
                        text_print("❌ Failure! The task went sideways and you got hurt.")
                        text_print("💥 You take 5 damage!")
                        actors["Player"]["health"] -= 5
                        if actors["Player"]["health"] < 0:
                            actors["Player"]["health"] = 0
                case "4":
                    text_print("Perhaps another quest may be more up your alley...")
                    # Checks if the player ran out of free refreshes. If so, increment quest_num to dock them a turn.
                    if free_refresh == 0:
                        print("⚠️  Warning! No more Free Refreshes, you are now losing turns!")
                        quest_num += 1
                    else:
                        free_refresh -= 1

        # Processes stat increases and items delivery strictly if the quest returns a success state flag.
        if success:
            quest_num += 1
            stat_name = quest["stat"]
            stat_amount = quest["amt"]
            
            actors["Player"][stat_name] += stat_amount
            text_print(f"💪 Reward: +{stat_amount} to your {stat_name.title()} stat!")
            
            if quest["item"] == "Cleric Potion":
                if inventory["Cleric Potion"] < 3:
                    inventory["Cleric Potion"] += 1
                    text_print("🧪 Found a Cleric Potion! Added to inventory.")
                else:
                    text_print("🧪 Found a Cleric Potion, but your bag can only hold 3!")
            elif quest["item"] == "Skeleton Key":
                inventory["Skeleton Key"] = True
                text_print("🔑 Found a Skeleton Key! Added to inventory.")

        # Prompts potion recovery systems if the player loop sustains injuries during tasks.
        if actors["Player"]["health"] < actors["Player"]["max_health"] and actors["Player"]["health"] > 0:
            show_status()
            text_print("Would you like to use a potion?\n")
            print("1. Yes ✔")
            print("2. No ❌")
            restchoice = input("Choose an action (1-2): ").strip()
            
            if restchoice == "1":
                use_potion()
                text_print("After taking a short rest, you trek onwards to your next quest...\n")
            else:
                text_print("You trek onwards to your next quest...\n")
                

# ==========================================
# 🃏 PRECURSOR OBJECTIVE: SKELLY THE JESTER
# ==========================================

# Manages the interactions with Skelly the Jester, running a riddle challenge or initiating combat.
def skelly_encounter():
    if actors["Player"]["health"] <= 0:
        return

    print("\n==============================================")
    print("🃏 AN ECCENTRIC FOE APPEARS 🃏")
    print("==============================================")
    
    text_print("Skelly: \'Well, well, well, look who made it through the script!\'")
    text_print("Skelly: \'A fleshy little bundle controlled by clicks and typed-out inputs!\'")
    text_print("Skelly: \'To open up the tomb, you need the shiny Skull King Key...\'")
    text_print("Skelly: \'But beating me in combat takes a while, as you will see!\'")
    text_print("Skelly: \'So let us play a little game to save some code execution time...\'")
    text_print("Skelly: \'Answer my riddle true, or enjoy a grueling, painful grind!\'")

    print("\nSkelly tilts his head and grins, juggling a glowing bone key.")
    print("1. Challenge his riddle! 🧠")
    print("2. Draw your weapon and fight! ⚔️")
    choice = input("Your choice (1-2): ").strip()

    riddles = [
        {
            "q": "What disappears as soon as you say its name?",
            "a": ["silence"]
        },
        {
            "q": "What comes once in a minute, twice in a moment, but never in a thousand years?",
            "a": ["the letter m", "m"]
        },
        {
            "q": "This belongs to you, but everyone else uses it.",
            "a": ["your name", "my name", "name"]
        }
    ]

    if choice == "1":
        selected_riddle = random.choice(riddles)
        
        print(f"\nSkelly cackles: \'A scholar! Fascinating! Here is your prompt:\'")
        text_print(f"👉 \"{selected_riddle['q']}\"")
        
        player_ans = input("Type your answer: ").strip().lower()
        
        correct = False
        # Scans through all viable answer variations to verify if the player typed the solution phrase
        for valid_answer in selected_riddle["a"]:
            if valid_answer in player_ans:
                correct = True
                break
                
        if correct:
            print("\nSkelly: \'Gasp! Impossibility! You read the source code, didn\'t you?!\'")
            text_print("Skelly: \'An intellectual giant! A magnificent digital brain!\'")
            text_print("Skelly: \'Take the Skull King Key! You skipped the fight and bypassed all the pain!\'")
            
            eligible_stats = ["defense", "attack", "magic", "speed"]
            chosen_stat = random.choice(eligible_stats)
            actors["Player"][chosen_stat] += 8
            
            text_print(f"🔑 Received: Skull King Key!")
            text_print(f"✨ Brain Power Bonus: Your {chosen_stat.title()} stat increased by +8!")
            return
            
        else:
            print("\nSkelly: \'WRONG! Oh, completely wrong! My grandma\'s dial-up has more processing power!\'")
            text_print("Skelly: \'You thought you were a genius, but your logic turned quite sour!\'")
            text_print("Skelly: \'Now my chaotic jester curse will make your pixels— er... I mean text? Yeah, text! It will make your text weak...\'")
            text_print("Skelly: \'Prepare to face my bells and whistles with a outlook rather bleak!\'")
            
            print("\n📉 DEBUFF ACTIVATED: Skelly\'s mockery lowers ALL your base stats by -3!")
            for stat in ["defense", "attack", "magic", "speed"]:
                actors["Player"][stat] = max(1, actors["Player"][stat] - 3)
                
    else:
        print("\nSkelly: \'Straight to violence? Boring! Where is the thematic flair?!\'")
        text_print("Skelly: \'Fine, press your attack buttons and let\'s see how you fare!\'")

    victory = combat_loop("Skelly")
    
    if victory:
        text_print("\nSkelly: \'Ouch! My hit points reached absolute zero...\'")
        text_print("Skelly: \'Fine, take the key, you overpowered brute-force hero...\'")
        text_print("🔑 Received: Skull King Key!")
    else:
        text_print("\nSkelly: \'Geeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeet DUNKED ON! LOLOLOLOL!\'")
        text_print("\nSkelly dances over your defeated character sprite!")

# ==========================================
# 👑 THE FINAL CONFRONTATION: LICH KING ZAVLA
# ==========================================

# Adjusts the final boss's speed and offense parameters upward if player defenses become too high.
def scale_final_boss_stats():
    player = actors["Player"]
    boss = actors["Zavla"]
    
    # Base Scaling rules for Speed (keeps him competitive but slightly slower)
    boss["speed"] = max(1, player["speed"] - 1)
    
    # Anti-tinkering bypass: if the player stacks pure defense, the boss forces an armor-shattering value
    if player["defense"] > boss["attack"] or player["defense"] > boss["magic"]:
        boss["attack"] = player["defense"] + 8
        boss["magic"] = player["defense"] + 8
        print("\n⚡ *Zavla senses your immense armor! His weapons pulse with shattering armor-piercing energy!* ⚡")

# Manages the final encounter with Zavla, requiring anatomy puzzle inputs to dispel his defensive ward.
def final_boss_battle():
    player = actors["Player"]
    boss = actors["Zavla"]
    
    shield_active = True
    shield_uses_left = 6
    
    trivia_pool = [
        {"q": "An adult human has 206 bones, but about how many does a baby have at birth?", "a": ["300"]},
        {"q": "Which two extremities contain over half of all the bones in your skeleton?", "a": ["hand", "feet", "foot"]},
        {"q": "What is the name of the longest and strongest bone in the human body?", "a": ["femur"]},
        {"q": "The stapes is the smallest bone in the body. Roughly how long is it in millimeters?", "a": ["2", "3", "two", "three"]},
        {"q": "Which singular skull bone does not articulate (connect) with any other bone?", "a": ["hyoid"]},
        {"q": "True or False: Bone is the hardest substance in the human body.", "a": ["false"]}
    ]
    
    random.shuffle(trivia_pool)
    question_index = 0

    print("\n==============================================")
    print("👑 THE FINAL SHOWDOWN 👑")
    print("==============================================")
    text_print("Lich King Zavla: \'So, you crawled through my valley and outsmarted my jester...\'")
    text_print("Lich King Zavla: \'But your little adventure ends here, mortal!\'")
    text_print("❄️ A blast of freezing wind fills the chamber. A massive aura of bone shards protects him!")
    text_print("⚠️ WARNING: Zavla\'s Necrotic Shield is ACTIVE. Normal attacks will deal 0 damage!")

    # Standard loop running until one side drops to zero health points
    while player["health"] > 0 and boss["health"] > 0:
        print(f"\n--- ❤️ HERO: {player['health']} HP | 👑 ZAVLA: {boss['health']} HP ---")
        
        # When shield is up, forces the user to solve trivia before conventional actions become active
        if shield_active and question_index < len(trivia_pool):
            print("\n🛡️ Zavla\'s Necrotic Shield is absorbing all energy! You must find a flaw in its anatomy!")
            current_trivia = trivia_pool[question_index]
            print(f"💀 TRIVIA CHALLENGE: {current_trivia['q']}")
            
            ans = input("Your answer: ").strip().lower()
            question_index += 1
            
            correct = False
            for keyword in current_trivia["a"]:
                if keyword in ans:
                    correct = True
                    break
                    
            if correct:
                text_print("💥 CRACK! Your bone expertise exposes a flaw in the spell! The shield shatters!")
                # NEW BALANCE MECHANIC: Reward correct answers with direct flat damage to the boss
                boss["health"] = max(0, boss["health"] - 20)
                text_print("⚡ Feedback loop! Shaking his magical foundations deals 20 TRUE damage to Zavla!")
                shield_active = False
            else:
                text_print("❌ WRONG! The ancient magical forces backfire completely!")
                text_print("💥 The shield explodes violently, dealing 20 damage to you!")
                player["health"] = max(0, player["health"] - 20)
                
                text_print("📉 DEBUFF: The necrotic energy dampens your spirit! (-2 Defense)")
                player["defense"] = max(1, player["defense"] - 2)
                
                shield_active = False
                
            if player["health"] <= 0 or boss["health"] <= 0:
                break

        # Standard action menu skipped if the feedback loop killed him early
        if boss["health"] <= 0:
            break

        print("\nWhat will you do?")
        print("1. Physical Attack ⚔️")
        print("2. Magic Spell ✨")
        print("3. Drink Potion 🧪")
        choice = input("Choose an action (1-3): ").strip()
        
        player_action = ""
        if choice == "1":
            player_action = "attack"
        elif choice == "2":
            player_action = "magic"
        elif choice == "3":
            if use_potion():
                player_action = "item"
            else:
                continue
        else:
            player_action = "attack"

        player_first = player["speed"] >= boss["speed"]
        
        if player_first:
            if player_action != "item":
                calculate_damage("Player", "Zavla", player_action)
        else:
            calculate_damage("Zavla", "Player", "attack")
            
        if player["health"] <= 0 or boss["health"] <= 0:
            break
            
        if player_first:
            calculate_damage("Zavla", "Player", "attack")
        else:
            if player_action != "item":
                calculate_damage("Player", "Zavla", player_action)

        # Triggers shield regeneration automatically if the boss survived the current round
        if boss["health"] > 0 and not shield_active and shield_uses_left > 0:
            shield_uses_left -= 1
            shield_active = True
            print(f"\n🔮 Zavla channels pure death magic! Necrotic Shield restored! (Regens left: {shield_uses_left})")

    return player["health"] > 0

# ==========================================
# 🎮 THE MAIN ORCHESTRATION LOOP
# ==========================================

# Directs execution flow across setup, side quests, intermediate encounter, optional grinding, and the final boss.
def main():
    print("==============================================")
    print("✨ WELCOME TO THE ISEKAI OF TERRA ✨")
    print("==============================================")
    
    character_creation()
    
    print("\n=================== 📜 THE PROPHECY ===================")
    text_print("Terra was peaceful until Zavla the Lich King shattered the ancient seals.")
    text_print("Now, undead armies spill across the valleys like a permanent shadow.")
    text_print("Your cell structures allow you to assimilate raw knowledge from physical tasks.")
    text_print("Gain strength, accumulate safe allies, unlock the sealed tomb, and save Terra!")
    text_print(f"Save us, {actors["Player"]["name"]}! O' Hero of Amazing Potential!")
    print("========================================================\n")
    time.sleep(1)
    
    side_quests()
    
    if actors["Player"]["health"] <= 0:
        print("\n💀 Your journey cut short by the perils of Terra. GAME OVER.")
        return

    skelly_encounter()
    
    if actors["Player"]["health"] <= 0:
        print("\n💀 Skelly\'s tricks were too much for your code structure. GAME OVER.")
        return

    show_status()

    text_print("Would you like to go on 3 more quests before facing the Zavla?\n")
    print("1. Yes ✔")
    print("2. No ❌")
    mainchoice = input("Choose an action (1-2): ").strip()

    if mainchoice == "1":
        side_quests()
    else:
        text_print("You trek onwards to Zavla's tomb, confident in your abilities.\n")
        
    # Call the scaling helper function here to rewrite the dictionary right before combat!
    scale_final_boss_stats()

    game_won = final_boss_battle()
    
    print("\n==============================================")
    if game_won:
        print("🎉 CONGRATULATIONS! YOU HAVE SAVED TERRA! 🎉")
        text_print("Zavla turns to ash, his throne collapses, and light returns to the fantasy realm.")
        text_print("The residents of Terra build a massive digital monument to your name!")
        text_print(f"Long Live the Hero: {actors["Player"]["name"]} the Great and Powerful!")
    else:
        print("💀 GAME OVER 💀")
        text_print("Your character sprite collapses onto the icy floor.")
        text_print("Zavla reigns supreme, and your code file rests in peace.")
        text_print(f"We shall remember your courage, courageous hero {actors["Player"]["name"]}...")
    print("==============================================")

if __name__ == "__main__":
    main()