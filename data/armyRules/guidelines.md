---
title: Guidelines
description: Some guidelines to follow when crafting 10th edition army rules
---

### The MOST Important guideline
Make your army rules unique and flavorful! The goal for this edition is for everyones armys to feel fun and unique! No two army rules should feel similar like they do in 10th edition

### What should army rules affect
Your whole army! make something fun and flavorful that represents the entirety of your army if possible! Like reanimation protocols for necrons for example. 

What is allowed:
Pretty much everything so long as its not overpowered! The goal however is to heavily limit rerolls, so reserve them for when you feel like they realy deserve rerolls.(like a primarch for example)  Rember a high WS/BS gives you some rerolls!
Our goal is also to limit/avoid the use of anti weapons, as its just more fun/interesting when the opponents stats actually matter. 

### Secondary Army Rules
Secondary Army rules that only affect specific units from your army(like in order to represent a specific subfaction in you rules) are also allowed! 

### Weaknesses 
Dont give your army everything! The more special/strong your army is in one area it should have weaknesses in another to compensate. EX Knights being weaker in melee than in range, Custodes having weaker shooting and their eliteness, Tau having weak melee, etc. There should be counterplay to your army!

### Warlord Traits
Similarly to 9th Edition, when constructing your army you may buy warlord traits for your warlord. Each player may only select 1 warlord trait. Be sure to make a list of ~6 Warlord traits for your army to choose from.

### Relics
Similary to 9th edition, when constructing your army you may also buy relics for any character models in your army. Be sure to make a list of relics for your army to choose from. These relics can offer unique abilities, stateline changes, or even completly replace a weapon profile!

### Additional Upgrades
These are optional upgrades for elite units in your army. Think tank ace upgrades for guard in 9th or exalted court upgrades for knights in 9th. You do not need to write these upgrades for your army, this just gives you an additional way of providing customization to elite/key units like tanks/knights/demons. These upgrades must be bought with points. 

### Strategems
Each army will have 4 Generic Strategems that are always available to them. Think armor of contempt for space marines or rotate ion shields for knights. 

### Detachments
Similarly to 10th edition, there will be detachments that represent a specific playstyle or aspect of your army! You can borrow some ideas from existing 10th edition detachments(but dont copy them word for word) or create your own unqiue detachments. Each detachment must have a detachment rule, 1 warlord trait, 1 relic, 3 enchancements, and 4 strategems available to that detachment. 

### Enhancements
Enhancements work just like they do in 10th edition, with 1 key difference. They are not restricted to characters by default. This opens up the design space for enhancements to units like dreadnoughts without turning them into characters first! 


### Format
All army rules are to be written in markdown. Not to fear, markdown is super easy to use/write in! Some quick basics so you can write your own army rules. Make sure to make 2 markdown pages, one for the army rules and one for the datasheets. Datasheets should be grouped together by ## headers and named with ### headers. 

Page Title/Description
```md
---
title: My Title
description: My description
---
```
Headings use ## and ### to create headings! The more # the smaller the heading is!

```md
---
title: Markdown Guide
description: How to use Markdown
---

## Inline Styles
body text

### Headings

```
Tables: Create tables using the following format, The number of "-" changes how wide the cell is!
```md
| Syntax | Description |
| ----- | ----- |
| Header | Title |
| Paragraph | Text |
```
| Syntax | Description |
| ----- | ----- |
| Header | Title |
| Paragraph | Text |

Example Datasheet in Markdown
```md
## Datasheet Examples

### Intercessor Squad
| M | BS | WS | T | W | Sv | Inv | I | AC | Ld | CL | Wil | Int |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 7" | 4 | 4 | 4 | 1 | 3+ | N/A | 4 | 3 | 6+ | 6+ | 6+ | 6+ |


##### Weapons
| Ranged Weapons | Abilites | Short Range | Medium Range | Long Range | A | S | AP | D | Cost |
| ------ | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- |
| Astartes grenade launcher-frag | BLAST | 12" | 18" | 24" | D3 | 4 | 0 | 1 | 5pts |
| Astartes grenade launcher-krak | BLAST | 12" | 18" | 24" | 1 | 6 | -2 | 2 | 5pts |
| Bolt Pistol | Pistol | 6" | 9" | 12" | 1 | 4 | 0 | 1 | 
| Bolt Rifle | Assault | 12" | 18" | 24" | 2 | 4 | 0 | 1 | 
| Hand Flamer | Ignores Cover Pistol Torrent | N/A | N/A | 12" | D6 | 3 | 0 | 1 | 5pts |
| Plasma Pistol - standard | Pistol Breaching 6+| 6" | 9" | 12" | 1 | 5 | -2 | 1 | 5pts |
| Plasma pistol - supercharge | Hazardous Pistol Breaching 5+ | 6" | 9" | 12" | 1 | 6 | -2 | 1 | 5pts |

| Melee Weapons | Abilities | IM | A | S | AP | D | Cost |
| ----- | ---- | --- | --- | --- | --- | --- | --- |
| Astartes chainsword | | 0 | 4 | 4 | -1 | 1 |
| Close combat weapon | | 0 | 2 | 4 | 0 | 1 |
| Power Fist | | -3 | 3 | 8 | -3 | 2 | 5pts |
| Power Weapon | | 0 | 3 | 5 | -2 | 1 | 5pts |
| Thunder Hammer | Cleave 2" | -2 | 3 | 7 | -3 | 2 | 5pts |

##### Wargear Options
- The Intercessor Sergeant's bolt rifle can be replaced with one of the following:
    - 1 Astartes chainsword
    - 1 Hand flamer
    - 1 Plasma pistol
    - 1 Power Weapon
- The Intercessor Sergeant's close combat weaon can be replaced with one of the following:
    - 1 Astartes chainsword
    - 1 Power Fist
    - 1 Power Weapon
    - 1 Thunder Hammer
- For Every 5 models in this unit, 1 model equipped with a bolt rifle can be equipped with 1 Astartes grenade launcher. 

##### Abilities
-Insert Faction Ability Here
-Target Elimination: Each time this unit is selected to shoot, if it remained stationary this turn, add the Sustained Fire 1 ability to bolt rifles equipped by models in this unit and you can only select one enemy unit as the target of all of this units attacks.

##### Unit Composition
- 1 Intercessor Sergeant
- 4-9 Intercessors
Every model is equipped with bolt pistol, bolt rifle, and close combat weapon.
```



## Datasheet Examples

### Intercessor Squad
| M | BS | WS | T | W | Sv | Inv | I | AC | Ld | CL | Wil | Int |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 7" | 4 | 4 | 4 | 1 | 3+ | N/A | 4 | 3 | 6+ | 6+ | 6+ | 6+ |

##### Weapons
| Ranged Weapons | Abilites | Short Range | Medium Range | Long Range | A | S | AP | D | Cost |
| ------ | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- |
| Astartes grenade launcher-frag | BLAST | 12" | 18" | 24" | D3 | 4 | 0 | 1 | 5pts |
| Astartes grenade launcher-krak | BLAST | 12" | 18" | 24" | 1 | 6 | -2 | 2 | 5pts |
| Bolt Pistol | Pistol | 6" | 9" | 12" | 1 | 4 | 0 | 1 | 
| Bolt Rifle | Assault | 12" | 18" | 24" | 2 | 4 | 0 | 1 | 
| Hand Flamer | Ignores Cover Pistol Torrent | N/A | N/A | 12" | D6 | 3 | 0 | 1 | 5pts |
| Plasma Pistol - standard | Pistol Breaching 5+| 6" | 9" | 12" | 1 | 5 | -2 | 1 | 5pts |
| Plasma pistol - supercharge | Hazardous Pistol Breaching 4+ | 6" | 9" | 12" | 1 | 6 | -2 | 1 | 5pts |

| Melee Weapons | Abilities | IM | A | S | AP | D | Cost |
| ----- | ---- | --- | --- | --- | --- | --- | --- |
| Astartes chainsword | | 0 | 4 | 4 | -1 | 1 |
| Close combat weapon | | 0 | 2 | 4 | 0 | 1 |
| Power Fist | | -3 | 3 | 8 | -3 | 2 | 5pts |
| Power Weapon | | 0 | 3 | 5 | -2 | 1 | 5pts |
| Thunder Hammer | Cleave 2" | -2 | 3 | 7 | -3 | 2 | 5pts |

##### Wargear Options
- The Intercessor Sergeant's bolt rifle can be replaced with one of the following:
    - 1 Astartes chainsword
    - 1 Hand flamer
    - 1 Plasma pistol
    - 1 Power Weapon
- The Intercessor Sergeant's close combat weaon can be replaced with one of the following:
    - 1 Astartes chainsword
    - 1 Power Fist
    - 1 Power Weapon
    - 1 Thunder Hammer
- For Every 5 models in this unit, 1 model equipped with a bolt rifle can be equipped with 1 Astartes grenade launcher. 

##### Abilities
-Insert Faction Ability Here
-Target Elimination: Each time this unit is selected to shoot, if it remained stationary this turn, add the Sustained Fire 1 ability to bolt rifles equipped by models in this unit and you can only select one enemy unit as the target of all of this units attacks.

##### Unit Composition
- 1 Intercessor Sergeant
- 4-9 Intercessors
Every model is equipped with bolt pistol, bolt rifle, and close combat weapon.


### Weapon References WIP!!!
| Ranged Weapons | Abilites | Short Range | Medium Range | Long Range | A | S | AP | D | Cost |
| ------ | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- |
| Bolter | | 12" | 18" | 24" | 2 | 4 | 0 | 1 | 
| Grenade launcher-frag | BLAST | 12" | 18" | 24" | D3 | 4 | 0 | 1 | 5pts |
| Grenade launcher-krak | BLAST | 12" | 18" | 24" | 1 | 6 | -2 | 2 | 5pts |
| Plasma pistol - standard | Pistol Breaching 6+| 6" | 9" | 12" | 1 | 5 | -2 | 1 | 5pts |
| Plasma pistol - supercharge | Hazardous Pistol Breaching 5+ | 6" | 9" | 12" | 1 | 6 | -2 | 1 | 5pts |
| Plasma gun - standard |  Breaching 6+ Sustained Fire 1 | 12" | 18" | 24" | 1 | 5 | -2 | 1 | 5pts |
| Plasma gun - supercharge | Hazardous  Breaching 5+ Sustained Fire 1 | 12" | 18" | 24" | 1 | 6 | -2 | 1 | 5pts |
| Lascannon | Heavy(S) | 24" | 36" | 48" | 1 | 8 | -3 | 3 | 10pts |
| Meltagun | Melta 2 | 6" | 9" | 12" | 1 | 8 | -4 | 2 | 5 pts |
| Multi-melta | Melta 2 | 9" | 12" | 18" | 2 | 9 | -4 | 2 | 20pts |


Attacks depend on who is holding the weapon. IE a captain will get more attacks than an assault intercessor
| Melee Weapons | Abilities | IM | A | S | AP | D | Cost |
| ----- | ---- | --- | --- | --- | --- | --- | --- |
| Chainsword | | 0 | 2 | 4 | -1 | 1 |
| Power Fist | | -3 | 2 | 8 | -3 | 2 | 5pts |
| Chain Fist | Armourbane | -3 | 2 | 8 | -3 | 2 | 5pts |
| Power Weapon | | 0 | 2 | 5 | -2 | 1 | 5pts |
| Thunder Hammer | Cleave 2" | -2 | 2 | 7 | -3 | 2 | 5pts |

### Example Statlines
##### Rhino
| M | BS | WS | I | AC | Ld | CL | Wil | Int |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | 
| 12" | 4 | 4 | 1 | 3 | 6+ | 6+ | 6+ | 6+ |

###### Hit Table
| D6 Result | Location Hit |
| ---- | ---- |
| 1-2 | Track |
| 3-6 | Hull |

###### Armor Table
| Location | Front | Side | Rear | HP | IP |
| ---- | --- | --- | --- | --- | --- |
| Tracks | 10 | 10 | 10 | 2 | 3 |
| Hull | 12 | 11 | 10 | 3 | 4 |

##### Land Raider
| M | BS | WS | I | AC | Ld | CL | Wil | Int |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | 
| 10" | 4 | 4 | 1 | 3 | 6+ | 6+ | 6+ | 6+ |

###### Hit Table
| D6 Result | Location Hit |
| ---- | ---- |
| 1-2 | Track |
| 3-5 | Hull |
| 6 | Sponson* |

*Select the closest one to the attacker

###### Armor Table
| Location | Front | Side | Rear | HP | IP |
| ---- | --- | --- | --- | --- | --- |
| Tracks | 12 | 12 | 12 | 3 | 4 |
| Hull | 14 | 14 | 14 | 7 | 8 |
| Sponson x2 | 11 | 11 | 11 | 4 | 4 |