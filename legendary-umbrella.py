import random


def main():
    player_max_hp = 100
    player_hp = player_max_hp

    # Pick a storm monster to be this game's boss.
    boss_name = random.choice(["Cumulus Beast", "Acid Drop"])
    boss_max_hp = 100
    boss_hp = boss_max_hp

    print("=" * 48)
    print("  LEGENDARY UMBRELLA: THE ACID RAIN ODYSSEY")
    print("=" * 48)
    print(f"\nA storm rolls in... The {boss_name} blocks your path!")
    print("Raise your Legendary Umbrella and prepare for battle.\n")

    # Continue taking turns until either the hero or the boss runs out of HP.
    while player_hp > 0 and boss_hp > 0:
        print("-" * 48)
        print(f"Your HP:       {player_hp}/{player_max_hp}")
        print(f"{boss_name} HP: {boss_hp}/{boss_max_hp}")
        print("\n[A] Umbrella Bash")
        print("[B] Open Canopy")
        print("[C] Glide / Evade")

        choice = input("\nChoose your move: ").strip().upper()

        if choice == "A":
            damage = random.randint(12, 24)
            boss_hp = max(0, boss_hp - damage)
            print(
                f"\nYou whirl the Legendary Umbrella like a mighty club "
                f"and bash the {boss_name} for {damage} damage!"
            )

        elif choice == "B":
            print(
                "\nYou open the canopy just in time! "
                "The Legendary Umbrella braces against the coming storm."
            )

        elif choice == "C":
            print("\nYou spring into the air and try to glide clear of danger!")

        else:
            print("\nPlease enter A, B, or C.")
            continue

        # End the fight immediately if the hero's attack defeated the boss.
        if boss_hp == 0:
            break

        monster_damage = random.randint(10, 20)
        print(f"\nThe {boss_name} unleashes a furious burst of acid rain!")

        if choice == "B":
            # The canopy blocks 80% of this incoming attack.
            blocked_damage = int(monster_damage * 0.80)
            damage_taken = monster_damage - blocked_damage
            player_hp = max(0, player_hp - damage_taken)
            print(
                "The acid splashes across the legendary fabric! "
                f"Your canopy blocks {blocked_damage} damage, "
                f"but {damage_taken} gets through."
            )

        elif choice == "C":
            if random.random() < 0.5:
                damage_taken = 0
                print(
                    "You catch a gust of wind and glide clear! "
                    "The acid rain hisses against the ground behind you."
                )
            else:
                damage_taken = monster_damage
                player_hp = max(0, player_hp - damage_taken)
                print(
                    "Your glide falters in the heavy rain! "
                    f"The storm hits you for {damage_taken} damage."
                )

        else:
            damage_taken = monster_damage
            player_hp = max(0, player_hp - damage_taken)
            print(
                f"The storm catches you off guard and hits for "
                f"{damage_taken} damage!"
            )

    print("\n" + "=" * 48)
    if player_hp == 0:
        print("GAME OVER — The storm has overwhelmed you.")
        print("Your Legendary Umbrella falls silent beneath the rain.")
    else:
        print(f"VICTORY — You defeated the {boss_name}!")
        print("The clouds part, and your Legendary Umbrella shines once more.")
    print("=" * 48)


if __name__ == "__main__":
    main()
