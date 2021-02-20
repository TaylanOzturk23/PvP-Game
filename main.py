class Game:
    def __init__(self):
        self.status = True
        self.hit = 0
        self.player_statistics = []
        self.encounter_text = (
            r"""
                    --------------------------------------
                            \\ STAGE {} //
                            ******* Hit {} *******
                            Opponnent: ︶ノ︵  {}  ︶ノ︵
                            -------------------------
                            Opponnent's Statistics:
                            Strength: {}
                            Agility: {}
                            Attack: {}
                            Defence: {} 
                            Vitality: {}
                            Stamina: {}
                            Magic: {}
                    --------------------------------------
            
            """
        )
        self.coordination = {
            "Strength": 0,
            "Agility": 1,
            "Attack": 2,
            "Defence": 3,
            "Vitality": 4,
            "Stamina": 5,
            "Magic": 6
        }
        
        with open("stage.txt", "r") as stage:
            self.stages = iter(range(int(stage.read()), 101))
            
        with open("enemy_names.json", "r") as enemy_name_datas:
            self.enemy_names = iter(list(json.load(enemy_name_datas)))
        
        with open("skill_points.json", "r") as data_base:
            self.player_skill_points = list(json.load(data_base))[0]
            data_base.seek(0)
            self.enemy_skill_point = list(json.load(data_base))[1]
        
        with open("player_skills.json", "r") as data_base:
            self.player_skill_datas = json.load(data_base)
            self.player_statistics = [
                self.player_skill_datas["Strength"], self.player_skill_datas["Agility"],
                self.player_skill_datas["Attack"], self.player_skill_datas["Defence"],
                self.player_skill_datas["Vitality"], self.player_skill_datas["Stamina"],
                self.player_skill_datas["Magic"]
            ]
            
    def distribute(self, count: int, size=7) -> list:
        N = size      
        list_ = sorted([random.randint(1, count-1) for i in range(N - 1)])
        list_.insert(0, 0)
        list_.append(count)
        result = []

        for i in range(N):
            result.append(list_[i + 1] - list_[i])

        return result
    
    
    def percent(self, percent: int) -> bool:
        return True if random.choice([i for i in range(1, 101)]) <= percent else False
    
    
    def skill_upgrade_menu(self):
        # Wanted skills that user's wanna update.
        upgraded_skills = input(
            f"""
            =================================================================================
            Choose whichever you want to upgrade and follow this syntax:
            <ability>: <upgrade value> | <ability>: <upgrade value> | ..... 
            Don't forget: Abilities can upgrade by 1 per 1 skill point. Spend them carefully
            
            Info 1: Be sensitive to spaces
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            False ----------> Strength:6
            True  ----------> Strength: 6                
            <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            You don't need to be sensitive to upper and lower case letters.
            
            Info 2: The values ​​in your entry providing information about the upgrade must be 1 digit.
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            False ----------> Strength: 10
            True  ----------> Strength: 9 | Strength: 1
            *********************************************
            False ----------> Strength: 16
            True  ----------> Strength: 9 | Strength: 7
            <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            =================================================================================
            
                    Strength: {self.player_statistics[self.coordination["Strength"]]} 
                    Agility: {self.player_statistics[self.coordination["Agility"]]}
                    Attack: {self.player_statistics[self.coordination["Attack"]]}
                    Defence: {self.player_statistics[self.coordination["Defence"]]}
                    Vitality: {self.player_statistics[self.coordination["Vitality"]]}
                    Stamina: {self.player_statistics[self.coordination["Stamina"]]}
                    Magic: {self.player_statistics[self.coordination["Magic"]]}
                        
                    Skill Points: {self.player_skill_points}
            ------------------------------------------------------------------------------
            ↓↓
            """
        )
        if not upgraded_skills.strip():
            print(
                """
                
                                **********************************
                                You Must Spend Your Skill Points
                                **********************************    
                """
            )
            self.skill_upgrade_menu()
            
        else:
            amounts = []
            for i in "".join(upgraded_skills.split("|")):
                if i.isdigit():
                    amounts.append(int(i))
            
            abilities = []
            for i in range(len("".join(("".join(upgraded_skills.split("|")).split(":"))).split()) - 1):
                if "".join(("".join(upgraded_skills.split("|")).split(":"))).split()[i].isalpha():
                    abilities.append("".join(("".join(upgraded_skills.split("|")).split(":"))).split()[i])
            
            for i in range(len(abilities)):
                try:
                    self.player_statistics[self.coordination[abilities[i].lower().capitalize()]] += amounts[i]
                except KeyError:
                    print("Please be sensitive to spaces")
                
            if sum(amounts) > self.player_skill_points:
                print(f"\n{60 * '*'}")
                print("\tOut of range skill points" + f"\n\t\t You have {self.player_skill_points} skill points but you spent {sum(amounts)}")
                print(60 * "*")
                self.skill_upgrade_menu()
            
            else:
                with open("player_skills.json", "w") as data_base:
                    datas = dict(self.player_skill_datas)
                    new_statistic = [i[0] + i[1] for i in list(zip([i for i in datas.values()], [i for i in self.player_statistics]))]
                    json.dump(dict(zip(self.coordination.keys(), new_statistic)), data_base)
                
                with open("skill_points.json", "w") as data_base:
                    self.player_skill_points -= sum(amounts)
                    json.dump(list([self.player_skill_points, self.enemy_skill_point]), data_base)
    

    def encountering(self, hit: int):
        self.player_figth_statistics = {
            "Block": self.player_statistics[self.coordination["Defence"]],
            "Accuracy": self.player_statistics[self.coordination["Attack"]],
            "Physical Damage": self.player_statistics[self.coordination["Strength"]] - self.enemy_statistics[self.coordination["Stamina"]],
            "Magical Damage": self.player_statistics[self.coordination["Magic"]] - self.enemy_statistics[self.coordination["Stamina"]], 
            "Damage Absorption": self.player_statistics[self.coordination["Stamina"]],
            "Additional Damage": self.player_statistics[self.coordination["Agility"]] * 1.5
        }
        self.enemy_figth_statistics = {
            "Block": self.enemy_statistics[self.coordination["Defence"]],
            "Accuracy": self.enemy_statistics[self.coordination["Attack"]],
            "Physical Damage": self.enemy_statistics[self.coordination["Strength"]] - self.player_statistics[self.coordination["Stamina"]],
            "Magical Damage": self.enemy_statistics[self.coordination["Magic"]] - self.player_statistics[self.coordination["Stamina"]], 
            "Damage Absorption": self.enemy_statistics[self.coordination["Stamina"]],
            "Additional Damage": self.enemy_statistics[self.coordination["Agility"]] * 1.5
        }
        
        print(self.encounter_text.format(self.stage, hit, self.enemy_name, *[i for i in list(self.enemy_statistics)]))
                
        # Attacking Styles
        player_attack_menu = (
            """
                            *********************
                            * YOU ARE ATTACKING!*
                            *********************
                            
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            Tip:
             Critical: 
              The chances of an accurate shot are too low. 
              But it makes your damage 6 times more effective
              
             Power: 
              The chances of an accurate shot are low. 
              But its damage is 3 times more effective.
              
             Quick:
              The chances of an accurate shot are too high. 
              But its damage is common.
            
            Tip:
             Magical damages are more effective than physical damages. 
             But its accuracy is lower.
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            =====================================================================================
            Choose a hit style by dialing their numbers:
            
            Critical:                     Powerful:                     Quick:
                [10] Critical (Physical)     [20] Powerful (Physical)     [30] Quick (Physical)        
                [11] Critical (Magical)      [21] Powerful (Magical)      [31] Quick (Magical)
            =====================================================================================
            ----------------------------------------------------------------------------
            ↓↓
            """
        )
        time.sleep(4)
        player_hit_style = input(player_attack_menu)
        self.figth_result_text = (
            """
            
                            ===============================
                            *****************************
                            {} Dealt {} {} Damage !
                            *****************************
                            Player's Health Has Left {}
                            *****************************
                            Enemy's Health Has Left {}
                            *****************************
                            ===============================
            """
        )
        blocked_hit_text = (
            """
                          *********************************
                          {}
                          *********************************
            """
        )
        self.player_physical_damage = abs(self.enemy_figth_statistics["Damage Absorption"] - self.player_figth_statistics["Physical Damage"] + (self.player_figth_statistics["Additional Damage"] if self.percent(25) else False))
        self.player_magical_damage = abs(self.enemy_figth_statistics["Damage Absorption"] - self.player_figth_statistics["Magical Damage"]) * 2 + (self.enemy_figth_statistics["Additional Damage"] if self.percent(25) else False)
        
          
        if player_hit_style == "10":
            if self.percent(5 + self.player_figth_statistics["Accuracy"] - self.enemy_figth_statistics["Block"]):
                self.enemy_health -= self.player_physical_damage * 6
                print(self.figth_result_text.format("You", self.player_physical_damage * 6, "Physical", self.player_health, self.enemy_health))
            
            else:
                print(blocked_hit_text.format("Your Opponnent Blocked Your Hit !"))
                
        elif player_hit_style == "11":
            if self.percent(5 + self.player_figth_statistics["Accuracy"]-35 - self.enemy_figth_statistics["Block"]):
                self.enemy_health -= self.player_magical_damage * 6
                print(self.figth_result_text.format("You", self.player_magical_damage * 6, "Magical", self.player_health, self.enemy_health))
        
            else:
                print(blocked_hit_text.format("Your Opponnent Blocked Your Hit !"))
                
        elif player_hit_style == "20":
            if self.percent(10 + self.player_figth_statistics["Accuracy"] - self.enemy_figth_statistics["Block"]):
                self.enemy_health -= self.player_physical_damage * 3
                print(self.figth_result_text.format("You", self.player_physical_damage * 3, "Physical", self.player_health, self.enemy_health))
    
            else:
                print(blocked_hit_text.format("Your Opponnent Blocked Your Hit !"))
                
        elif player_hit_style == "21":
            if self.percent(10 + self.player_figth_statistics["Accuracy"]-35 - self.enemy_figth_statistics["Block"]):
                self.enemy_health -= self.player_magical_damage * 3
                print(self.figth_result_text.format("You", self.player_magical_damage * 3, "Magical", self.player_health, self.enemy_health))
            else:
                print(blocked_hit_text.format("Your Opponnent Blocked Your Hit !"))
                
        elif player_hit_style == "30":
            if self.percent(65 + self.player_figth_statistics["Accuracy"] - self.enemy_figth_statistics["Block"]):
                self.enemy_health -= self.player_physical_damage
                print(self.figth_result_text.format("You", self.player_physical_damage, "Physical", self.player_health, self.enemy_health))
            else:
                print(blocked_hit_text.format("Your Opponnent Blocked Your Hit !"))
                
        elif player_hit_style == "31":
            if self.percent(65 + self.player_figth_statistics["Accuracy"]-35 - self.enemy_figth_statistics["Block"]):
                self.enemy_health -= self.player_magical_damage
                print(self.figth_result_text.format("You", self.player_magical_damage, "Magical", self.player_health, self.enemy_health))
            else:
                print(blocked_hit_text.format("Your Opponnent Blocked Your Hit !"))
                
        else:
            print("Please dial a number displayed in menu")
        
    
        print(
            """
                            ***********************
                            * ENEMY IS ATTACKING! *
                            ***********************
            """
        )
        
        time.sleep(1)
        for i in range(6):
            print("🕒" * i)
            time.sleep(0.6) 
            
        styles = [
            1 * [["Critical Physical", "Critical Physical", "Critical Magical"]], # 10% Chance
            3 * [["Powerful Physical", "Powerful Physical", "Powerful Magical"]], # 30% Chance 
            6 * [["Quickly Physical", "Quickly Physical", "Quickly Magical"]] # 60% Chance
        ]
        self.enemy_hit_style = random.choice(random.choice(random.choice(styles)))
        
        self.enemy_physical_damage = abs(self.player_figth_statistics["Damage Absorption"] - self.enemy_figth_statistics["Physical Damage"] + (self.enemy_figth_statistics["Additional Damage"] if self.percent(25) else False))
        self.enemy_magical_damage = abs(self.player_figth_statistics["Damage Absorption"] - self.enemy_figth_statistics["Magical Damage"] * 2 + (self.enemy_figth_statistics["Additional Damage"] if self.percent(25) else False))
        
        if self.enemy_hit_style == "Critical Physical":
            if self.percent(5 + self.enemy_figth_statistics["Accuracy"] - self.player_figth_statistics["Block"]):
                self.player_health -= self.enemy_physical_damage * 6
                print(self.figth_result_text.format("Enemy", self.enemy_physical_damage * 6, "Physical", self.player_health, self.enemy_health))
                
            else:
                print(blocked_hit_text.format("You Blocked your Opponnent's Hit"))
            
        elif self.enemy_hit_style == "Critical Magical":
            if self.percent(5 + self.enemy_figth_statistics["Accuracy"]-35 - self.player_figth_statistics["Block"]):
                self.player_health -= self.enemy_magical_damage * 6
                print(self.figth_result_text.format("Enemy", self.enemy_magical_damage * 6, "Magical", self.player_health, self.enemy_health))
                
            else:
                print(blocked_hit_text.format("You Blocked your Opponnent's Hit"))
            
        elif self.enemy_hit_style == "Powerful Physical":
            if self.percent(10 + self.enemy_figth_statistics["Accuracy"] - self.player_figth_statistics["Block"]):
                self.player_health -= self.enemy_physical_damage * 3
                print(self.figth_result_text.format("Enemy", self.enemy_physical_damage * 3, "Physical", self.player_health, self.enemy_health))
                
            else:
                print(blocked_hit_text.format("You Blocked your Opponnent's Hit"))
            
        elif self.enemy_hit_style == "Powerful Magical":
            if self.percent(10 + self.enemy_figth_statistics["Accuracy"]-35 - self.player_figth_statistics["Block"]):
                self.player_health -= self.enemy_magical_damage * 3
                print(self.figth_result_text.format("Enemy", self.enemy_magical_damage * 3, "Magical", self.player_health, self.enemy_health))
                
            else:
                print(blocked_hit_text.format("You Blocked your Opponnent's Hit"))
            
        elif self.enemy_hit_style == "Quickly Physical":
            if self.percent(65 + self.enemy_figth_statistics["Accuracy"] - self.player_figth_statistics["Block"]):
                self.player_health -= self.enemy_physical_damage
                print(self.figth_result_text.format("Enemy", self.enemy_physical_damage, "Physical", self.player_health, self.enemy_health))
                
            else:
                print(blocked_hit_text.format("You Blocked your Opponnent's Hit"))
            
        elif self.enemy_hit_style == "Quickly Magical":
            if self.percent(65 + self.enemy_figth_statistics["Accuracy"]-35 - self.player_figth_statistics["Block"]):
                self.player_health -= self.enemy_magical_damage
                print(self.figth_result_text.format("Enemy", self.enemy_magical_damage, "Magical", self.player_health, self.enemy_health))
                
            else:
                print(blocked_hit_text.format("You Blocked your Opponnent's Hit"))
                
            
    def play(self):
        # define stage
        try:
            self.stage = next(self.stages)
        except StopIteration:
            print("GAME OVER")
            self.status = False
        
        # define enemy names
        self.enemy_name = next(self.enemy_names)
        
        # increase enemy skill points according to stages.
        if self.stage % 2 != 0 and self.stage % 5 == 0:
            self.enemy_skill_point += 5
             
        elif self.stage % 10 == 0:
            self.enemy_skill_point += 10
            
        else:
            self.enemy_skill_point += 1
        
        # enemy statistics
        if self.stage == 1:
            self.enemy_statistics = self.distribute(self.enemy_skill_point)
        
        else:
            self.enemy_statistics = self.distribute(self.enemy_skill_point)

        # saving amounts to files.
        with open("enemy_skills.json", "w") as data_base:
            json.dump(self.enemy_statistics, data_base)
        
        with open("skill_points.json", "w") as data_base:
            json.dump(list([self.player_skill_points, self.enemy_skill_point]), data_base)
        
        with open("stage.txt", "w") as data_base:
            print(str(self.stage), file=data_base, flush=True)
        
        # Customizing First Stage
        if self.stage == 1:
            print(
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
                     there is a 25% Chance that you can add this damage next to your normal damage.
                
                 Defancive:
                    Stamina: It decreases your opponnent's damage
                
                 Accuracy:
                    Attack: It increases your succesful attack chance. So your accuracy depends on this skill
                    Defence: It increases your block chance.
                    
                 Health:
                    Vitality: Its value is multiplied by three and added to your health. 
                
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
            )
            self.skill_upgrade_menu()
        
        # Healths
        self.player_health = 30 + self.player_statistics[self.coordination["Vitality"]] * 3
        self.enemy_health = 30 + self.enemy_statistics[self.coordination["Vitality"]] * 3
        
        # Hit
        self.hit = 0
        
        # Loop of every stage.
        if self.stage in [i for i in range(1, 100+1)]:
            while True:
                if not self.player_health > 0:
                    print(
                        """
                                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                                You Have Been Slained
                                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        """
                    )
                    exit()
                
                elif not self.enemy_health > 0:
                    break
            
                else:
                    self.hit += 1
                    self.encountering(self.hit)
                    
                
            self.player_skill_points += 1
            with open("skill_points.json", "w") as data_base:
                json.dump(list([self.player_skill_points, self.enemy_skill_point]), data_base)

            print(
                """
                            ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
                                You have successfully completed the episode
                                after your opponent's last hit before he died!
                            ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
                """
            )
            self.skill_upgrade_menu()
            
        else:
            print("YOU HAVE FINISHED THE GAME !")
            
    
if __name__ == '__main__':
    import json
    import random
    import time
    
    game = Game()
    while game.status:
        game.play()
