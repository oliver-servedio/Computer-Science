def scoreTosses(numPlayers, tosses):
    final = {}
    for p in range(len(tosses)):
        
        toss = (tosses[p]).split(' ')
        score = 0
        toss_length = len(toss)

        for i in range(len(toss)):
            x = toss[i]
            l = list(x)

            for plus in l:
                if plus == '+':
                    score += 2
                    del l[-1]
                    x = x.replace('+', '')
            
            
            if len(x) == 1:
                if x == 'A' or x == 'R':
                    score += 1
                if x == 'O' or x == 'G':
                    score += 3
                if x == 'B':
                    score += 6

            else:
                score += 1
                for n in l:
                    if n == 'A' or n == 'R':
                        score += 1
                    if n == 'O' or n == 'G':
                        score += 3
                    if n == 'B':
                        score += 6
        final[p+1] = [toss_length, score]
    sorted_results = sorted(final.items(), key=lambda item: (-item[1][1], item[1][0]))
    result = []
    for player, stats in sorted_results:
        result.append(f'{player}-{stats[1]}')
        print(result)
    result = ' '.join(result)
    return result






result = scoreTosses(3, ['A R AO+', 'B+ GR OA B', 'G OB+'])
print(result)

