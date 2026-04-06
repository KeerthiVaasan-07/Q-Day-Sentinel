def calculate_risk_score(data_shelf_life, transition_time):
    # Estimated years until a Cryptographically Relevant Quantum Computer (CRQC)
    years_until_qday = 2035 - 2026 
    
    # Mosca's Theorem: If (Shelf Life + Transition Time) > Years to Q-Day, you are in trouble.
    exposure_gap = (data_shelf_life + transition_time) - years_until_qday
    
    if exposure_gap > 0:
        return "CRITICAL", exposure_gap
    elif exposure_gap > -3:
        return "WARNING", exposure_gap
    else:
        return "SAFE", exposure_gap
