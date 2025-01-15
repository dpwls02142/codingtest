dice_num = input().split(" ")

if len(dice_num) != 3:
    exit()
else:
    dice_num = list(map(int, dice_num))
    if dice_num[0] == dice_num[1] == dice_num[2]:
        print(10000 + dice_num[0] * 1000)
    elif dice_num[0] == dice_num[1] or dice_num[0] == dice_num[2]:
        print(1000 + dice_num[0] * 100)
    elif dice_num[1] == dice_num[2]:
        print(1000 + dice_num[1] * 100)
    else:
        print(max(dice_num) * 100)