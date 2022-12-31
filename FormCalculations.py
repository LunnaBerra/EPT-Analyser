def teamFormScore(formDict):
    if formDict["Games Played"] == 0:
        FS1 = 0
    else:
        FS1 = (formDict["Games Played"] - formDict["Losses"] -
               0.5*formDict["Draws"])/formDict["Games Played"]

    if formDict["Goals Made"] == 0 and formDict["Goals Conceded"] == 0:
        FS2 = 0
    else:
        FS2 = (formDict["Goals Made"] - formDict["Goals Conceded"]) / (formDict["Goals Made"] + formDict["Goals Conceded"])

    TFS = 100*((FS1 + FS2)/2)
    return TFS


def playerScore(statDict, position):

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

        if Appearances == 0:
            Appearances = 10 ^ 7
        if Crosses == 0:
            Crosses = 10 ^ 7
        if Shots == 0:
            Shots = 10 ^ 7
        if Passes == 0 and Crosses == 0:
            Passes = 10 ^ 7
        if Fouls == 0:
            Fouls = 10 ^ 7
        if Tackles == 0:
            Tackles = 10 ^ 7

        scoreGeneral = (1*Wins/Appearances + 0.5 *
                        (Appearances-Wins-Losses)/Appearances)/1.5
        scoreAttack = (1*Goals/Shots + 1*Shooting_accuracy -
                       1*Big_chances_missed/Shots)/3
        scoreTeamPlay = (0.5*Assists/(Crosses) +
                         2*Big_Chances_Created/(Passes+Crosses))/2.5
        scoreDiscipline = (0.5*Yellow_cards/Fouls + 3 *
                           Red_cards/Fouls)/3.5
        scoreDefense = (0.5*Blocked_shots/Tackles + 1*Interceptions/Tackles)/1.5
        score = ((2*scoreGeneral + 1.5*scoreAttack +
                  1*scoreTeamPlay - 0.75*scoreDiscipline + 0.75*scoreDefense)/4.5)
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
        Tackle_success = statDict["Tackle success %"]/100
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

        if Appearances == 0:
            Appearances = 10 ^ 7
        if Crosses == 0:
            Crosses = 10 ^ 7
        if Through_balls == 0:
            Through_balls = 10 ^ 7
        if Accurate_long_balls == 0:
            Accurate_long_balls = 10 ^ 7
        if Fouls == 0:
            Fouls = 10 ^ 7
        if Duels_won == 0 and Duels_lost == 0:
            Duels_lost = 10 ^ 7
        if Aerial_battles_won == 0 and Aerial_battles_lost == 0:
            Aerial_battles_lost = 10 ^ 7
        if Tackles == 0:
            Tackles = 10 ^ 7

        scoreGeneral = (1*Wins/Appearances + 0.5 *
                        (Appearances-Wins-Losses)/Appearances)/1.5
        scoreAttack = (1*Goals/Appearances)/1
        scoreTeamPlay = (1*Assists/Crosses + 1.75*Assists/Through_balls + 1*Cross_accuracy +
                         1.5*Big_Chances_Created/Through_balls + 1.5*Big_Chances_Created/Accurate_long_balls)/6.75
        scoreDiscipline = (0.5*Yellow_cards/Fouls + 3 *
                           Red_cards/Fouls)/3.5
        scoreDefense = (2*Clean_sheets/Appearances + 1.5*Tackle_success + 1.25*Duels_won/(Duels_won+Duels_lost) + 1.25 *
                        Aerial_battles_won/(Aerial_battles_won+Aerial_battles_lost) + 1*Blocked_shots/Tackles + 1.5*Interceptions/Tackles)/8.5
        score = ((2*scoreGeneral + 0.75*scoreAttack + 1*scoreTeamPlay -
                 1*scoreDiscipline + 2*scoreDefense)/4.75)
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
        Tackle_success = statDict["Tackle success %"]/100
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

        if Appearances == 0:
            Appearances = 10 ^ 7
        if Shots == 0:
            Shots = 10 ^ 7
        if Crosses == 0:
            Crosses = 10 ^ 7
        if Through_balls == 0:
            Through_balls = 10 ^ 7
        if Accurate_long_balls == 0:
            Accurate_long_balls = 10 ^ 7
        if Through_balls == 0:
            Through_balls = 10 ^ 7
        if Fouls == 0:
            Fouls = 10 ^ 7
        if Duels_won == 0 and Duels_lost == 0:
            Duels_lost = 10 ^ 7
        if Aerial_battles_won == 0 and Aerial_battles_lost == 0:
            Aerial_battles_lost = 10 ^ 7
        if Tackles == 0:
            Tackles = 10 ^ 7

        scoreGeneral = (1*Wins/Appearances + 0.5 *
                        (Appearances-Wins-Losses)/Appearances)/1.5
        scoreAttack = (1*Goals/Shots + 1*Shooting_accuracy -
                       1*Big_chances_missed/Shots)/3
        scoreTeamPlay = (1*Assists/Crosses + 1*Assists/Through_balls + 1*Assists/Accurate_long_balls +
                         1*Cross_accuracy + 1*Big_Chances_Created/Through_balls + 1*Big_Chances_Created/Accurate_long_balls)/6
        scoreDiscipline = (1*Yellow_cards/Fouls + 1 *
                           Red_cards/Fouls + 1*Offsides/Fouls)/3
        scoreDefense = (1*Tackle_success + 1*Duels_won/(Duels_won+Duels_lost) + 1 *
                        Aerial_battles_won/(Aerial_battles_won+Aerial_battles_lost) + 1*Blocked_shots/Tackles + 1*Interceptions/Tackles)/5
        score = ((scoreGeneral + scoreAttack +
                  scoreTeamPlay - scoreDiscipline + scoreDefense)/5)
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

        if Appearances == 0:
            Appearances = 10 ^ 7
        if Saves == 0:
            Saves = 10 ^ 7
        if Accurate_long_balls == 0:
            Accurate_long_balls = 10 ^ 7
        if Passes == 0:
            Passes = 10 ^ 7
        if Fouls == 0:
            Fouls = 10 ^ 7
        if Saves == 0:
            Saves = 10 ^ 7
        if Goals_Conceded == 0:
            Goals_Conceded = 10 ^ 7
        scoreGeneral = (1*Wins/Appearances + 0.5 *
                        (Appearances-Wins-Losses)/Appearances)/1.5
        scoreGoalkeeper = (1*Clean_sheets/Appearances + 1*(Penalties_Saved +
                           Punches + High_Claims + Catches + Sweeper_clearances)/Saves)/5
        scoreTeamPlay = (1*Goals/Appearances + 1*Assists /
                         Accurate_long_balls + 1*Accurate_long_balls/Passes)/3
        scoreDiscipline = (1*Yellow_cards/Fouls + 1 *
                           Red_cards/Fouls)/2
        scoreDefense = (1*Goals_Conceded/Saves - 1*Errors_leading_to_goal /
                        Goals_Conceded - 1*Own_goals/Goals_Conceded)/3
        score = ((scoreGeneral + scoreGoalkeeper +
                  scoreTeamPlay - scoreDiscipline + scoreDefense)/5)
    else:
        score = 0

    return score


def teamScore(statDict):

    for k, v in statDict.items():
            statDict[k] = float(v)
    
    # General stats
    Matches_played = statDict["Matches played"]
    Wins = statDict["Wins"]
    Losses = statDict["Losses"]
    Goals = statDict["Goals"]
    Goals_Conceded = statDict["Goals Conceded"]
    Clean_sheets = statDict["Clean sheets"]

    # Attack stats
    Goals_per_match = statDict["Goals per match"]
    Shots = statDict["Shots"]
    Shots_on_target = statDict["Shots on target"]
    Shooting_accuracy = statDict["Shooting accuracy %"]/100
    Penalties_scored = statDict["Penalties scored"]
    Big_Chances_Created = statDict["Big Chances Created"]
    Hit_woodwork = statDict["Hit woodwork"]

    # Team Play stats
    Passes = statDict["Passes"]
    Passes_per_match = statDict["Passes per match"]
    Pass_accuracy = statDict["Pass accuracy %"]/100
    Crosses = statDict["Crosses"]
    Cross_accuracy = statDict["Cross accuracy %"]/100

    # Defense stats
    Goals_Conceded = statDict["Goals Conceded"]
    Goals_conceded_per_match = statDict["Goals conceded per match"]
    Saves = statDict["Saves"]
    Tackles = statDict["Tackles"]
    Tackle_success = statDict["Tackle success %"]/100
    Blocked_shots = statDict["Blocked shots"]
    Interceptions = statDict["Interceptions"]
    Clearances = statDict["Clearances"]
    Headed_Clearance = statDict["Headed Clearance"]
    Aerial_Battles_Duels_Won = statDict["Aerial Battles/Duels Won"]
    Errors_leading_to_goal = statDict["Errors leading to goal"]
    Own_goals = statDict["Own goals"]

    # Disipline stats
    Yellow_cards = statDict["Yellow cards"]
    Red_cards = statDict["Red cards"]
    Fouls = statDict["Fouls"]
    Offsides = statDict["Offsides"]

    if Matches_played == 0:
            Matches_played = 10 ^ 7
    if Tackles == 0:
        Tackles = 10 ^ 7
    if Shots == 0:
        Shots = 10 ^ 7
    if Fouls == 0:
        Fouls = 10 ^ 7
    if Goals == 0:
        Goals = 10 ^ 7

    scoreGeneral = (1*Wins/Matches_played + 0.5 *
                    (Matches_played-Wins-Losses)/Matches_played + 1*Clean_sheets/Matches_played)/2.5
    scoreAttack = (1*Goals/Shots + 1*Shooting_accuracy +
                   1*Big_Chances_Created/Shots)/3
    scoreDefense = (1*Tackle_success + 1*Blocked_shots/Tackles + 1*Interceptions/Tackles +
                    1*Clean_sheets/Matches_played + 1*(Goals-Goals_Conceded)/Goals - 1*(Own_goals+Errors_leading_to_goal)/Matches_played)/7
    scoreDiscipline = (1*Yellow_cards/Fouls + 1 *
                       Red_cards/Fouls + 1*Offsides/Fouls)/3
    scoreTeamPlay = (1*Cross_accuracy + 1*Pass_accuracy)/2
    score = ((scoreGeneral + scoreAttack +
              scoreTeamPlay - scoreDiscipline + scoreDefense)/5)

    return score


def positionEval(playerList):
    ForwardScore = 0
    DefenderScore = 0
    MidfielderScore = 0
    GoalkeeperScore = 0
    ForwardAppearances = 0
    DefenderAppearance = 0
    MidfielderAppearance = 0
    GoalkeeperAppearance = 0

    for i in playerList:
        if i["Appearances"] == 0:
            continue
        if i["Position"] == "Forward":
            ForwardAppearances = ForwardAppearances + i["Appearances"]
            ForwardScore = ForwardScore + i["Score"]

        if i["Position"] == "Defender":
            DefenderAppearance = DefenderAppearance + i["Appearances"]
            DefenderScore = DefenderScore + i["Score"]

        if i["Position"] == "Midfielder":
            MidfielderAppearance = MidfielderAppearance + i["Appearances"]
            MidfielderScore = MidfielderScore + i["Score"]

        if i["Position"] == "Goalkeeper":
            GoalkeeperAppearance = GoalkeeperAppearance + i["Appearances"]
            GoalkeeperScore = GoalkeeperScore + i["Score"]

    ForwardScore = ForwardScore/ForwardAppearances
    DefenderScore = DefenderScore/DefenderAppearance
    MidfielderScore = MidfielderScore/MidfielderAppearance
    GoalkeeperScore = GoalkeeperScore/GoalkeeperAppearance

    PositionScore = [ForwardScore, DefenderScore,
                     MidfielderScore, GoalkeeperScore]
    return PositionScore
