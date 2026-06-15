---
title: Activation Phase
description: A overview of the activation phase
---

## Overview
Starting with the player with priority, each player will take turns activating units one at a time until every unit has activated. 

If one player has greater than or equal to double the amount of unactivated units, they must activate 2 units at a time. If one player has greater than or equal to triple the amount of unactivated units, they must activate 3 units at a time, etc. 

### Examples
| Move Number | Player A Units Remaining | Player B Units Remaining | Player A Activates | Player B Activates |
| ------ | ------ | ------ | ------ |  ------ |
| 1 | 10 | 15 | 1 | 1 |
| 2 | 9 | 14 | 1 | 1 |
| 3 | 8 | 13 | 1 | 1 | 
| 4 | 7 | 12 | 1 | 1 |
| 5 | 6 | 11 | 1 | 1 |
| 6 | 5 | 10 | 1 | 2 |
| 7 | 4 | 8 | 1 | 2 |
| 8 | 3 | 6 | 1 | 2 |
| 9 | 2 | 4 | 1 | 2 |
| 10 | 1 | 2 | 1 | 2 |


| Move Number | Player A Units Remaining | Player B Units Remaining | Player A Activates | Player B Activates |
| ------ | ------ | ------ | ------ |  ------ |
| 1 | 5 | 14 | 1 | 2 |
| 2 | 4 | 12 | 1 | 3 |
| 3 | 3 | 9 | 1 | 3 |
| 4 | 2 | 6 | 1 | 3 |
| 5 | 1 | 3 | 1 | 3 |

### Actions
Each unit can attempt each of the below actions once per turn, so long as it has enough activations left to complete each action. Each action has an associated AC, and each unit starts the phase with activations equal to that units AC characteristic. 

### Move (AC:1): 
The unit can move up to its movement characteristic with and can rotate for free during any part of the move, with the exception of non WALKER VEHICLE units which can only rotate up to 90 degrees if moving more than half their movement. You cannot enter, leave, or end the move engagement range as a part of this move. Vehicles can enter and leave engagement range but cannot end in engagement range. A unit can only move so long as it has not made a Run or Fallback action in the same turn. 

### Run (AC:2): 
The unit can move up to 1.5x your movement characteristic rounding up, with the same restrictions as the Move Action. A unit can only run so long as it has not made a Move or Fallback action in the same turn. Until the end of turn, this unit is has a -1 to hit modifier when making ranged attacks and cannot fire any weapons with the HEAVY ability, or perform the Charge action. 

### Fallback (AC:2):
The unit can move up to its movement charactersitic with the same restrictions as the Move Action, but it can leave/enter Engagement Range so long as it doesn't end that move in Engagement Range. Until the end of the turn, this unit is battleshocked and any ranged attacks it makes hit on an umodifiable 6+, and is unable to perform a Charge action. 

### Take Aim (AC:1):
Until the end of the turn, add 1 to this units Ballistic Skill.

### Overwatch (AC:2):
The unit can rotate, after which it has considered to have entered Overwatch until the end of the turn or until until the unit moves for any reason. While the unit is in Overwatch, when a unit starts or ends a move within 24 inches of this unit, you may interrupt them and shoot at -1 BS and cannot have any positive BS or hit roll modifiers. 

### Charge (AC:1):
You may move up to your initiative characteristic + d6 inches to a maximum of 12 inches. You must end this move in engagement range, and there is no limit on rotations. You can immediatly perform a free fight action, and until the end of the turn add one to the attacks characteristic of melee weapons equipped by this unit. 

### Shoot (AC:1):
The unit may shoot its ranged weapons. See [Shooting](/0thEdition/core/shooting/).

### Fight (AC:1):
The unit may fight in melee with its melee weapons
See [Fighting](/0thEdition/core/fighting/).
If in melee combat with a Vehicle, see [Vehicle](/0thEdition/core/vehicle/).

### Go To Ground (AC:1):
Until the unit moves for any reason, it has a 6+ cover save.

### Manifest Psychic Power(AC:1):
Select one psychic power the bearer knows or Smite. The bearer must roll 2d6, subtracting the difficulty rating of power from the roll. If the result is greater than or equal to the units Willpower characteristic the test is passed and the psychic power takes immediate affect. If it is failed, the power has no effect and the action is wasted. Each psychic power may only be manifested once per turn, and every time a PSYKER manifests a psychic power, subtract 1 from future psychic power tests until the end of turn for each power this PSYKER has manifested. 

However, psychic powers are not without risk, as if doubles are rolled during the test the unit suffers perils of the warp, and suffers D3 mortal wounds. Suffering perils does not stop the power from taking effect if the test is successful. 

#### Deny the Witch
If there are any enemy PSYKER models within 12" of a PSYKER as it attempts to manifest a psychic power, they may attempt to deny the witch so long as they do not exceed the maximum amount of deny the witch attempts listed on the enemy PSYKER's datasheet. To deny the witch, roll 2d6, if result is greater than or equal to the enemy psykers Willpower characteristic and the unmodified roll is greater than the unmodified roll used to manifest the power, then the psychic power has been nullified and fails to take effect. 

#### Smite - Difficulty 0
This psychic power can be can be manifested multiple times a turn, so long as it is not being manifested by the same unit. Each time this psychic power is manifested, increase its difficulty rating by 1 for that player until the end of turn. Select 1 unit within 12" of this psyker, if this power is successful it suffers d3 mortal wounds. If an umodified roll of 11+ it suffers d6 mortal wounds. 


### Secure Objective (AC:1):
If this unit has the BATTELINE keyword and is within range of an objective you control, that objective remains under your control, even if you have no models within range of it, until your opponent controls it at the start or end of any turn.  

### Disembark (AC:1): 
Can only be done by transport models. Set up any models embarked within the transport wholly with 3" of the transport and not within engagement range of enemy models. Cannot be done after a run action. If done after a move action the disembarked models cannot charge. 

### Embark (AC:1):
Select a valid unit wholly within 3 inches of the transport and not within engagement range of enemy models. The unit must be able to fit inside the transport. If sucessfull remove the unit from the board and it is considered to be embarked inside the transport. 

### Deep Strike (AC:1):
This action may only be performed by units off the board with the DEEP STRIKE ability. Set this unit up more than 9 inches away from any enemy models. This unit can no make a Move, Run, or Fallback action until the end of turn. This action cannot be done turn 1. 

### Strategic Reserves (AC:1):
This action may only be performed by units off the board. Set this unit up more than 9 inches away from any enemy models and within 6 inches of a board edge. This unit can no make a Move, Run, or Fallback action until the end of turn. This action cannot be done turn 1, and you cannot set up any units within the opponents deployment zone until turn 3. 