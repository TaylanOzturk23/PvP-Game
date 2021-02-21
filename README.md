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
[![Watch the video]()](https://youtu.be/T-D1KVIuvjA)

