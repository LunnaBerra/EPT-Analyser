def teamFormScore(formDict):
    FS1 = (formDict["Games Played"] - formDict["Losses"] - 0.5*formDict["Draws"])/formDict["Games Played"]
    FS2 = (formDict["Goals Made"] - formDict["Goals Conceded"])/(formDict["Goals Made"] + formDict["Goals Conceded"])
    TFS = 100*(FS1 + FS2)
    return TFS

def playerScore(statDict,position):

    if position == "Forward": 
        # Attack stats
            Appearances = statDict["Appearances"]
            Goals = statDict["Goals"]
            Wins = statDict["Wins"]
            Losses = statDict["Losses"]
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
            Yellow_cards = statDict["Yellow Cards"]
            Red_cards = statDict["Red Cards"]
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
            score = 0
    elif position == "Defender":
            #TODO perfect scoring
            scoreAttack = 0
            scoreTeamPlay = 0
            scoreDiscipline = 0
            scoreDefense = 0
            score = 0
    elif position == "Midfielder":
            scoreAttack = 0
            scoreTeamPlay = 0
            scoreDiscipline = 0
            scoreDefense = 0
            score = 0
    elif position == "Goalkeeper":
            scoreAttack = 0
            scoreTeamPlay = 0
            scoreDiscipline = 0
            scoreDefense = 0
            score = 0
    else:
            score = 0
    
    return score