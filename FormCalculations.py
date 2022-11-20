def teamFormScore(formDict):
    FS1 = (formDict["Games Played"] - formDict["Losses"] - 0.5*formDict["Draws"])/formDict["Games Played"]
    FS2 = (formDict["Goals Made"] - formDict["Goals Conceded"])/(formDict["Goals Made"] + formDict["Goals Conceded"])
    TFS = 100*(FS1 + FS2)
    return TFS

