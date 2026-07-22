import random
import time

# player_item = []
# devil_item = []
#
# all_item_num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# all_item_name = ["手机", "香烟", "过期药", "手铐", "刀", "啤酒", "放大镜", "肾上腺素", "转换器"]
# all_item = {}
# all_item[all_item_num] = all_item_name
# print("恶魔轮盘赌")
rule="""
规则
与恶魔进行对赌，每局随机2~4滴血，2~8颗子弹，子弹半真半假，打死恶魔算一轮，总共三轮
喝药：无尽模式，每三轮可以选择结束或者现金翻倍 不喝药：三轮结束
a 手机：告诉你未来一发子弹的真假（不会是第一发）
b 香烟：恢复一滴血
c 过期药：50%恢复两滴血 50%扣一滴血
d 手铐：使得对方下一回合无法行动
e 刀：伤害*2，不可叠加
f 啤酒：退掉当前膛中子弹
g 放大镜：获悉当前膛中子弹真假
h 肾上腺素：偷取对面的一样物品（不能是肾上腺素）
i 转换器：转换当前膛中子弹的真假
"""
menu="""
########操作界面########
1.使用道具
    a 手机 b 香烟 c 过期药 d 手铐 e 刀 f 啤酒 g 放大镜 h 肾上腺素 i 转换器 
2.选择射击对象
    s 射击对面 ss 射击自己
"""

# while True:
#     name = input("请输入名称：")
#     if name=="god":
#         continue
#     else:
#         break
#
# print(rule)
# choice = input("是否选择吃药？不吃药：1，吃药：2 :")
# match choice:
#         case "1":
#                     round_num=1
#                     player_life=random.randint(2,4)
#                     devil_life=player_life
#                     # 随机生命值
#                     bullet_num = random.randint(2, 8)
#                     if bullet_num%2==0:
#                         real=bullet_num/2
#                         fake=bullet_num/2
#                     else:
#                         real=bullet_num//2
#                         fake=bullet_num//2+1
#                     # 随机子弹和子弹规则
#                     item_get_num= random.randint(2, 4)
#                     player_item_num=0
#                     player_item_num+=item_get_num
#                     devil_item_num=0
#                     devil_item_num+=item_get_num
#                     # 随机获取物品个数
#                     while item_get_num>(8-player_item_num):
#                         item_get_num-=1
#                         if item_get_num-(8-player_item_num)==1:
#                             item_get_num -= 1
#                             print("道具栏已满，真遗憾~")
#                             break
#                     # 玩家获取物品上限和提示
#                     while item_get_num>(8-devil_item_num):
#                         item_get_num-=1
#                     # 恶魔获取物品上限
#                     for i in range(item_get_num):
#                         range_item = random.randint(0, 8)
#                         player_item.append(all_item_name[range_item])
#                     for i in range(item_get_num):
#                         range_item = random.randint(0, 8)
#                         devil_item.append(all_item_name[range_item])
#                     #玩家和恶魔随机获取物品
#
#
#                         print(f"第{round_num}局")
#                         while player_life or devil_life>0:
#                             print(menu)
#                             print(f"你的生命值：{player_life}")
#                             print(f"恶魔的生命值：{devil_life}")
#                             print(f"你的物品：{player_item}")
#                             print(f"恶魔的物品：{devil_item}")
#
#
# class Inventory:
#     def __init__(self):
#         self.slots = []  # 当前存放的道具
#         self.max_slots = 8  # 最大8格
#
#     def add(self, item):
#         """添加道具，满了返回False"""
#         if len(self.slots) >= self.max_slots:
#             print(f"物品栏已满，无法存放 {item}！")
#             return False
#         self.slots.append(item)
#         return True
#
#     def remove(self, item):
#         """移除道具"""
#         if item in self.slots:
#             self.slots.remove(item)
#             return True
#         return False
#
#     def has(self, item):
#         """检查是否有某道具"""
#         return item in self.slots
#
#
#     def show(self):
#         """显示物品栏"""
#         print(f"[{' | '.join(self.slots) if self.slots else '空'}] ({len(self.slots)}/8)")
#
#
# # 使用
# player_inventory = Inventory()
# enemy_inventory = Inventory()
#
# items = ["转换器", "香烟", "刀", "放大镜", "手机", "手铐", "能量饮料", "肾上腺素", "过期药"]
#
# # 各抽2-4个
# draw = random.randint(2, 4)
# i=draw
# for _ in range(i):
#     player_inventory.add(random.choice(items))
#     enemy_inventory.add(random.choice(items))
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# 定义所有物品
ITEM_NAMES = {
    "phone": "手机", "cigarette": "香烟", "expired_medicine": "过期药",
    "handcuffs": "手铐", "knife": "刀", "beer": "啤酒",
    "magnifier": "放大镜", "adrenaline": "肾上腺素", "inverter": "转换器"
}
class InteractiveTextGame:
    def __init__(self, player):
        # self.player = {
        #     "name":"",
        #     "hp":random.randint(2,5),
        # }
        # self.devil = {
        #     "name": "敌人",
        #     "hp":player["hp"],

        # }
        self.player = player
        hp = random.randint(2, 5)
        self.player["hp"] = hp
        self.devil = {"name": "恶魔", "hp": hp, "max_hp": hp}


        self.chamber=[]
        self.current_index=0
        # self._load_chamber()

        self.round_count = 0
        # self.big_round=0

        self.player_skip=False
        self.devil_skip=False
        self.knife_active=False
        self.handcuffs_used_this_round = False
        self.current_round_shots = []
        self._new_round_player_first = False  # ★ 新回合玩家先手标记

        self.player_inventory=[]
        self.enemy_inventory=[]
        # self.max_inventory=8

        # self.all_items=["转换器", "香烟", "刀", "放大镜", "手机",
        #     "手铐", "能量饮料", "肾上腺素", "过期药"]
        self.all_items = [
            "phone", "cigarette", "expired_medicine",
            "handcuffs", "knife", "beer",
            "magnifier", "adrenaline", "inverter"
        ]

    # ==================== 物品栏 ====================
    def _get_inventory(self, user):
        if user["name"] == self.player["name"]:
            return self.player_inventory
        else:
            return self.devil_inventory

    def _remove_item(self, inventory, item_name):
        if item_name in inventory:
            inventory.remove(item_name)
            return True
        return False

    def _count_item(self, inventory, item_name):
        return inventory.count(item_name)

    # ==================== 枪械系统 ====================
    def _load_chamber(self):
        total=random.randint(2,8)
        real_count=total//2
        fake_count=total-real_count

        bullets=["real"]*real_count+["fake"]*fake_count
        random.shuffle(bullets)

        self.chamber=bullets
        self.current_index=0
        #==========================新增==================
        self.current_round_shots = []

        self.player_inventory = []
        self.devil_inventory = []
        draw = random.randint(2, 4)
        for _ in range(draw):
            self.player_inventory.append(random.choice(self.all_items))
            self.devil_inventory.append(random.choice(self.all_items))

        self.handcuffs_used_this_round = False
        self.player_skip = False  # ★ 重置
        self.devil_skip = False  # ★ 重置
        self.knife_active = False
        self._new_round_player_first = True  # ★ 标记新回合玩家先手

    # ==========================新增==================
    def _show_round_info(self):
        real = self.chamber.count("real")
        fake = self.chamber.count("fake")
        total = len(self.chamber)
        print(f"\n{'=' * 40}")
        print(f"🔫 第 {self.round_count} 轮！枪膛共 {total} 发子弹：{real} 真 / {fake} 假")
        print(f"{'=' * 40}")

    def fire(self):
        if self.current_index>=len(self.chamber):
            self._load_chamber()
            self._show_round_info()
            return None
        bullet=self.chamber[self.current_index]
        self.current_index+=1
        self.knife_active = False
        return bullet

    def get_player_choice(self):
        """获取玩家选择"""
        print("\n请选择行动：")
        print("1. 向恶魔开枪")
        print("2. 向自己开枪")
        print("3. 使用转换器（改变当前膛中子弹状态，剩余: {}）".format(self.player["transformer"]))
        print("4. 使用香烟（恢复1HP，剩余: {}）".format(self.player["cigarette"]))
        print("5. 使用刀（子弹伤害翻倍，剩余: {}）".format(self.player["knife"]))
        print("6. 使用放大镜（获知膛中子弹信息，剩余: {}）".format(self.player["magnifying_glass"]))
        print("7. 使用手机（获知第2~X发子弹中某一发的信息，剩余: {}）".format(self.player["phone"]))
        print("8. 使用手铐（使对手下一回合不能行动，剩余: {}）".format(self.player["handcuffs"]))
        print("9. 使用能量饮料（退弹，剩余: {}）".format(self.player["energy_drink"]))
        print("10. 使用肾上腺素（偷走对面的一个道具，不能是肾上腺素，剩余: {}）".format(self.player["adrenaline"]))
        print("11. 使用过期药（吃药50%回两滴血50%扣一滴血，剩余: {}）".format(self.player["expired_medicine"]))
        print("12. 退出游戏")

        while True:
            try:
                choice = int(input("输入数字选择 (1-12): "))
                if 1 <= choice <=12:
                    return choice
                else:
                    print("请输入1-12之间的数字")
            except ValueError:
                print("请输入有效的数字")

    def generate_enemy(self):
        return{
            "hp":self.player["hp"],
        }

    def show_status(self):
        print("\n" + "=" * 40)
        print(f"玩家: {self.player['name']}")
        print(f"HP: {self.player['hp']}")
        print(f"bullet num: {len(self.chamber)}")
        print(f"转换器: {self.player['transformer']}")
        print(f"香烟: {self.player['cigarette']}")
        print(f"刀: {self.player['knife']}")
        print(f"放大镜: {self.player['magnifying_glass']}")
        print(f"手机: {self.player['phone']}")
        print(f"手铐: {self.player['handcuffs']}")
        print(f"能量饮料: {self.player['energy_drink']}")
        print(f"肾上腺素: {self.player['adrenaline']}")
        print(f"过期药: {self.player['expired_medicine']}")
        print("=" * 40)

    # def player_attack(self,enemy,knife_use=False):
    #     if self.bullet["fire"]==1:
    #         print("实弹")
    #         if knife_use:
    #             enemy["hp"] -= 2
    #         else:
    #             enemy["hp"]-=1
    #     else:
    #         print("空弹")
    #
    # def player_self_attack(self,player,knife_use=False):
    #     if self.bullet["fire"]==1:
    #         print("实弹")
    #         if knife_use:
    #             player["hp"] -= 2
    #         else:
    #             player["hp"]-=1
    #     else:
    #         print("空弹")
    #
    # def enemy_self_attack(self,enemy,knife_use=False):
    #     if self.bullet["fire"] == 1:
    #         print("实弹")
    #         if knife_use:
    #             enemy["hp"] -= 2
    #         else:
    #             enemy["hp"] -= 1
    #     else:
    #         print("空弹")

    def _attack_target(self, target,attacker_name):
        """攻击目标（玩家或敌人）"""

        bullet=self.fire()
        if bullet is None:
            return (False,False,True)

        name = target["name"]
        damage = 2 if self.knife_active else 1

        if bullet=="real":
            target["hp"] -= damage
            if damage==2:
                print(f" 实弹！{name} 受到 {damage} 点伤害（刀伤翻倍）！(剩余HP: {target['hp']})")
            else:
                print(f" 实弹！{name} 受到 {damage} 点伤害！(剩余HP: {target['hp']})")
            self.knife_active = False
        else:
            print(f" 空包弹！")
            self.knife_active = False
            # ★ 核心规则：空包弹打自己 → 保持回合
            if target["name"] == attacker_name:
                print(" 空包弹打自己，回合继续！")
                return (target["hp"] <= 0, True, False)
            return (False, False, False)

    # def player_attack(self, enemy, use_knife=False):
    #     return self._attack_target(enemy, use_knife)
    #
    # def player_self_attack(self, player, use_knife=False):
    #     return self._attack_target(player, use_knife)
    #
    # def enemy_attack(self, player, use_knife=False):
    #     return self._attack_target(player, use_knife)
    #
    # def enemy_self_attack(self, enemy, use_knife=False):
    #     return self._attack_target(enemy,use_knife)

    # def enemy_movement(self,enemy):

    # # player 调用
    # self.use_cigarette(self.player)
    #
    # # enemy 调用
    # self.use_cigarette(self.enemy)


    # def use_transformer(self,user):
    #     if user["transformer"] > 0:
    #         user["fire"] ^= 1
    #         user["transformer"] -= 1
    #         print(f"{user['name']}使用了转换器，子弹状态改变")
    #         return True
    #     else:
    #         print("没有转换器了！")
    #         return False
    def use_inverter(self, user):
        inv = self._get_inventory(user)
        if self._count_item(inv, "inverter") == 0:
            print(" 没有转换器！")
            return False
        self._remove_item(inv, "inverter")
        if self.current_index >= len(self.chamber):
            print("枪膛已空！")
            return False
        old = self.chamber[self.current_index]
        self.chamber[self.current_index] = "real" if old == "fake" else "fake"
        print(f" {user['name']} 使用了转换器！当前子弹已反转。")
        return True

    def use_cigarette(self, user):
        # if user["cigarette"] > 0:
        #     user["hp"] += 1
        #     user["cigarette"] -= 1
        #     print(f"{user['name']}使用了香烟，回一滴血")
        #     return True
        # else:
        #     print(f"{user['name']}没有香烟了！")
        #     return False
        inv = self._get_inventory(user)
        if self._count_item(inv, "cigarette") == 0:
            print(" 没有香烟！")
            return False
        self._remove_item(inv, "cigarette")
        user["hp"] = min(user["hp"] + 1, user.get("max_hp", 4))
        print(f" {user['name']} 抽了根烟，回复1点HP！(HP: {user['hp']})")
        return True

    # def use_knife(self, user):
    #     if user["knife"] > 0:
    #         user["knife"] -= 1
    #         print(f"{user['name']}使用了刀，伤害翻倍")
    #         return True
    #     else:
    #         print(f"{user['name']}没有刀了！")
    #         return False
    def use_knife(self, user):
        inv = self._get_inventory(user)
        if self._count_item(inv, "knife") == 0:
            print(" 没有刀！")
            return False
        if self.knife_active:
            print(" 刀已使用，请先打出当前子弹！")
            return False
        self._remove_item(inv, "knife")
        self.knife_active = True
        print(f" {user['name']} 磨了磨刀，下一发子弹伤害翻倍！")
        return True

    # def attack(self, attacker, defender):
    #     damage = attacker["fire"]  # 基础伤害
    #
    #     if self.use_knife(attacker):  # 如果用了刀
    #         damage *= 2  # 仅本次翻倍
    #
    #     defender["hp"] -= damage
    #     print(f"{attacker['name']}造成 {damage} 点伤害")
    #
    #     # 下次攻击时，attacker["fire"] 还是原来的值，不受影响


    # def use_magnifying_glass(user,bullet):
    #     if user["magnifying glass"] > 0:
    #         user["magnifying glass"] -= 1
    #         if bullet["fire"]==1:
    #             print(f"{user['name']}使用了放大镜，子弹为真")
    #         else:
    #             print(f"{user['name']}使用了放大镜，子弹为假")
    #         return True
    #     else:
    #         print(f"{user['name']}没有放大镜了！")
    #         return False
    def use_magnifier(self, user):
        inv = self._get_inventory(user)
        if self._count_item(inv, "magnifier") == 0:
            print(" 没有放大镜！")
            return False
        self._remove_item(inv, "magnifier")
        if self.current_index >= len(self.chamber):
            print(" 枪膛已空！")
            return False
        bullet = self.chamber[self.current_index]
        print(f" {user['name']} 查看了当前子弹：{'实弹' if bullet == 'real' else '空包弹'}")
        self.current_round_shots.append(bullet)
        return True
    # 调用时：InteractiveTextGame.use_magnifying_glass(user, bullet)

    def use_phone(self, user):
        # if user.get("phone", 0) <= 0:
        #     return None
        # user["phone"] -= 1
        #
        # # 没有足够子弹可查看（至少需要2发才能排除第1发）
        # if len(self.chamber) <= 1:
        #     return None
        #
        # # 随机选一个索引，排除第1发（索引0）
        # idx = random.randint(1, len(self.chamber) - 1)
        # chosen = self.chamber[idx]
        # result = "真子弹" if chosen == "real" else "空包弹"
        #
        # # 判断是否已打出
        # if idx < self.current_index:
        #     status = "已打出"
        # else:
        #     status = "未打出"
        #
        # if is_player:
        #     print(f"{user['name']}使用了手机！")
        #     print(f"第 {idx + 1} 发子弹({status})是【{result}】！")
        # else:
        #     print(f"{user['name']}使用了手机")
        #
        # return {"index": idx, "real": chosen == "real"}
        inv = self._get_inventory(user)
        if self._count_item(inv, "phone") == 0:
            print(" 没有手机！")
            return False
        self._remove_item(inv, "phone")
        remaining = len(self.chamber) - self.current_index
        if remaining <= 0:
            print(" 枪膛已空，无法使用手机")
            return False
        idx = random.randint(self.current_index, len(self.chamber) - 1)
        bullet = self.chamber[idx]
        pos = idx - self.current_index + 1
        print(f" 第 {pos} 发子弹是: {'实弹' if bullet == 'real' else '空包弹'}")
        self.current_round_shots.append(bullet)
        return True

    def use_handcuffs(self,user):
        # if user["handcuffs"] > 0:
        #     self.enemy_skip = True
        #     print(f"{user['name']}使用了手铐，对方下一回合不能行动")
        #     user["handcuffs"] -= 1
        #     return True
        # else:
        #     print(f"{user['name']}没有手铐了！")
        #     return False
        inv = self._get_inventory(user)
        if self._count_item(inv, "handcuffs") == 0:
            print(" 没有手铐！")
            return False
        if self.handcuffs_used_this_round:
            print(" 本回合已经使用过手铐了！")
            return False
        self._remove_item(inv, "handcuffs")

        # ★ 铐住对方，不是自己
        if user["name"] == self.player["name"]:
            self.devil_skip = True
            print(f" {user['name']} 使用了手铐！恶魔下回合将被跳过！")
        else:
            self.player_skip = True
            print(f" {user['name']} 使用了手铐！玩家下回合将被跳过！")

        self.handcuffs_used_this_round = True
        return True

    # def use_energy_drink(self, user,is_player=False):
    #     # idx = random.randint(1, len(self.chamber) - 1)
    #     # chosen = self.chamber[idx]
    #     chosen=self.chamber[self.current_index]
    #     result = "真子弹" if chosen == "real" else "空包弹"
    #
    #
    #     if user["energy_drink"] > 0:
    #         print(f"{user['name']}使用了能量饮料，{result}被退出")
    #         self.current_index += 1
    #         user["energy_drink"] -= 1
    #         return True
    #     else:
    #         print(f"{user['name']}没有能量饮料了！")
    #         return False
    def use_beer(self, user):
        inv = self._get_inventory(user)
        if self._count_item(inv, "beer") == 0:
            print(" 没有啤酒！")
            return False
        self._remove_item(inv, "beer")
        bullet=self.chamber[self.current_index]
        if self.current_index < len(self.chamber):
            # ★ 枪膛中还有子弹，退出当前这发
            self.current_index += 1  # ★ 跳过当前子弹，相当于指针后移
            print(f" {user['name']} 喝了啤酒，当前子弹：{'实弹' if bullet == 'real' else '空包弹'}被退出！")
        else:
            print(f" 枪膛已空，没有子弹可退。")
        return True
#########################################################################

    # def use_adrenaline(user,enemy):
    #     ask_item_map={
    #         "3":"transformer",
    #         "4":"cigarette",
    #         "5":"knife",
    #         "6":"magnifying_glass",
    #         "7":"phone",
    #         "8":"handcuffs",
    #         "9":"energy_drink",
    #         "11":"expired_medicine",
    #     }
    #
    #     if user["adrenaline"] > 0:
    #         print(f"{user['name']}使用了肾上腺素")
    #         ask=input("请选择想要拿走的对方道具（不能是肾上腺素），对应选择[3,9],{11}：")
    #         if ask in ask_item_map:
    #             item_key=ask_item_map[ask]
    #             Inventory.add(user,user[item_key])
    #             Inventory.remove(enemy,enemy[item_key])
    #             user["adrenaline"] -= 1
    #         else:
    #             print("非法操作")
    #
    #         return True
    #     else:
    #         print(f"{user['name']}没有肾上腺素了！")
    #         return False
    def use_adrenaline(self, user):
        inv = self._get_inventory(user)
        if self._count_item(inv, "adrenaline") == 0:
            print(" 没有肾上腺素！")
            return False

        if user["name"] == self.player["name"]:
            target_inv = self.devil_inventory
            target_name = self.devil["name"]
        else:
            target_inv = self.player_inventory
            target_name = self.player["name"]

        if not target_inv:
            print(" 对手没有道具可偷！")
            return False

        self._remove_item(inv, "adrenaline")

        stealable = [item for item in target_inv if item != "adrenaline"]
        if not stealable:
            print(" 对手只有肾上腺素，无法偷取！")
            return False

        stolen = random.choice(stealable)
        target_inv.remove(stolen)
        inv.append(stolen)
        print(f" {user['name']} 使用肾上腺素，偷了 {target_name} 的 {ITEM_NAMES.get(stolen, stolen)}！")
        return True



#########################################################################

    def use_expired_medicine(self,user):
        # k=random.randint(0,1)
        # if user["expired_medicine"] > 0:
        #     if k:
        #         user["hp"]+=2
        #         print(f"{user['name']}使用了过期药，回两滴血")
        #     else:
        #         user["hp"]-=1
        #         print(f"{user['name']}使用了过期药，扣一滴血")
        #     user["expired medicine"] -= 1
        #     return True
        # else:
        #     print(f"{user['name']}没有过期药了！")
        #     return False
        inv = self._get_inventory(user)
        if self._count_item(inv, "expired_medicine") == 0:
            print(" 没有过期药！")
            return False
        self._remove_item(inv, "expired_medicine")
        if random.random() < 0.5:
            user["hp"] = min(user["hp"] + 2, user.get("max_hp", 4))
            print(f" {user['name']} 吃了过期药，运气好！回复2点HP！(HP: {user['hp']})")
        else:
            user["hp"] -= 1
            print(f" {user['name']} 吃了过期药，中毒了！扣1点HP！(HP: {user['hp']})")
        return True
    # ==================== 恶魔 AI ====================

    def _devil_use_item(self, item_name):
        item_methods = {
            "phone": self.use_phone,
            "cigarette": self.use_cigarette,
            "expired_medicine": self.use_expired_medicine,
            "handcuffs": self.use_handcuffs,
            "knife": self.use_knife,
            "beer": self.use_beer,
            "magnifier": self.use_magnifier,
            "adrenaline": self.use_adrenaline,
            "inverter": self.use_inverter,
        }
        print(f"恶魔使用了 {ITEM_NAMES.get(item_name, item_name)}！")
        return item_methods[item_name](self.devil)

    def _devil_calculate_real_probability(self):
        """★ 恶魔计算剩余子弹中实弹的概率（基于已知信息）"""
        remaining = self.chamber[self.current_index:]
        known_real = self.current_round_shots.count("real")
        known_fake = self.current_round_shots.count("fake")

        total_remaining = len(remaining)
        if total_remaining == 0:
            return 0.0

        total_known_real = self.chamber.count("real")
        remaining_real = total_known_real - known_real
        if remaining_real < 0:
            remaining_real = 0

        return remaining_real / total_remaining

    def enemy_turn(self):
        """★ 恶魔的完整回合逻辑"""
        print(f"\n --- 恶魔的回合 ---")

        # ★ 检查：新回合开始，玩家先手
        if getattr(self, '_new_round_player_first', False):
            self._new_round_player_first = False
            print(" 新的一轮，玩家先手！")
            return "continue"

        # ★ 检查恶魔是否被手铐铐住
        if self.devil_skip:
            print(" 恶魔被手铐铐住，跳过回合！")
            self.devil_skip = False
            return "continue"

        # 阶段1：烟和过期药无论如何都要用，用完为止
        while self._count_item(self.devil_inventory, "cigarette") > 0:
            self._devil_use_item("cigarette")
        while self._count_item(self.devil_inventory, "expired_medicine") > 0:
            self._devil_use_item("expired_medicine")

        # 阶段2：肾上腺素 → 偷对手道具
        if self._count_item(self.devil_inventory, "adrenaline") > 0:
            steal_priority = ["cigarette", "expired_medicine", "handcuffs", "knife"]
            player_has = False
            for item in steal_priority:
                if item in self.player_inventory:
                    player_has = True
                    break
            if player_has or self.player_inventory:
                self._devil_use_item("adrenaline")

        # 阶段3：手铐直接用
        if self._count_item(self.devil_inventory, "handcuffs") > 0:
            if not self.handcuffs_used_this_round:
                self._devil_use_item("handcuffs")

        # 阶段4：概率计算 + 决定打谁
        prob = self._devil_calculate_real_probability()
        # ★ 不输出概率

        if prob > 0.5:
            # 实弹概率高 → 打玩家，有刀就先用刀
            target = self.player
            print(f" 恶魔决定攻击玩家！")
            if self._count_item(self.devil_inventory, "knife") > 0 and not self.knife_active:
                self._devil_use_item("knife")
        else:
            # 实弹概率低 → 有转换器就用转换器然后打玩家，否则打自己
            if self._count_item(self.devil_inventory, "inverter") > 0:
                self._devil_use_item("inverter")
                target = self.player
                print(f" 恶魔使用转换器后攻击玩家！")
            else:
                target = self.devil
                print(f" 恶魔朝自己开枪！")

        # 执行攻击
        dead, keep_turn, round_ended = self._attack_target(target, self.devil["name"])

        if round_ended:
            # ★ 子弹打完，新回合开始，不显示状态（等玩家回合再显示）
            return "continue"

        # ★ 只在非子弹打完情况下显示状态
        self._show_status()

        if dead:
            if target["name"] == self.player["name"]:
                print(" 玩家被恶魔击杀！")
                return "lose"
            else:
                print(" 恶魔自杀了！")
                return "win"

        # ★ 如果保持回合（空包弹打自己），恶魔继续
        if keep_turn:
            print(" 恶魔的回合继续！")
            return self.enemy_turn()

        return "continue"
        # ==================== 玩家回合 ====================

    def _show_inventory(self, inventory):
        if not inventory:
            return "无"
        result = []
        for item in self.all_items:
            count = inventory.count(item)
            if count > 0:
                result.append(f"{ITEM_NAMES.get(item, item)}×{count}")
        return " | ".join(result) if result else "无"

    def _show_status(self):
        """★ 显示双方状态"""
        print(f"\n{'=' * 40}")
        print(f" {self.player['name']}: HP {self.player['hp']}/{self.player.get('max_hp', 4)}")
        print(f"   道具: {self._show_inventory(self.player_inventory)}")
        print(f" {self.devil['name']}: HP {self.devil['hp']}/{self.devil.get('max_hp', 4)}")
        print(f"   道具: {self._show_inventory(self.devil_inventory)}")
        remaining = len(self.chamber) - self.current_index
        print(f" 剩余子弹: {remaining} 发")
        if self.knife_active:
            print(f"已使用刀，伤害翻倍")
        print(f"{'=' * 40}")

    def combat_round(self, user, enemy):
        """
        ★ 玩家回合
        """
        # ★ 检查玩家是否被手铐铐住
        if self.player_skip:
            print(" 你被手铐铐住了！跳过回合。")
            self.player_skip = False
            return "continue"

        self._show_status()

        print("\n 你的回合：")
        print("  1. 对对手开枪")
        print("  2. 对自己开枪")
        print("  3. 使用道具")
        print("  4. 逃跑")

        choice = input("请选择 (1-4): ").strip()

        if choice == "1":
            dead, keep_turn, round_ended = self._attack_target(enemy, user["name"])
            if round_ended:
                return "continue"
            self._show_status()
            if dead:
                print(f"你击杀了 {enemy['name']}！")
                return "win"
            return "continue"

        elif choice == "2":
            dead, keep_turn, round_ended = self._attack_target(user, user["name"])
            if round_ended:
                return "continue"
            self._show_status()
            if dead:
                print(" 你自杀了...")
                return "lose"
            if keep_turn:
                print(" 你获得额外回合！")
                return self.combat_round(user, enemy)
            return "continue"

        elif choice == "3":
            return self._player_use_item(user, enemy)

        elif choice == "4":
            print(" 你逃跑了！")
            return "flee"
        else:
            print(" 无效选择")
            return self.combat_round(user, enemy)

    def _player_use_item(self, user, enemy):
        print("\n 你的道具栏：")
        items_display = []
        idx = 1
        item_map = {}
        for item in self.all_items:
            count = self._count_item(self.player_inventory, item)
            if count > 0:
                items_display.append(f"{idx}. {ITEM_NAMES.get(item, item)} ×{count}")
                item_map[str(idx)] = item
                idx += 1

        if not items_display:
            print("  (空)")
            print("按回车返回...")
            input()
            return self.combat_round(user, enemy)

        for d in items_display:
            print(f"  {d}")
        print(f"  {idx}. 返回")

        item_choice = input(f"请选择道具 (1-{idx}): ").strip()

        if item_choice == str(idx):
            return self.combat_round(user, enemy)

        item_name = item_map.get(item_choice)
        if not item_name:
            print(" 无效选择")
            return self._player_use_item(user, enemy)

        item_methods = {
            "phone": self.use_phone,
            "cigarette": self.use_cigarette,
            "expired_medicine": self.use_expired_medicine,
            "handcuffs": self.use_handcuffs,
            "knife": self.use_knife,
            "beer": self.use_beer,
            "magnifier": self.use_magnifier,
            "adrenaline": self.use_adrenaline,
            "inverter": self.use_inverter,
        }
        success = item_methods[item_name](user)
        if success:
            return self.combat_round(user, enemy)
        else:
            return self._player_use_item(user, enemy)

    # def combat_round(self, user,enemy):
    #     print(f"\n{'=' * 50}")
    #     print(f"第{self.round_count}回合")
    #     print(f"敌人HP：{enemy['hp']}/{enemy['max_hp']}")
    #
    #     choice = self.get_player_choice()
    #
    #     # if choice==1:
    #     #     enemy_defeated=self.player_attack(enemy)
    #     #     if enemy_defeated:
    #     #         return "win"
    #     if choice == 1:
    #         enemy_defeated = self.player_attack(enemy, use_knife=True)
    #         if enemy_defeated:
    #             return "win"
    #     elif choice == 2:
    #         player_die=self.player_self_attack(user,use_knife=True)
    #         if player_die:
    #             return "lose"
    #
    #     elif choice == 3:
    #         if not self.use_energy_drink(user):
    #             return "continue"
    #
    #     elif choice == 4:
    #         if not self.use_cigarette(user):
    #             return "continue"
    #
    #     elif choice == 5:
    #         if not self.use_knife(user):
    #             return "continue"
    #
    #     elif choice == 6:
    #         if not self.use_magnifying_glass(user):
    #             return "continue"
    #
    #     elif choice == 7:
    #         if not self.use_phone(user):
    #             return "continue"
    #
    #     elif choice == 8:
    #         if not self.use_handcuffs(user):
    #             return "continue"
    #
    #     elif choice == 9:
    #         if not self.use_energy_drink(user):
    #             return "continue"
    #
    #     elif choice == 10:
    #         if not self.use_adrenaline(user):
    #             return "continue"
    #
    #     elif choice == 11:
    #         if not self.use_expired_medicine(user):
    #             return "continue"
    #
    #     elif choice == 12:
    #        return "flee"
    #
    #     else:
    #         print("非法输入")
    #         return "continue"

      #  if enemy["hp"]>0 and choice in [1,2]:


#
#     def run(self,player,devil):
#         print(" 欢迎来到文字冒险游戏！")
#         self.player["name"] = input("请输入你的角色名: ")
#
#         print(f"\n勇敢的 {self.player['name']}，冒险开始了！")
#         self.show_status()
#
#         while True:
#             self.round_count += 1
#
#             while devil["hp"]>0:
#                 result=self.combat_round(devil)
#                 if result == "win":
#                     print("胜利")
#                     break
#                 elif result in ["flee","lose"]:
#                     return result
#                 elif result == "continue":
#                     continue
#
#             if self.player["hp"]<=0:
#                 print(f"\n游戏结束！你坚持了{self.combat_round}个回合")
#                 break
#
#             time.sleep(1)
#
#             if self.round_count > 0:
#                 cont = input("\n继续下一回合？(y/n): ").lower()
#                 if cont != 'y':
#                     print(f"\n感谢游玩！最终回合数: {self.round_count}")
#                     break
#
# if __name__ == "__main__":
#     game=InteractiveTextGame()
#     game.run()
#
#     # ==================== 主循环 ====================

    def run(self):
        """★ 游戏主循环"""
        print("🎮 欢迎来到恶魔轮盘赌！")
        self.player["name"] = input("请输入你的角色名: ").strip()
        print(f"\n勇敢的 {self.player['name']}，冒险开始了！")
        print(f"双方初始血量{self.player['hp']}")

        while True:
            self.round_count += 1
            self._load_chamber()
            self._show_round_info()

            while self.player["hp"] > 0 and self.devil["hp"] > 0:
                # ★ 重置新回合标记，确保玩家先手
                self._new_round_player_first = False

                result = self.combat_round(self.player, self.devil)
                if result in ["win", "lose", "flee"]:
                    self._end_game(result)
                    return

                if self.devil["hp"] > 0 and self.player["hp"] > 0:
                    result = self.enemy_turn()
                    if result in ["win", "lose"]:
                        self._end_game(result)
                        return

            if self.player["hp"] <= 0:
                break
            if self.devil["hp"] <= 0:
                print(f"\n 你击败了恶魔！")
                self.devil["hp"] = self.devil["max_hp"]
                print(f"👿 恶魔复活了！准备下一轮...")

            cont = input("\n继续下一回合？(y/n): ").lower()
            if cont != 'y':
                print(f"\n感谢游玩！最终回合数: {self.round_count}")
                break

    def _end_game(self, result):
        if result == "win":
            print(f"\n 恭喜 {self.player['name']}！你战胜了恶魔！")
        elif result == "lose":
            print(f"\n {self.player['name']} 被恶魔击败了...")
        elif result == "flee":
            print(f"\n {self.player['name']} 逃跑了！")
        print(f" 总共进行了 {self.round_count} 轮")


if __name__ == "__main__":
    player_data = {"name": "", "hp": 4, "max_hp": 4}
    game = InteractiveTextGame(player_data)
    game.run()

