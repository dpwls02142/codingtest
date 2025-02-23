def solution(today, terms, privacies):
    today_year, today_month, today_day = map(int, today.split('.'))
    ans = []

    term_dict = {}
    for term in terms:
        t, m = term.split(" ")
        term_dict[t] = int(m)

    for i in range(len(privacies)):
        p_date, p_type = privacies[i].split(" ")
        p_year, p_month, p_day = map(int, p_date.split("."))

        if p_type in term_dict:
            t = term_dict[p_type]
            p_month += t
            p_day -= 1
            
            # 월이 12를 넘어갈 때 처리
            if p_month > 12:
                p_year += (p_month - 1) // 12
                p_month = (p_month - 1) % 12 + 1

        if (p_year < today_year) or \
           (p_year == today_year and p_month < today_month) or \
           (p_year == today_year and p_month == today_month and p_day < today_day):
            ans.append(i + 1)

    return ans