import sys

t = int(sys.stdin.readline().rstrip())
for _ in range (t):
    n = int(sys.stdin.readline().rstrip())
    team_number = list(map(int, sys.stdin.readline().rstrip().split()))
    team_cnt = {}

    for i in range (n):
        if team_number[i] in team_cnt:
            team_cnt[team_number[i]] += 1
        else:
            team_cnt[team_number[i]] = 1
    # for idx, value in enumerate(team_cnt, start = 1): ==> RuntimeError: dictionary changed size during iteration
    #     if value < 6:
    #         del(team_cnt[idx])
    # print(team_cnt)
    short_team = {}
    for key, value in team_cnt.items():
        if value < 6:
            short_team[key] = 1

    team = {}
    idx = 1
    for i in range(n):
        current_team = team_number[i]
        if current_team not in short_team:
            if current_team in team:
                if team[current_team][0] < 4:
                    team[current_team][0] += 1
                    team[current_team][1] += idx
                elif team[current_team][0] == 4:
                    team[current_team][0] += 1
                    team[current_team][2] = idx
            else:
                team[current_team] = [1, idx, 0]

            idx += 1
    
    team = sorted(team.items(), key=lambda x:(x[1][1], x[1][2]))
    print(team[0][0])