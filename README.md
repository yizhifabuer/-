# -纯文字恶魔轮盘赌
```mermaid
flowchart LR
    RUN["run()"] --> COMBAT["combat_round()"]
    RUN --> ENEMY["enemy_turn()"]
    RUN --> LOAD["_load_chamber()"]
    
    COMBAT --> ATTACK["_attack_target()"]
    COMBAT --> PITEM["_player_use_item()"]
    COMBAT --> STATUS["_show_status()"]
    
    ENEMY --> ATTACK
    ENEMY --> DITEM["_devil_use_item()"]
    ENEMY --> PROB["_calculate_prob()"]
    
    ATTACK --> FIRE["fire()"]
    FIRE --> LOAD
    
    PITEM --> ITEMS["道具方法 x9"]
    DITEM --> ITEMS
    
    ITEMS --> INV["_get_inventory()"]
    ITEMS --> REMOVE["_remove_item()"]
    
    LOAD --> CHAMBER["chamber[]"]
    LOAD --> FLAGS["状态标记重置"]
    
    ATTACK --> RESULT{"返回三元组<br/>dead, keep_turn, round_ended"}
    RESULT --> COMBAT
    RESULT --> ENEMY

```


```mermaid
flowchart TB
    RUN["🎮 run() 主循环"] --> LOAD["_load_chamber()<br/>装弹 + 发道具 + 设先手"]
    LOAD --> INFO["_show_round_info()"]
    INFO --> RESET["重置 _new_round_player_first"]
    
    RESET --> PLAYER["👤 combat_round()<br/>玩家回合"]
    PLAYER --> PCHECK{"检查 player_skip?"}
    PCHECK -- "被铐跳过" --> DEVIL
    PCHECK -- "正常" --> PMENU["菜单: ①打对手 ②打自己 ③道具 ④逃跑"]
    
    PMENU --> ATTACK["_attack_target()"]
    ATTACK --> FIRE["fire()"]
    FIRE --> FCHECK{"子弹?"}
    FCHECK -- "None" --> LOAD
    FCHECK -- "实弹" --> DAMAGE["扣血<br/>刀=伤害×2"]
    FCHECK -- "空包弹" --> SELFT{"打自己?"}
    SELFT -- "是" --> KEEP["保持回合<br/>继续操作"]
    SELFT -- "否" --> DEVIL
    
    PLAYER --> ITEMS["💊 道具方法"]
    ITEMS --> PLAYER
    
    DEVIL["👿 enemy_turn()<br/>恶魔回合"] --> DCHECK1{"检查新回合标记?"}
    DCHECK1 -- "玩家先手" --> PLAYER
    DCHECK1 -- "正常" --> DCHECK2{"检查 devil_skip?"}
    DCHECK2 -- "被铐跳过" --> PLAYER
    DCHECK2 -- "正常" --> DAI
    
    DAI["AI决策"] --> DPHASE1["阶段1: 回血道具"]
    DPHASE1 --> DPHASE2["阶段2: 偷道具"]
    DPHASE2 --> DPHASE3["阶段3: 手铐"]
    DPHASE3 --> DPHASE4["阶段4: 概率决策"]
    DPHASE4 --> ATTACK
    
    DEVIL --> DONE{"结果?"}
    DONE -- "玩家死亡" --> END["_end_game()"]
    DONE -- "恶魔死亡" --> REVIVE["复活询问"]
    DONE -- "继续" --> RESET

```
```mermaid
flowchart LR
    RUN["run()"] --> COMBAT["combat_round()"]
    RUN --> ENEMY["enemy_turn()"]
    RUN --> LOAD["_load_chamber()"]
    
    COMBAT --> ATTACK["_attack_target()"]
    COMBAT --> PITEM["_player_use_item()"]
    COMBAT --> STATUS["_show_status()"]
    
    ENEMY --> ATTACK
    ENEMY --> DITEM["_devil_use_item()"]
    ENEMY --> PROB["_calculate_prob()"]
    
    ATTACK --> FIRE["fire()"]
    FIRE --> LOAD
    
    PITEM --> ITEMS["道具方法 x9"]
    DITEM --> ITEMS
    
    ITEMS --> INV["_get_inventory()"]
    ITEMS --> REMOVE["_remove_item()"]
    
    LOAD --> CHAMBER["chamber[]"]
    LOAD --> FLAGS["状态标记重置"]
    
    ATTACK --> RESULT{"返回三元组<br/>dead, keep_turn, round_ended"}
    RESULT --> COMBAT
    RESULT --> ENEMY

```
赛博小垃圾，本来打算全部自己写的，最后一些功能有想法但是不会实现，还是用到了ai，还是存在对象混淆不清，多余类之类一系列问题
学到的东西：1.在写代码前整体的架构其实更为重要，我总是想不全，等要用手机和啤酒的时候再想到枪膛，在要用肾上腺素的时候才想到物品栏，这样思路不是顺的，会来回往返，之前也没有经验。因此应该在写之前完完整整的描述自己所需要的所有功能，先画出这个思维导图，然后会看的更清晰
           2.很多ai新创建的变量和函数，只是正常的用法，但是我还是想不到，比如 _devil_calculate_real_probability，对恶魔计数只有模糊的认识，看过结果之后其实不复杂，但归根结底问题的关键还是自己想出来
