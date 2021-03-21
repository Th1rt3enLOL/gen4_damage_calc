#variables
power = int()
physical = str()
STAB = str()
effectiveness = float()
crit = str()
level = int()
attack = int()
attack_stage = int()
attack_modifier = float()
defense = int()
defense_stage = int()
defense_modifier = float()
damage_modifier = float()
damage_min = float()
damage_max = float()
#input move
power = int(input("attack's power: "))
while power <= 0:
    power = int(input("power must be positive: "))
physical = input("is the move physical or special?: ")
while physical != "physical" and physical != "special":
    physical = input("you must enter 'physical' or 'special': ")
STAB = input("is the move's type the same as the attacking pokemon's type?: ")
while STAB != "yes" and "no":
    STAB = input("you must enter 'yes' or 'no': ")
effectiveness = float(input("the moves effectiveness in decimal form: "))
while effectiveness != 0 and effectiveness != .25 and effectiveness != .5 and effectiveness != 1 and effectiveness != 2 and effectiveness != 0 and effectiveness != 4:
    effectiveness = float(input("not a valid input: "))
crit = input("does the move crit?: ")
while crit != "yes" and crit != "no":
    crit = input("you must enter 'yes' or 'no': ")
#input pokemon stats
level = int(input("attacking pokemon level: "))
while level < 1 or level > 100:
    level = int(input("level must be an integer between 1 and 100 inclusive: "))
if physical == "physical":
        attack = int(input("attacking pokemon attack stat: "))
        while attack <= 0:
            attack = int(input("attack must be positive: "))
        attack_stage = int(input("attacking pokemon attack stage: "))
        while attack_stage < -6 or attack_stage > 6:
            attack_stage = int(input("not a valid input: "))
        defense = int(input("defending pokemon defense stat: "))
        while defense <= 0:
            defense = int(input("defense must be positive: "))
        defense_stage = int(input("defending pokemon defense stage: "))
        while defense_stage < -6 or attack_stage > 6:
            defense_stage = int(input("not a valid input: "))
elif physical == "special":
        attack = int(input("attacking pokemon special attack stat: "))
        while attack <= 0:
            attack = int(input("special attack must be positive: "))
        attack_stage = int(input("attacking pokemon special attack stage: "))
        while attack_stage < -6 or attack_stage > 6:
            attack_stage = int(input("not a valid input: "))
        defense = int(input("defending pokemon special defense stat: "))
        while defense <= 0:
            defense = int(input("special defense must be positive: "))
        defense_stage = int(input("defending pokemon special defense stage: "))
        while defense_stage < -6 or attack_stage > 6:
            defense_stage = int(input("not a valid input: "))
#attack modifier
if attack_stage == -6:
    attack_modifier = .25
elif attack_stage == -5:
    attack_modifier = .2857
elif attack_stage == -4:
    attack_modifier = .3333
elif attack_stage == -3:
    attack_modifier = .4
elif attack_stage == -2:
    attack_modifier = .5
elif attack_stage == -1:
    attack_modifier = .6667
elif attack_stage == 0:
    attack_modifier = 1
elif attack_stage == 1:
    attack_modifier = 1.5
elif attack_stage == 2:
    attack_modifier = 2
elif attack_stage == 3:
    attack_modifier = 2.5
elif attack_stage == 4:
    attack_modifier = 3
elif attack_stage == 5:
    attack_modifier = 3.5
elif attack_stage == 6:
    attack_modifier = 4
#defense modifier
if defense_stage == -6:
    defense_modifier = .25
elif defense_stage == -5:
    defense_modifier = .2857
elif defense_stage == -4:
    defense_modifier = .3333
elif defense_stage == -3:
    defense_modifier = .4
elif defense_stage == -2:
    defense_modifier = .5
elif defense_stage == -1:
    defense_modifier = .6667
elif defense_stage == 0:
    defense_modifier = 1
elif defense_stage == 1:
    defense_modifier = 1.5
elif defense_stage == 2:
    defense_modifier = 2
elif defense_stage == 3:
    defense_modifier = 2.5
elif defense_stage == 4:
    defense_modifier = 3
elif defense_stage == 5:
    defense_modifier = 3.5
elif defense_stage == 6:
    defense_modifier = 4
#damage modifier
damage_modifier = effectiveness
if STAB == "yes":
    damage_modifier = damage_modifier * 1.5
if crit == "yes":
    damage_modifier = damage_modifier * 2
    if attack_modifier < 1:
        attack_modifier = 1
    if defense_modifier > 1:
        defense_modifier = 1
#calculate damage
damage_max = ((.4 * level + 2) * power * attack * attack_modifier / defense / defense_modifier / 50 + 2) * damage_modifier
damage_min = damage_max * .85
print("expected damage is between " , damage_min , " and " , damage_max)
