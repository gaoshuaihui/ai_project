class Character:
    """角色基类"""

    def __init__(self, name, health, attack_power):
        """
        初始化角色
        :param name: 角色名称
        :param health: 生命值
        :param attack_power: 攻击力
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        """
        判断角色是否存活
        :return: True表示存活，False表示已死亡
        """
        return self.health > 0

    def attack(self, target):
        """
        攻击目标
        :param target: 被攻击的目标（Character对象）
        """
        if not self.is_alive():
            print(f"{self.name} 已经死亡，无法攻击")
            return

        if not target.is_alive():
            print(f"{target.name} 已经死亡，无需攻击")
            return

        damage = self.attack_power
        target.health -= damage
        print(f"{self.name} 攻击 {target.name}，造成 {damage} 点伤害")

        if not target.is_alive():
            print(f"{target.name} 被击败！")




class Warrior(Character):
    """战士类，继承自Character"""

    def __init__(self, name, health, attack_power, armor):
        """
        初始化战士
        :param name: 战士名称
        :param health: 生命值
        :param attack_power: 攻击力
        :param armor: 护甲值
        """
        super().__init__(name, health, attack_power)
        self.armor = armor

    def attack(self, target):
        """
        重写攻击方法，造成额外物理伤害
        :param target: 被攻击的目标
        """
        if not self.is_alive():
            print(f"{self.name} 已经死亡，无法攻击")
            return

        if not target.is_alive():
            print(f"{target.name} 已经死亡，无需攻击")
            return

        # 战士攻击造成额外伤害（攻击力 + 护甲值）
        damage = self.attack_power + self.armor
        target.health -= damage
        print(f"{self.name}（战士）使用重击攻击 {target.name}，造成 {damage} 点物理伤害")

        if not target.is_alive():
            print(f"{target.name} 被击败！")


class Mage(Character):
    """法师类，继承自Character"""

    def __init__(self, name, health, attack_power, mana):
        """
        初始化法师
        :param name: 法师名称
        :param health: 生命值
        :param attack_power: 攻击力
        :param mana: 法力值
        """
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, target):
        """
        重写攻击方法，普通攻击
        :param target: 被攻击的目标
        """
        if not self.is_alive():
            print(f"{self.name} 已经死亡，无法攻击")
            return

        if not target.is_alive():
            print(f"{target.name} 已经死亡，无需攻击")
            return

        damage = self.attack_power
        target.health -= damage
        print(f"{self.name}（法师）施放魔法攻击 {target.name}，造成 {damage} 点伤害")

        if not target.is_alive():
            print(f"{target.name} 被击败！")

    def fireball(self, target):
        """
        法师特有技能：火球术
        :param target: 被攻击的目标
        """
        if not self.is_alive():
            print(f"{self.name} 已经死亡，无法施法")
            return

        if not target.is_alive():
            print(f"{target.name} 已经死亡，无需施法")
            return

        if self.mana < 10:
            print(f"{self.name} 法力不足，无法施放火球术")
            return

        # 火球术造成双倍伤害
        damage = self.attack_power * 2
        target.health -= damage
        self.mana -= 10
        print(f"{self.name}（法师）施放火球术攻击 {target.name}，造成 {damage} 点火焰伤害，消耗10点法力")

        if not target.is_alive():
            print(f"{target.name} 被击败！")


# 使用示例
if __name__ == "__main__":
    # 创建角色
    warrior = Warrior("战士阿强", 150, 20, 10)
    mage = Mage("法师小美", 100, 15, 50)
    enemy = Character("怪物", 80, 10)

    print("=== 游戏开始 ===")

    # 战士攻击
    warrior.attack(enemy)
    print(f"敌人剩余生命值: {enemy.health}")

    # 法师普通攻击
    mage.attack(enemy)
    print(f"敌人剩余生命值: {enemy.health}")

    # 法师使用火球术
    mage.fireball(enemy)
    print(f"敌人剩余生命值: {enemy.health}")
    print(f"法师剩余法力值: {mage.mana}")