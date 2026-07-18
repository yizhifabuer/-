import random
import time
import os

# ★ 新增：道具名称到中文的映射（恶魔AI输出用）
ITEM_NAMES = {
    "phone": "手机", "cigarette": "香烟", "expired_medicine": "过期药",
    "handcuffs": "手铐", "knife": "刀", "beer": "啤酒",
    "magnifier": "放大镜", "adrenaline": "肾上腺素", "inverter": "转换器"
}

class InteractiveTextGame:
    def __init__(self, player):
        self.player = player
        hp=random.randint(2, 5)
        self.player["hp"] = hp
        self.devil = {"name": "恶魔", "hp": hp, "max_hp": hp}

        self.all_items = [
            "phone", "cigarette", "expired_medicine",
            "handcuffs", "knife", "beer",
            "magnifier", "adrenaline", "inverter"
        ]
        self.player_inventory = []
        self.devil_inventory = []

        self.chamber = []
        self.current_index = 0

        self.knife_active = False
        self.handcuffs_used_this_round = False
        # ★ 修改：手铐效果改为跳过"对方"回合
        self.player_skip = False    # 玩家被铐，跳过玩家回合
        self.devil_skip = False     # 恶魔被铐，跳过恶魔回合
        self.current_round_shots = []
        self._new_round_player_first = False  # ★ 新回合玩家先手标记

        self.round_count = 0

    # ==================== 道具辅助方法 ====================

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
        total = random.randint(2, 8)
        real_count = total // 2
        fake_count = total - real_count
        bullets = ["real"] * real_count + ["fake"] * fake_count
        random.shuffle(bullets)
        self.chamber = bullets
        self.current_index = 0
        self.current_round_shots = []

        self.player_inventory = []
        self.devil_inventory = []
        draw = random.randint(2, 4)
        for _ in range(draw):
            self.player_inventory.append(random.choice(self.all_items))
            self.devil_inventory.append(random.choice(self.all_items))

        self.handcuffs_used_this_round = False
        self.player_skip = False   # ★ 重置
        self.devil_skip = False    # ★ 重置
        self.knife_active = False
        self._new_round_player_first = True  # ★ 标记新回合玩家先手

    def _show_round_info(self):
        real = self.chamber.count("real")
        fake = self.chamber.count("fake")
        total = len(self.chamber)
        print(f"\n{'='*40}")
        print(f" 第 {self.round_count} 轮！枪膛共 {total} 发子弹：{real} 真 / {fake} 假")
        print(f"{'='*40}")

    def fire(self):
        """★ 开枪，返回子弹类型。子弹打完返回 None。"""
        if self.current_index >= len(self.chamber):
            self._load_chamber()
            self._show_round_info()
            return None  # ★ 返回 None 表示子弹打完
        bullet = self.chamber[self.current_index]
        self.current_index += 1
        self.knife_active = False  # 子弹打出后刀失效
        return bullet

    def _attack_target(self, target, attacker_name):
        """
        ★ 攻击目标，返回 (目标是否死亡, 是否保持回合, 是否子弹打完)
        保持回合条件：空包弹 + 打自己
        """
        bullet = self.fire()
        if bullet is None:
            # ★ 子弹打完，新回合开始
            return (False, False, True)

        name = target["name"]
        damage = 2 if self.knife_active else 1

        if bullet == "real":
            target["hp"] -= damage
            if damage == 2:
                print(f" 实弹！{name} 受到 {damage} 点伤害（刀伤翻倍）！(剩余HP: {target['hp']})")
            else:
                print(f" 实弹！{name} 受到 {damage} 点伤害！(剩余HP: {target['hp']})")
            self.knife_active = False
            return (target["hp"] <= 0, False, False)
        else:
            print(f" 空包弹！")
            self.knife_active = False
            # ★ 核心规则：空包弹打自己 → 保持回合
            if target["name"] == attacker_name:
                print(" 空包弹打自己，回合继续！")
                return (target["hp"] <= 0, True, False)
            return (False, False, False)

    # ==================== 道具使用方法 ====================

    def use_phone(self, user):
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

    def use_cigarette(self, user):
        inv = self._get_inventory(user)
        if self._count_item(inv, "cigarette") == 0:
            print(" 没有香烟！")
            return False
        self._remove_item(inv, "cigarette")
        user["hp"] = min(user["hp"] + 1, user.get("max_hp", 4))
        print(f" {user['name']} 抽了根烟，回复1点HP！(HP: {user['hp']})")
        return True

    def use_expired_medicine(self, user):
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

    def use_handcuffs(self, user):
        """
        ★ 手铐：对方下一回合无法行动。每回合限用一次。
        """
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
            print(f"🔗 {user['name']} 使用了手铐！恶魔下回合将被跳过！")
        else:
            self.player_skip = True
            print(f"🔗 {user['name']} 使用了手铐！玩家下回合将被跳过！")

        self.handcuffs_used_this_round = True
        return True

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

    # def use_beer(self, user):
    #     inv = self._get_inventory(user)
    #     if self._count_item(inv, "beer") == 0:
    #         print("❌ 没有啤酒！")
    #         return False
    #     self._remove_item(inv, "beer")
    #     if self.current_index > 0:
    #         self.current_index -= 1
    #         print(f"🍺 {user['name']} 喝了啤酒，当前子弹被退出！")
    #     else:
    #         print(f"🍺 没有子弹可退。")
    #     return True

    def use_beer(self, user):
        inv = self._get_inventory(user)
        if self._count_item(inv, "beer") == 0:
            print(" 没有啤酒！")
            return False
        self._remove_item(inv, "beer")
        if self.current_index < len(self.chamber):
            # ★ 枪膛中还有子弹，退出当前这发
            self.current_index += 1  # ★ 跳过当前子弹，相当于指针后移
            print(f" {user['name']} 喝了啤酒，当前子弹被退出！")
        else:
            print(f" 枪膛已空，没有子弹可退。")
        return True

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
        print(f"👿 恶魔使用了 {ITEM_NAMES.get(item_name, item_name)}！")
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
        print(f"\n👿 --- 恶魔的回合 ---")

        # ★ 检查：新回合开始，玩家先手
        if getattr(self, '_new_round_player_first', False):
            self._new_round_player_first = False
            print(" 新的一轮，玩家先手！")
            return "continue"

        # ★ 检查恶魔是否被手铐铐住
        if self.devil_skip:
            print("🔗 恶魔被手铐铐住，跳过回合！")
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
            print(f"👿 恶魔决定攻击玩家！")
            if self._count_item(self.devil_inventory, "knife") > 0 and not self.knife_active:
                self._devil_use_item("knife")
        else:
            # 实弹概率低 → 有转换器就用转换器然后打玩家，否则打自己
            if self._count_item(self.devil_inventory, "inverter") > 0:
                self._devil_use_item("inverter")
                target = self.player
                print(f"👿 恶魔使用转换器后攻击玩家！")
            else:
                target = self.devil
                print(f"👿 恶魔朝自己开枪！")

        # 执行攻击
        dead, keep_turn, round_ended = self._attack_target(target, self.devil["name"])

        if round_ended:
            # ★ 子弹打完，新回合开始，不显示状态（等玩家回合再显示）
            return "continue"

        # ★ 只在非子弹打完情况下显示状态
        self._show_status()

        if dead:
            if target["name"] == self.player["name"]:
                print("💀 玩家被恶魔击杀！")
                return "lose"
            else:
                print(" 恶魔自杀了！")
                return "win"

        # ★ 如果保持回合（空包弹打自己），恶魔继续
        if keep_turn:
            print("👿 恶魔的回合继续！")
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
        print(f"\n{'='*40}")
        print(f" {self.player['name']}: HP {self.player['hp']}/{self.player.get('max_hp', 4)}")
        print(f"   道具: {self._show_inventory(self.player_inventory)}")
        print(f"👿 {self.devil['name']}: HP {self.devil['hp']}/{self.devil.get('max_hp', 4)}")
        print(f"   道具: {self._show_inventory(self.devil_inventory)}")
        remaining = len(self.chamber) - self.current_index
        print(f" 剩余子弹: {remaining} 发")
        if self.knife_active:
            print(f"已使用刀，伤害翻倍")
        print(f"{'='*40}")

    def combat_round(self, user, enemy):
        """
        ★ 玩家回合
        """
        # ★ 检查玩家是否被手铐铐住
        if self.player_skip:
            print("🔗 你被手铐铐住了！跳过回合。")
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
                print("💀 你自杀了...")
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

    # ==================== 主循环 ====================

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