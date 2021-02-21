# PvP-Game
#### A game like "Swords and Sandals II" with python and played in terminal.

# Info about game shortly 
#### This text is excerpted from the game. So the same text is also available in the game.

                """
                -------------------------------------------------------------------------------
                Welcome to the Game ! 
                This is a PvP game played in terminal and it also like "Swords and Sandals II". 
                Your target is reaching to the last stage and beating the last boss. 
            
                --> Categories of brawler statistics:
                
                 Offensive:
                    Strength: It increases your Physical Damage. Your Physical Damage depends on this skill
                    Magic: It increases your Magical Damage. Your Magical Damage depends on this skill
                    Agility: Its value is multiplied by 1.5 and
                     there is a 30% Chance that you can add this damage next to your normal damage.
                
                 Defancive:
                    Stamina: It decreases your opponnent's damage
                
                 Accuracy:
                    Attack: It increases your succesful attack chance. So your accuracy depends on this skill
                    Defence: It increases your block chance.
                    
                 Health:
                    Vitality: Its value is multiplied by three (ten if stage is more than 20) and added to your health. 
                
                --> WARNING:
                 Everything is saved when you exit the program.
                 But be careful when you are quitting. 
                 You must exit the game when you are moving to a new stage. 
                 Otherwise, your skills may not be recorded.
                 
                --> The Logic of the game:
                 There are 100 stages in this game and you are tryna reach till to the last stage.
                 You fight with an enemy in every stages. You must kill them to transitioning to a next stage.
                 Everyone has some skills to beat each other. 
                 So, you have skills too. You and other enemies are  needing skill points to upgrade a skill.
                 You must transition to a next stage to get more skill points.
                 There are some bosses in this game.
                 Masters (M) and Grandmasters (GM). GMs are more powerful.
                 
                 Masters are coming in these stages :
                 print(list(filter(lambda x: True if x % 5 == 0 and not x % 2 == 0 else False, range(1, 100+1))))
                 
                 Grandmasters are coming in these stages:
                 print(list(filter(lambda x: False if x % 10 else True, range(1, 100+1))))
                 
                 And here are some attack styles. Magical and physical attack styles.
                 Magical attacks are more effective than physical attacks. 
                 But magical attack's accuracy is lower.
                 
                 
                 --> TIP:   
                 It is recommended to upgrade physical damage in the early stages, 
                 and it is recommended to use one of the attack styles, the "quick" style. 
                 Because the magic damage in the early stages is unlikely to be accurate.
                 Likewise, "powerful" and "critical" attack styles are unlikely to be accurate.
                 So it is recommended to be prone to physical damage in the early stages and 
                 to use the "quick" style heavily.
                ------------------------------------------------------------------------------
                """

# Setup
Just clone this repository and insert them to a same directory.
It is important which directory are these files having in. All of them should stay in a same directory.
After inserting these files to a same directory, just run main.py and have fun !


# Preview and informative video
[![Watch the video](data:image/jpeg;base64,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)](https://youtu.be/4ShLU_Ner08)

