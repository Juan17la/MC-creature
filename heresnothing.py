SpecialAbility.objects.bulk_create([
    SpecialAbility(name='Decay', level_power=9, race=Race.objects.get(name='Zombie')),
    SpecialAbility(name='Hungry', level_power=5, race=Race.objects.get(name='Zombie')),
    SpecialAbility(name='Poisonness', level_power=8, race=Race.objects.get(name='Zombie')),

    SpecialAbility(name='Invisibility', level_power=5, race=Race.objects.get(name='Spider')),
    SpecialAbility(name='Division', level_power=9, race=Race.objects.get(name='Spider')),
    SpecialAbility(name='Acid Spit', level_power=8, race=Race.objects.get(name='Spider')),

    SpecialAbility(name='BigBang', level_power=10, race=Race.objects.get(name='Creeper')),
    SpecialAbility(name='Launcher', level_power=8, race=Race.objects.get(name='Creeper')),
    SpecialAbility(name='Dimintute Dinamite', level_power=6, race=Race.objects.get(name='Creeper')),

    SpecialAbility(name='Sharp Bones', level_power=6, race=Race.objects.get(name='Skeleton')),
    SpecialAbility(name='Bone Needles', level_power=7, race=Race.objects.get(name='Skeleton')),
    SpecialAbility(name='Calcium Armor', level_power=8, race=Race.objects.get(name='Skeleton')),

    SpecialAbility(name='Creature Tamer', level_power=10, race=Race.objects.get(name='Human')),
    SpecialAbility(name='X-ray', level_power=6, race=Race.objects.get(name='Human')),
    SpecialAbility(name='Lightning Control', level_power=8, race=Race.objects.get(name='Human')),

    SpecialAbility(name='Infinite God Carrot', level_power=10, race=Race.objects.get(name='Pig')),
    SpecialAbility(name='Herobrine Corruption', level_power=10, race=Race.objects.get(name='Pig')),

    SpecialAbility(name='Clonatioln', level_power=8, race=Race.objects.get(name='Enderman')),
    SpecialAbility(name='Endermans breath', level_power=6, race=Race.objects.get(name='Enderman')),
    SpecialAbility(name='Ingenuity', level_power=9, race=Race.objects.get(name='Enderman')),
])


Race.objects.bulk_create([
    Race(name='Zombie'),
    Race(name='Skeleton'),
    Race(name='Human'),
    Race(name='Enderman'),
    Race(name='Creeper'),
    Race(name='Spider'),
    Race(name='Pig')
])