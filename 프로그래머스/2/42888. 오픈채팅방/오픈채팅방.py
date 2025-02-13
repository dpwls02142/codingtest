def solution(record):
    user_dict = {}
    log = []
    
    for entry in record:
        data = entry.split()
        command, uid = data[0], data[1]

        if command == "Enter":
            nickname = data[2]
            user_dict[uid] = nickname
            log.append([uid, "님이 들어왔습니다."])

        elif command == "Leave":
            log.append([uid, "님이 나갔습니다."])

        elif command == "Change":
            nickname = data[2]
            user_dict[uid] = nickname
            
    return [user_dict[uid] + action for uid, action in log]