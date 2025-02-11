def solution(n, words):
    use_words = set()
    use_words.add(words[0])
    for i in range (1, len(words)):
        prev = words[i-1]
        curr = words[i]
        
        player_num = (i % n) + 1
        turn_num = (i // n) + 1
        
        if words[i] in use_words:
            return(player_num, turn_num)
            
        if prev[-1] != curr[0]:
            return(player_num, turn_num)
            
        use_words.add(curr)

    return [0,0]