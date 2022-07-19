from random import random


import random
import json

races = ["Human", "Dwarf", "Elf", "Orc", "Halfling", "Dragonborn", "Gnome", "Goliath"]
classes = ["Bard", "Barbarian", "Cleric", "Fighter", "Monk", "Paladin", "Ranger", "Rouge", "Sorcerer", "Warlock", "Wizard," "Druid", "Warrior"]

randomIndex = random.randint(0, len(classes) -1)


def __getAbilityScores__(characterClasses):

    scores = []
    for x in range(6):

        score = []
        for x in range(4):
            score.append(random.randint(1,6))

        scores = sorted(scores)
        score.pop(0)
        scores.append(sum(score))

        score = sorted(score)
        arrangedScores = {'STR' :0, 'DEX' :0, 'CON' :0, 'INT' :0, 'WIS' :0, 'CHA' :0}
    
    match characterClasses:
        case "Bard":
            arrangedScores["CHA"] = scores[5]
            arrangedScores["INT"] = scores[4]
            arrangedScores["DEX"] = scores[3]
            arrangedScores["WIS"] = scores[2]
            arrangedScores["STR"] = scores[1]
            arrangedScores["CON"] = scores[0]   
        case "Barbarian":
            arrangedScores["CON"] = scores[5]
            arrangedScores["STR"] = scores[4]
            arrangedScores["CHA"] = scores[3]
            arrangedScores["DEX"] = scores[2]
            arrangedScores["CHA"] = scores[1]
            arrangedScores["WIS"] = scores[0]
        case "Cleric":
            arrangedScores["WIS"] = scores[5]
            arrangedScores["CON"] = scores[4]
            arrangedScores["DEX"] = scores[3]
            arrangedScores["STR"] = scores[2]
            arrangedScores["INT"] = scores[1]
            arrangedScores["CHA"] = scores[0]
        case "Paladin":
            arrangedScores["STR"] = scores[5]
            arrangedScores["CHA"] = scores[4]
            arrangedScores["CON"] = scores[3]
            arrangedScores["WIS"] = scores[2]
            arrangedScores["DEX"] = scores[1]
            arrangedScores["INT"] = scores[0]
        case "Ranger":
            arrangedScores["DEX"] = scores[5]
            arrangedScores["WIS"] = scores[4]
            arrangedScores["STR"] = scores[3]
            arrangedScores["CON"] = scores[2]
            arrangedScores["CHA"] = scores[1]
            arrangedScores["INT"] = scores[0]
        case "Rouge":
            arrangedScores["DEX"] = scores[5]
            arrangedScores["CON"] = scores[4]
            arrangedScores["CHA"] = scores[3]
            arrangedScores["WIS"] = scores[2]
            arrangedScores["STR"] = scores[1]
            arrangedScores["INT"] = scores[0]
        case "Sorcerer":
            arrangedScores["CHA"] = scores[5]
            arrangedScores["DEX"] = scores[4]
            arrangedScores["CON"] = scores[3]
            arrangedScores["INT"] = scores[2]
            arrangedScores["WIS"] = scores[1]
            arrangedScores["STR"] = scores[0]
        case "Warlock":
            arrangedScores["CHA"] = scores[5]
            arrangedScores["DEX"] = scores[4]
            arrangedScores["CON"] = scores[3]
            arrangedScores["INT"] = scores[2]
            arrangedScores["WIS"] = scores[1]
            arrangedScores["STR"] = scores[0]
        case "Druid":
            arrangedScores["WIS"] = scores[5]
            arrangedScores["DEX"] = scores[4]
            arrangedScores["CON"] = scores[3]
            arrangedScores["INT"] = scores[2]
            arrangedScores["CHA"] = scores[1]
            arrangedScores["STR"] = scores[0]
        case "Fighter":
            arrangedScores["STR"] = scores[5]
            arrangedScores["DEX"] = scores[4]
            arrangedScores["CON"] = scores[3]
            arrangedScores["CHA"] = scores[2]
            arrangedScores["WIS"] = scores[1]
            arrangedScores["INT"] = scores[0]
        case "Monk":
            arrangedScores["DEX"] = scores[5]
            arrangedScores["WIS"] = scores[4]
            arrangedScores["CON"] = scores[3]
            arrangedScores["STR"] = scores[2]
            arrangedScores["CHA"] = scores[1]
            arrangedScores["INT"] = scores[0]
        case "Wizard":
            arrangedScores["INT"] = scores[5]
            arrangedScores["DEX"] = scores[4]
            arrangedScores["CON"] = scores[3]
            arrangedScores["CHA"] = scores[2]
            arrangedScores["WIS"] = scores[1]
            arrangedScores["STR"] = scores[0]

    return arrangedScores



class character:
    def __init__( self ):
        self.race = races[random.randint(0, len(races) -1)]
        self.characterClasses = classes[random.randint(0, len(classes) -1)]
        self.abilityScores = __getAbilityScores__(self.characterClasses)



newCharacter = character()
print(json.dumps(newCharacter.__dict__))
