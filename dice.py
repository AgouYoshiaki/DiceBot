import discord
import random
import re

client = discord.Client()  # 接続に使用するオブジェクト
"""3引くから0-9"""
damage_board=[[0,0,0,1,2,2,3,3,4,4],[0,0,0,1,2,3,3,3,4,4],[0,0,0,1,2,3,4,4,4,4],[0,0,1,1,2,3,4,4,4,5],[0,0,1,2,2,3,4,4,5,5],[0,1,1,2,2,3,4,5,5,5],
[0,1,1,2,3,3,4,5,5,5],[0,1,1,2,3,4,4,5,5,6],[0,1,2,2,3,4,4,5,6,6],[0,1,2,3,3,4,4,5,6,7],[1,1,2,3,3,4,5,5,6,7],
[1,2,2,3,3,4,5,6,6,7],[1,2,2,3,4,4,5,6,6,7],[1,2,3,3,4,4,5,6,7,7],[1,2,3,4,4,4,5,6,7,8],[1,2,3,4,4,5,5,6,7,8],
[1,2,3,4,4,5,6,7,7,8],[1,2,3,4,5,5,6,7,7,8],[1,2,3,4,5,6,6,7,7,8],[1,2,3,4,5,6,7,7,8,9],[1,2,3,4,5,6,7,8,9,10],
[1,2,3,4,6,6,7,8,9,10],[1,2,3,5,6,6,7,8,9,10],[2,2,3,5,6,7,7,8,9,10],[2,3,4,5,6,7,7,8,9,10],[2,3,4,5,6,7,8,8,9,10],
[2,3,4,5,6,8,8,9,9,10],[2,3,4,6,6,8,8,9,9,10],[2,3,4,6,6,8,9,9,10,10],[2,3,4,6,7,8,9,9,10,10],[2,4,4,6,7,8,9,10,10,10],
[2,4,5,6,7,8,9,10,10,11],[3,4,5,6,7,8,10,10,10,11],[3,4,5,6,8,8,10,10,10,11],[3,4,5,6,8,9,10,10,11,11],[3,4,5,7,8,9,10,10,11,12],
[3,5,5,7,8,9,10,11,11,12],[3,5,6,7,8,9,10,11,12,12],[3,5,6,7,8,10,10,11,12,13],[4,5,6,7,8,10,11,11,12,13],[4,5,6,7,9,10,11,11,12,13],
[4,6,6,7,9,10,11,12,12,13],[4,6,7,7,9,10,11,12,13,13],[4,6,7,8,9,10,11,12,13,14],[4,6,7,8,10,10,11,12,13,14],[4,6,7,9,10,10,11,12,13,14],
[4,6,7,9,10,10,12,13,13,14],[4,6,7,9,10,11,12,13,13,15],[4,6,7,9,10,12,12,13,13,15],[4,6,7,10,10,12,12,13,14,15],[4,6,8,10,10,12,12,13,15,15],
[5,7,8,10,10,12,12,13,15,15],[5,7,8,10,11,12,1,13,15,15],[5,7,9,10,11,12,12,14,15,16],[5,7,9,10,11,12,13,14,15,16],[5,7,10,10,11,12,13,14,16,16],
[5,8,10,10,11,12,13,15,16,16],[5,8,10,11,11,12,13,15,16,17],[5,8,10,11,12,12,13,15,16,17],[5,9,10,11,12,12,14,15,16,17],[5,9,10,11,12,13,14,15,16,18],
[5,9,10,11,12,13,14,16,17,18],[5,9,10,11,13,13,14,16,17,18],[5,9,10,11,13,13,15,17,17,18],[5,9,10,11,13,14,15,17,17,18],[5,9,10,12,13,14,15,17,18,18],
[5,9,10,12,13,15,15,17,18,19],[5,9,10,12,13,15,16,17,19,19],[5,9,10,12,14,15,16,17,19,19],[5,9,10,12,14,16,16,17,19,19],[5,9,10,12,14,16,17,18,19,19],
[5,9,10,13,14,16,17,18,19,20],[5,9,10,13,15,16,17,18,19,20],[5,9,10,13,15,16,17,19,20,21],[6,9,10,13,15,16,18,19,20,21],[6,9,10,13,16,16,18,19,20,21],
[6,9,10,13,16,17,18,19,20,21],[6,9,10,13,16,17,18,20,21,22],[6,9,10,13,16,17,19,20,22,23],[6,9,10,13,16,18,19,20,22,23],[6,9,10,13,16,18,20,21,22,23],
[6,9,10,14,17,18,20,21,22,23],[6,9,10,14,17,18,20,21,22,24],[6,9,11,14,17,18,20,21,23,24],[6,9,11,14,17,19,20,21,23,24],[6,9,11,14,17,19,21,22,23,24],
[7,10,11,14,17,19,21,22,23,25],[7,10,12,14,17,19,21,22,24,25],[7,10,12,14,18,19,21,22,24,25],[7,10,12,15,18,19,21,22,24,26],[7,10,12,15,18,19,21,23,25,26],
[7,11,13,15,18,19,21,23,25,26],[7,11,13,15,18,20,21,23,25,27],[8,11,13,15,18,20,22,23,25,27],[8,11,13,16,18,20,22,23,25,28],[8,11,14,16,18,20,22,23,26,28],
[8,11,14,16,19,20,22,23,26,28],[8,12,14,16,19,20,22,24,26,28],[8,12,15,16,19,20,22,24,27,28],[8,12,15,17,19,20,22,24,27,29],[8,12,15,18,19,20,22,24,27,30]]

def roll_dice(dice_count):
    results=""
    sum=0
    for i in range(int(dice_count[0])):
        randnum=random.randint(1,int(dice_count[1]))
        sum+=randnum
        results+=str(randnum)
        if i!=int(dice_count[0])-1:
            results+=", "
    return results,sum

def get_keyend(mes,key_end):
    """return 1-indexd number"""
    while key_end+1<len(mes):
        if mes[key_end+1].isdecimal():
            key_end+=1
        else :
            break
    return key_end+1

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')



@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return
    if message.content.find("/r")!=0:
        return
    
    message_list = message.content.split()
    """roll_dice"""
    total=0
    count=0
    critical=1000000
    goal=1000000
    use_damage=-1
    achieve=""
    fix_options=""
    goal_options=""
    for i in range(len(message_list)):
        results=""
        if message_list[i].find("<=")!=-1:
            key=message_list[i].find("<=")
            key_end=get_keyend(message_list[i],key+2)
            goal=int(message_list[i][key+2:key_end])
            goal_options+=message_list[i][key:key_end]
        if message_list[i].find(">=")!=-1:
            key=message_list[i].find(">=")
            key_end=get_keyend(message_list[i],key+2)
            goal=int(message_list[i][key+2:key_end])*-1
            goal_options+="-"+message_list[i][key:key_end]
        if message_list[i].find("+")!=-1:
            key=message_list[i].find("+")
            key_end=get_keyend(message_list[i],key+1)
            print(key_end)
            print(len(message_list[i]))
            if key_end!=len(message_list[i]) and message_list[i][key_end]=="d":
                """ need refactoring """
                dice=[int(message_list[i][key_end-1]),int(message_list[i][key_end+1])]
                result,sum=roll_dice(dice)
                await message.channel.send("result")
                total+=sum
            else :
                total+=int(message_list[i][key+1:key_end])
                count+=1
                fix_options=message_list[i][key:key_end]+fix_options

        if message_list[i].find("d")>0:
            dice_count=re.split('[d<>=+]',message_list[i])
            print(dice_count[0]+dice_count[1])
            if critical<=int(dice_count[0]):
                await message.channel.send("you are cheating!!")
                break
            count+=int(dice_count[0])
            results+=dice_count[0]+"d"+dice_count[1]+"("
            while True:
                result,sum=roll_dice(dice_count)
                results+=result
                """SW"""
                if dice_count[0]=="2" and dice_count[1]=="6":
                    if sum==2:
                        results+="  fumble!  "
                        break
                    if use_damage!=-1:
                        total+=damage_board[use_damage][sum-3]
                    else :
                        total+=sum
                    if critical<=sum:
                        results+="  burst!  "
                        continue
                else :
                    total+=sum
                """CoC"""
                if dice_count[0]=="1" and dice_count[1]=="100" and goal!=1000000:
                    if sum<=5:
                        achieve="critical!!"
                    elif sum<=goal/5:
                        achieve="special!!"
                    elif 96<=sum:
                        achieve="fumble :\\"
                    elif sum<=goal:
                        achieve="success"
                    else:
                        achieve="failure"
                break
            results+=")"
            await message.channel.send(results+fix_options+"="+str(total)+goal_options)    
            if achieve=="" and goal!=1000000:
                if goal<=-1:
                    total*=-1
                if total<=goal:
                    achieve="success"
                else:
                    achieve="failure"
            if achieve!="":
                await message.channel.send(achieve)
            fix_options=""
            goal_options=""
            total=0
        elif message_list[i].find("c")==0:
            critical=int(re.sub("\\D","",message_list[i]))
        elif message_list[i].find("d")==0 or message_list[i].find("k")==0:
            use_damage=int(message_list[i][1:])
        """elif i!=0 :
            await message.channel.send(message_list[i])"""




# botの接続と起動
# （botアカウントのアクセストークンを入れてください）
client.run("")
