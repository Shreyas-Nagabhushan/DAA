def stable_match(men_prefs, woman_prefs):
    free_men = set(men_prefs.keys())
    pairings = {} 

    while free_men:
        proposer = free_men.pop()
        proposer_prefs = men_prefs[proposer]

        for desired_woman in proposer_prefs:
            if desired_woman not in pairings:
                pairings[desired_woman] = proposer
                break 
            
            else:
                current_partner = pairings[desired_woman]
                if woman_prefs[desired_woman].index(proposer) < woman_prefs[desired_woman].index(current_partner):
                    pairings[desired_woman] = proposer 
                    free_men.add(current_partner)
                    break 
    
    print(pairings)

men_prefs = {
    'A': ['V', 'W', 'X'],
    'B': ['W', 'V', 'X'],
    'C': ['V', 'W', 'X']
}

woman_prefs = {
    'V': ['A', 'B', 'C'],
    'W': ['B', 'C', 'A'],
    'X': ['C', 'A', 'B']
}

# Call the function with the sample input
stable_match(men_prefs, woman_prefs)