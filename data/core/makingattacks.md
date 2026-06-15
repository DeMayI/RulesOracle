---
title: Making Attacks
description: An overview of how to make attacks
---

### 1. Hit Roll
When a model makes an attack, you must first make a Hit roll by rolling one D6. 
If the result of that hit roll is greater than or equal to 7 minus the models BS (If the attack is being made by a ranged weapon) then the hit roll succeds, otherwise the attack fails and the sequence ends. 

An umodified Hit roll of a 1 always fails, and an unmodified Hit roll of 6 is called a critical hit and is always successful. A hit roll can never be modified by more than +1. 

If the unit has a BS (if the attack is made by a ranged weapon) or WS (if the attack is made by a melee weapon) greater than 6, you may reroll reroll one hit dice for that unit each time it shoots/fights for each point greater than 6. 

If the attack is being made by a ranged weapon, measure the shortest distance between the attacking unit and the target unit. If that range is less than or equal to the weapons Short(S) range, then no range modifiers are applied. If the range is instead less than or equal to the weapons Medium(M) range but not in Short range, a -1 to hit modifier is applied to the attack. If the weapon is less than or equal to the weapons Long(L) range, but not in Short or Medium range, a -2 to hit modifier is applied to the attack. 

#### Example
| BS/WS | Rerolls |
| --- | --- |
| <= 6 | 0 |
| 7 | 1 |
| 8 | 2 |
| 9 | 3 |

If the attack is made with a melee weapon compare the targets weapon skill with the bearers weapon skill using the table below.

| Your WS vs Target WS | D6 Result Required |
| ----- | ----- |
| Your WS is greater than Target WS | 3+ |
| Your WS is less than or equal to Target WS | 4+ |
| Your WS is less than or equal to half of Target WS | 5+ |

### 2. Wound Roll
Each time an attack scores a hit against a non VEHICLE unit, make a wound roll for that attack by rolling one D6 to see if the attack successfully wounds the target unit. The result required is determined by comparing the attack's Strength(S) characteristic with the target's Toughness (T) characteristic, as shown below. See [Vehicles](/0thEdition/core/vehicle) for information how to handle attacking vehicles. 

| Attacks Strength VS Target Toughness | D6 Result Required |
| ------- | ------- |
| Strength is or 2 or more points greater than Toughness | 2+ |
| Stength is 1 point greater than Toughness | 3+ |
| Strength is equal to Toughness | 4+ |
| Strength is 1 point less than Toughness | 5+ |
| Strength is 2 or more points less than Toughness | 6+ |

#### Example:
| Strength | Toughness | D6 Result Required |
| --- | --- | --- |
| 3 | 3 | 4+ |
| 3 | 4 | 5+ |
| 3 | 5 | 6+ |
| 4 | 3 | 3+ |
| 5 | 3 | 2+ |

### 3. Allocate Attack
If an attack successfully wounds the target a unit, the controlling player must allocate that attack to one model in the target unit as follows.

If a model in the target unit has already lost one or more wounds, or has already had attacks allocated to it in this phase, that atack must be allocated to that model. 

The model selected must either be in engagement range of the attacking unit, or visible to at least one model in the attacking unit. If no such model exists the attack sequence ends. 

### 4. Saving Throw
The player controlling the target unit then makes one saving throw using their models Save (Sv). To make a saving throw, roll one D6 then modifiy the result by the weapons Armor Penetration(AP). For example if the attack has an AP of -1 then 1 is subtracted from the saving throw. If the result is greater than or equal to the Save characteristic, then the throw is successful and the attack sequence ends. Otherwise the saving throw fails and that model suffers damage. An unmodifiable saving throw of 1 always fails and a saving throw can never be improved by more tha +1.

#### Invulnerable Saves
Some models have an invulnerable save listed on their datasheet. Each time an attack is allocated to a model with an invulnerable save, before making any saving throws, roll one d6. If the result is greater than or equal to the the characteristic listed then the throw is sucessfull and the attack sequence ends. A model may only ever use one invulnerable save, and if a model has more than one invulnerable save the controlling player must choose which one to use before making any invulnerable saving throws. 

#### Cover Saves
Some models have a cover save. If a model has a cover save, before making any saving throws or any invulnerable saving throws, roll one d6. If the result is greater than or equal to the models cover save, the cover successfully protects the model and the attack sequence ends. A model may only ever use one cover save, and if a model has more than one cover save its controlling player must pick which one to use before making any cover saving throws. Cover saves may only be made against ranged attacks. 

If a model has the MONSTER or VEHICLE keyword, an umodified result of 1-5 always fails. 

### 5. Inflict Damage
The damage inflicted is equal to the Damage (D) characteristic of the attack. For each point of damage, the model will lose one wound. If a model is reduced to 0 wounds or less, it is destroyed and removed from play, any excess damage inflicted by that attack is lost. 

#### Mortal Wounds
Some rules inflict mortal wounds on units. Each time mortal wounds are inflicted on a unit, each mortal wound inflicts one point of damage to that unit, in the same manner as allocating an attack. However, excess damage is not lost and spills over between models until there are no mortal wounds remaining. If targeting a vehicle, the player who caused the mortal wounds may decide which location suffers damage. If these mortal wounds are the result of the HAZARDOUS ability, they must first target the location with that HAZARDOUS weapon, or any location with a HAZARDOUS weapon if it is not possible to determine which location should be hit due to fast rolling different weapons at once. 

#### Feel No Pain
Some models have the Feel No Pain X+ listed in their abilities. Each time a model with this ability suffers damage and loses a wound(including as a result of mortal wounds), roll one d6. If the result is greater than or equal to the number denoted by 'X', that wound is ignored and not lost. If a model has more than one Feel No Pain ability you can only use one of those abilities each time the model suffers damage. 