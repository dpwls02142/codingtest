import sys
n = int(sys.stdin.readline().rstrip())
for _ in range (n):
    team, solve, my_id, log = map(int, sys.stdin.readline().rstrip().split())
    all_team = {}
    team_score = {}
    team_cnt = {}
    last_sub = {}
    for _ in range (1, team + 1):
        all_team[_] = {}
        team_score[_] = 0
        team_cnt[_] = 0
        last_sub[_] = 0

    for i in range (1, log + 1):
        t_id, j, s = map(int, sys.stdin.readline().rstrip().split())
        team_cnt[t_id] += 1
        last_sub[t_id] = i
        if j not in all_team[t_id]:
            all_team[t_id][j] = s
            team_score[t_id] += s
        else:
            if s > all_team[t_id][j]:
                team_score[t_id] += s - all_team[t_id][j]
                all_team[t_id][j] = s
    sorted_teams = sorted(
        range(1, team + 1),
        key=lambda x: (-team_score[x], team_cnt[x], last_sub[x])
    )
    # print(sorted_teams)
    print(sorted_teams.index(my_id) + 1)