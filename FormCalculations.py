def teamFormScore(formDict):
    if formDict["Games Played"] == 0:
        FS1 = 0
    else:
        FS1 = (formDict["Games Played"] - formDict["Losses"] - 0.5*formDict["Draws"])/formDict["Games Played"]

    if formDict["Goals Made"] == 0 and formDict["Goals Conceded"] == 0:
        FS2 = 0
    else:
        FS2 = (formDict["Goals Made"] - formDict["Goals Conceded"])/(formDict["Goals Made"] + formDict["Goals Conceded"])

    TFS = 100*((FS1 + FS2)/2)
    return TFS

def playerScore(statDict,position):

    if position == "Forward": 
        # General stats
            Appearances = statDict["Appearances"]
            Goals = statDict["Goals"]
            Wins = statDict["Wins"]
            Losses = statDict["Losses"]

        # Attack stats
            Goals_per_match = statDict["Goals per match"]
            Headed_goals = statDict["Headed goals"]
            Goals_with_right_foot = statDict["Goals with right foot"]
            Goals_with_left_foot = statDict["Goals with left foot"]
            Penalties_scored = statDict["Penalties scored"]
            Freekicks_scored = statDict["Freekicks scored"]
            Shots = statDict["Shots"]
            Shots_on_target = statDict["Shots on target"]
            Shooting_accuracy = statDict["Shooting accuracy %"]/100
            Hit_woodwork = statDict["Hit woodwork"]
            Big_chances_missed = statDict["Big chances missed"]
        
        # Team Play stats    
            Assists = statDict["Assists"]
            Passes = statDict["Passes"]
            Passes_per_match = statDict["Passes per match"]
            Big_Chances_Created = statDict["Big Chances Created"]
            Crosses = statDict["Crosses"]

        # Disipline stats
            Yellow_cards = statDict["Yellow cards"]
            Red_cards = statDict["Red cards"]
            Fouls = statDict["Fouls"]
            Offsides = statDict["Offsides"]

        # Defence stats
            Tackles = statDict["Tackles"]
            Blocked_shots = statDict["Blocked shots"]
            Interceptions = statDict["Interceptions"]
            Clearances = statDict["Clearances"]
            Headed_Clearance = statDict["Headed Clearance"]

            scoreAttack = 0
            scoreTeamPlay = 0
            scoreDiscipline = 0
            scoreDefense = 0
            score = 100*((scoreAttack + scoreTeamPlay + scoreDiscipline + scoreDefense)/4)
    elif position == "Defender":
        # General stats
            Appearances = statDict["Appearances"]
            Goals = statDict["Goals"]
            Wins = statDict["Wins"]
            Losses = statDict["Losses"]
            
        # Attack stats
            Headed_goals = statDict["Headed goals"]
            Goals_with_right_foot = statDict["Goals with right foot"]
            Goals_with_left_foot = statDict["Goals with left foot"]
            Hit_woodwork = statDict["Hit woodwork"]
        
        # Team Play stats    
            Assists = statDict["Assists"]
            Passes = statDict["Passes"]
            Passes_per_match = statDict["Passes per match"]
            Big_Chances_Created = statDict["Big Chances Created"]
            Crosses = statDict["Crosses"]
            Cross_accuracy = statDict["Cross accuracy %"]/100
            Through_balls = statDict["Through balls"]
            Accurate_long_balls = statDict["Accurate long balls"]

        # Disipline stats
            Yellow_cards = statDict["Yellow cards"]
            Red_cards = statDict["Red cards"]
            Fouls = statDict["Fouls"]
            Offsides = statDict["Offsides"]

        # Defence stats
            Clean_sheets = statDict["Clean sheets"]
            Goals_Conceded = statDict["Goals Conceded"]
            Tackles = statDict["Tackles"]
            Tackle_success= statDict["Tackle success %"]/100
            Last_man_tackles = statDict["Last man tackles"]
            Blocked_shots = statDict["Blocked shots"]
            Interceptions = statDict["Interceptions"]
            Clearances = statDict["Clearances"]
            Headed_Clearance = statDict["Headed Clearance"]
            Clearances_off_line = statDict["Clearances off line"]
            Recoveries = statDict["Recoveries"]
            Duels_won = statDict["Duels won"]
            Duels_lost = statDict["Duels lost"]
            Successful_50_50s = statDict["Successful 50/50s"]
            Aerial_battles_won = statDict["Aerial battles won"]
            Aerial_battles_lost = statDict["Aerial battles lost"]
            Own_goals = statDict["Own goals"]
            Errors_leading_to_goal = statDict["Errors leading to goal"]


            scoreAttack = 0
            scoreTeamPlay = 0
            scoreDiscipline = 0
            scoreDefense = 0
            score = 0
    elif position == "Midfielder":
        # General stats
            Appearances = statDict["Appearances"]
            Goals = statDict["Goals"]
            Wins = statDict["Wins"]
            Losses = statDict["Losses"]

        # Attack stats
            Goals_per_match = statDict["Goals per match"]
            Headed_goals = statDict["Headed goals"]
            Goals_with_right_foot = statDict["Goals with right foot"]
            Goals_with_left_foot = statDict["Goals with left foot"]
            Penalties_scored = statDict["Penalties scored"]
            Freekicks_scored = statDict["Freekicks scored"]
            Shots = statDict["Shots"]
            Shots_on_target = statDict["Shots on target"]
            Shooting_accuracy = statDict["Shooting accuracy %"]/100
            Hit_woodwork = statDict["Hit woodwork"]
            Big_chances_missed = statDict["Big chances missed"]
        
        # Team Play stats    
            Assists = statDict["Assists"]
            Passes = statDict["Passes"]
            Passes_per_match = statDict["Passes per match"]
            Big_Chances_Created = statDict["Big Chances Created"]
            Crosses = statDict["Crosses"]
            Cross_accuracy = statDict["Cross accuracy %"]/100
            Through_balls = statDict["Through balls"]
            Accurate_long_balls = statDict["Accurate long balls"]

        # Disipline stats
            Yellow_cards = statDict["Yellow cards"]
            Red_cards = statDict["Red cards"]
            Fouls = statDict["Fouls"]
            Offsides = statDict["Offsides"]

        # Defence stats
            Tackles = statDict["Tackles"]
            Tackle_success= statDict["Tackle success %"]/100
            Blocked_shots = statDict["Blocked shots"]
            Interceptions = statDict["Interceptions"]
            Clearances = statDict["Clearances"]
            Headed_Clearance = statDict["Headed Clearance"]
            Recoveries = statDict["Recoveries"]
            Duels_won = statDict["Duels won"]
            Duels_lost = statDict["Duels lost"]
            Successful_50_50s = statDict["Successful 50/50s"]
            Aerial_battles_won = statDict["Aerial battles won"]
            Aerial_battles_lost = statDict["Aerial battles lost"]
            Errors_leading_to_goal = statDict["Errors leading to goal"]

        
            scoreAttack = 0
            scoreTeamPlay = 0
            scoreDiscipline = 0
            scoreDefense = 0
            score = 0
    elif position == "Goalkeeper":
        # General stats
            Appearances = statDict["Appearances"]
            Clean_sheets = statDict["Clean sheets"]
            Wins = statDict["Wins"]
            Losses = statDict["Losses"]

        # Goalkeeper stats
            Saves = statDict["Saves"]
            Penalties_Saved = statDict["Penalties Saved"]
            Punches = statDict["Punches"]
            High_Claims = statDict["High Claims"]
            Catches = statDict["Catches"]
            Sweeper_clearances = statDict["Sweeper clearances"]
            Throw_outs = statDict["Throw outs"]
            Goal_Kicks = statDict["Goal Kicks"]

        # Team Play stats    
            Goals = statDict["Goals"]
            Assists = statDict["Assists"]
            Passes = statDict["Passes"]
            Passes_per_match = statDict["Passes per match"]
            Accurate_long_balls = statDict["Accurate long balls"]

        # Disipline stats
            Yellow_cards = statDict["Yellow cards"]
            Red_cards = statDict["Red cards"]
            Fouls = statDict["Fouls"]

        # Defence stats
            Goals_Conceded = statDict["Goals Conceded"]
            Errors_leading_to_goal = statDict["Errors leading to goal"]
            Own_goals = statDict["Own goals"]

            scoreAttack = 0
            scoreTeamPlay = 0
            scoreDiscipline = 0
            scoreDefense = 0
            score = 0
    else:
            score = 0
    
    return score