def safe_pawns(pawns):
    
    safePawns = 0
    
    for pawn in pawns:
        col = pawn[0]
        row = pawn[1]
        
        defenseRow = str(int(row)-1)
        defenseLeft = chr(ord(col)-1) + defenseRow
        defenseRight = chr(ord(col)+1) + defenseRow
        
        if defenseLeft in pawns or defenseRight in pawns:
            safePawns += 1
            
    return safePawns
