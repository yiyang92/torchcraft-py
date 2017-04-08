"""Protocol definitions for communicating with the TorchCraft server."""

VERSION = '16'


# Build reverted index
def _build_index(t):
    tmp = []
    for k, v in t.items():
        tmp.append(k)
    for k in tmp:
        t[t[k]] = k


# All available commands
commands = {
    # No arguments
    'quit': 0,  # Leave the game
    'restart': 1,  # Restart the game. Doesn't work in multi-player.
    'map_hack': 2,  # Remove fog of war
    'request_image': 3,
    'exit_process': 4,
    'noop': 5,  # Do nothing

    # One argument
    'set_speed': 6,  # Sets the game speed (integer)
    'set_log': 7,  # Activates logging (boolean)
    'set_gui': 8,  # Activates drawing and text in SC (boolean)
    'set_frameskip': 9,  # Number of frames to skip (integer)
    'set_cmd_optim': 10,  # Reduce bot APM (0-6)
    'set_combine_frames': 11,  # Combine n frames before sending (integer)

    # Sets the map with BWAPI->setMap and by writing to the config. Is not
    # thread-safe. However, as long as the next connect finishes after
    # set_map, you are guaranteed the map will be what you want.
    'set_map': 12,
    'set_multi': 13,

    # Arguments: (unit ID, command, target id, target x, target y, extra)
    # (x, y) are walktiles instead of pixels
    # otherwise this corresponds exactly to BWAPI::UnitCommand
    'command_unit': 14,
    'command_unit_protected': 15,

    # Arguments: (command, args)
    # For documentation about args, see user_command_types
    'command_user': 16,

    'MAX': 17
}
_build_index(commands)

user_command_types = {
    # One arg
    'Move_Screen_Up': 0,  # Arguments: magnitude (amount of pixels)
    'Move_Screen_Down': 1,  # Arguments: magnitude (amount of pixels)
    'Move_Screen_Left': 2,  # Arguments: magnitude (amount of pixels)
    'Move_Screen_Right': 3,  # Arguments: magnitude (amount of pixels)

    # Two args
    'Move_Screen_To_Pos': 4,  # Arguments: (x, y)
    'Right_Click': 5,  # Arguments: (x, y)

    'MAX': 7
}
_build_index(user_command_types)

# Corresponds to BWAPI::UnitCommandTypes::Enum
unit_command_types = {
    'Attack_Move': 0,
    'Attack_Unit': 1,
    'Build': 2,
    'Build_Addon': 3,
    'Train': 4,
    'Morph': 5,
    'Research': 6,
    'Upgrade': 7,
    'Set_Rally_Position': 8,
    'Set_Rally_Unit': 9,
    'Move': 10,
    'Patrol': 11,
    'Hold_Position': 12,
    'Stop': 13,
    'Follow': 14,
    'Gather': 15,
    'Return_Cargo': 16,
    'Repair': 17,
    'Burrow': 18,
    'Unburrow': 19,
    'Cloak': 20,
    'Decloak': 21,
    'Siege': 22,
    'Unsiege': 23,
    'Lift': 24,
    'Land': 25,
    'Load': 26,
    'Unload': 27,
    'Unload_All': 28,
    'Unload_All_Position': 29,
    'Right_Click_Position': 30,
    'Right_Click_Unit': 31,
    'Halt_Construction': 32,
    'Cancel_Construction': 33,
    'Cancel_Addon': 34,
    'Cancel_Train': 35,
    'Cancel_Train_Slot': 36,
    'Cancel_Morph': 37,
    'Cancel_Research': 38,
    'Cancel_Upgrade': 39,
    'Use_Tech': 40,
    'Use_Tech_Position': 41,
    'Use_Tech_Unit': 42,
    'Place_COP': 43,
    'None': 44,
    'Unknown': 45,
    'MAX': 46
}
_build_index(unit_command_types)

# Corresponds to BWAPI::Orders::Enum
orders = {
    'Die': 0,
    'Stop': 1,
    'Guard': 2,
    'PlayerGuard': 3,
    'TurretGuard': 4,
    'BunkerGuard': 5,
    'Move': 6,
    'ReaverStop': 7,
    'Attack1': 8,
    'Attack2': 9,
    'AttackUnit': 10,
    'AttackFixedRange': 11,
    'AttackTile': 12,
    'Hover': 13,
    'AttackMove': 14,
    'InfestedCommandCenter': 15,
    'UnusedNothing': 16,
    'UnusedPowerup': 17,
    'TowerGuard': 18,
    'TowerAttack': 19,
    'VultureMine': 20,
    'StayInRange': 21,
    'TurretAttack': 22,
    'Nothing': 23,
    'Unused_24': 24,
    'DroneStartBuild': 25,
    'DroneBuild': 26,
    'CastInfestation': 27,
    'MoveToInfest': 28,
    'InfestingCommandCenter': 29,
    'PlaceBuilding': 30,
    'PlaceProtossBuilding': 31,
    'CreateProtossBuilding': 32,
    'ConstructingBuilding': 33,
    'Repair': 34,
    'MoveToRepair': 35,
    'PlaceAddon': 36,
    'BuildAddon': 37,
    'Train': 38,
    'RallyPointUnit': 39,
    'RallyPointTile': 40,
    'ZergBirth': 41,
    'ZergUnitMorph': 42,
    'ZergBuildingMorph': 43,
    'IncompleteBuilding': 44,
    'IncompleteMorphing': 45,
    'BuildNydusExit': 46,
    'EnterNydusCanal': 47,
    'IncompleteWarping': 48,
    'Follow': 49,
    'Carrier': 50,
    'ReaverCarrierMove': 51,
    'CarrierStop': 52,
    'CarrierAttack': 53,
    'CarrierMoveToAttack': 54,
    'CarrierIgnore2': 55,
    'CarrierFight': 56,
    'CarrierHoldPosition': 57,
    'Reaver': 58,
    'ReaverAttack': 59,
    'ReaverMoveToAttack': 60,
    'ReaverFight': 61,
    'ReaverHoldPosition': 62,
    'TrainFighter': 63,
    'InterceptorAttack': 64,
    'ScarabAttack': 65,
    'RechargeShieldsUnit': 66,
    'RechargeShieldsBattery': 67,
    'ShieldBattery': 68,
    'InterceptorReturn': 69,
    'DroneLand': 70,
    'BuildingLand': 71,
    'BuildingLiftOff': 72,
    'DroneLiftOff': 73,
    'LiftingOff': 74,
    'ResearchTech': 75,
    'Upgrade': 76,
    'Larva': 77,
    'SpawningLarva': 78,
    'Harvest1': 79,
    'Harvest2': 80,
    'MoveToGas': 81,
    'WaitForGas': 82,
    'HarvestGas': 83,
    'ReturnGas': 84,
    'MoveToMinerals': 85,
    'WaitForMinerals': 86,
    'MiningMinerals': 87,
    'Harvest3': 88,
    'Harvest4': 89,
    'ReturnMinerals': 90,
    'Interrupted': 91,
    'EnterTransport': 92,
    'PickupIdle': 93,
    'PickupTransport': 94,
    'PickupBunker': 95,
    'Pickup4': 96,
    'PowerupIdle': 97,
    'Sieging': 98,
    'Unsieging': 99,
    'WatchTarget': 100,
    'InitCreepGrowth': 101,
    'SpreadCreep': 102,
    'StoppingCreepGrowth': 103,
    'GuardianAspect': 104,
    'ArchonWarp': 105,
    'CompletingArchonSummon': 106,
    'HoldPosition': 107,
    'QueenHoldPosition': 108,
    'Cloak': 109,
    'Decloak': 110,
    'Unload': 111,
    'MoveUnload': 112,
    'FireYamatoGun': 113,
    'MoveToFireYamatoGun': 114,
    'CastLockdown': 115,
    'Burrowing': 116,
    'Burrowed': 117,
    'Unburrowing': 118,
    'CastDarkSwarm': 119,
    'CastParasite': 120,
    'CastSpawnBroodlings': 121,
    'CastEMPShockwave': 122,
    'NukeWait': 123,
    'NukeTrain': 124,
    'NukeLaunch': 125,
    'NukePaint': 126,
    'NukeUnit': 127,
    'CastNuclearStrike': 128,
    'NukeTrack': 129,
    'InitializeArbiter': 130,
    'CloakNearbyUnits': 131,
    'PlaceMine': 132,
    'RightClickAction': 133,
    'SuicideUnit': 134,
    'SuicideLocation': 135,
    'SuicideHoldPosition': 136,
    'CastRecall': 137,
    'Teleport': 138,
    'CastScannerSweep': 139,
    'Scanner': 140,
    'CastDefensiveMatrix': 141,
    'CastPsionicStorm': 142,
    'CastIrradiate': 143,
    'CastPlague': 144,
    'CastConsume': 145,
    'CastEnsnare': 146,
    'CastStasisField': 147,
    'CastHallucination': 148,
    'Hallucination2': 149,
    'ResetCollision': 150,
    'ResetHarvestCollision': 151,
    'Patrol': 152,
    'CTFCOPInit': 153,
    'CTFCOPStarted': 154,
    'CTFCOP2': 155,
    'ComputerAI': 156,
    'AtkMoveEP': 157,
    'HarassMove': 158,
    'AIPatrol': 159,
    'GuardPost': 160,
    'RescuePassive': 161,
    'Neutral': 162,
    'ComputerReturn': 163,
    'InitializePsiProvider': 164,
    'SelfDestructing': 165,
    'Critter': 166,
    'HiddenGun': 167,
    'OpenDoor': 168,
    'CloseDoor': 169,
    'HideTrap': 170,
    'RevealTrap': 171,
    'EnableDoodad': 172,
    'DisableDoodad': 173,
    'WarpIn': 174,
    'Medic': 175,
    'MedicHeal': 176,
    'HealMove': 177,
    'MedicHoldPosition': 178,
    'MedicHealToIdle': 179,
    'CastRestoration': 180,
    'CastDisruptionWeb': 181,
    'CastMindControl': 182,
    'DarkArchonMeld': 183,
    'CastFeedback': 184,
    'CastOpticalFlare': 185,
    'CastMaelstrom': 186,
    'JunkYardDog': 187,
    'Fatal': 188,
    'None': 189,
    'Unknown': 190,
    'MAX': 191
}
_build_index(orders)

# Corresponds to BWAPI::TechTypes::Enum
tech_types = {
    'Stim_Packs': 0,
    'Lockdown': 1,
    'EMP_Shockwave': 2,
    'Spider_Mines': 3,
    'Scanner_Sweep': 4,
    'Tank_Siege_Mode': 5,
    'Defensive_Matrix': 6,
    'Irradiate': 7,
    'Yamato_Gun': 8,
    'Cloaking_Field': 9,
    'Personnel_Cloaking': 10,
    'Burrowing': 11,
    'Infestation': 12,
    'Spawn_Broodlings': 13,
    'Dark_Swarm': 14,
    'Plague': 15,
    'Consume': 16,
    'Ensnare': 17,
    'Parasite': 18,
    'Psionic_Storm': 19,
    'Hallucination': 20,
    'Recall': 21,
    'Stasis_Field': 22,
    'Archon_Warp': 23,
    'Restoration': 24,
    'Disruption_Web': 25,
    'Unused_26': 26,
    'Mind_Control': 27,
    'Dark_Archon_Meld': 28,
    'Feedback': 29,
    'Optical_Flare': 30,
    'Maelstrom': 31,
    'Lurker_Aspect': 32,
    'Unused_33': 33,
    'Healing': 34,
    'None': 44,
    'Nuclear_Strike': 45,
    'Unknown': 46,
    'MAX': 47
}
_build_index(tech_types)

# Corresponds to BWAPI::UnitTypes::Enum
unit_types = {
    'Terran_Marine': 0,
    'Terran_Ghost': 1,
    'Terran_Vulture': 2,
    'Terran_Goliath': 3,
    'Terran_Siege_Tank_Tank_Mode': 5,
    'Terran_SCV': 7,
    'Terran_Wraith': 8,
    'Terran_Science_Vessel': 9,
    'Terran_Dropship': 11,
    'Terran_Battlecruiser': 12,
    'Terran_Vulture_Spider_Mine': 13,
    'Terran_Nuclear_Missile': 14,
    'Terran_Civilian': 15,
    'Terran_Siege_Tank_Siege_Mode': 30,
    'Terran_Firebat': 32,
    'Spell_Scanner_Sweep': 33,
    'Terran_Medic': 34,
    'Zerg_Larva': 35,
    'Zerg_Egg': 36,
    'Zerg_Zergling': 37,
    'Zerg_Hydralisk': 38,
    'Zerg_Ultralisk': 39,
    'Zerg_Broodling': 40,
    'Zerg_Drone': 41,
    'Zerg_Overlord': 42,
    'Zerg_Mutalisk': 43,
    'Zerg_Guardian': 44,
    'Zerg_Queen': 45,
    'Zerg_Defiler': 46,
    'Zerg_Scourge': 47,
    'Zerg_Infested_Terran': 50,
    'Terran_Valkyrie': 58,
    'Zerg_Cocoon': 59,
    'Protoss_Corsair': 60,
    'Protoss_Dark_Templar': 61,
    'Zerg_Devourer': 62,
    'Protoss_Dark_Archon': 63,
    'Protoss_Probe': 64,
    'Protoss_Zealot': 65,
    'Protoss_Dragoon': 66,
    'Protoss_High_Templar': 67,
    'Protoss_Archon': 68,
    'Protoss_Shuttle': 69,
    'Protoss_Scout': 70,
    'Protoss_Arbiter': 71,
    'Protoss_Carrier': 72,
    'Protoss_Interceptor': 73,
    'Protoss_Reaver': 83,
    'Protoss_Observer': 84,
    'Protoss_Scarab': 85,
    'Critter_Rhynadon': 89,
    'Critter_Bengalaas': 90,
    'Critter_Scantid': 93,
    'Critter_Kakaru': 94,
    'Critter_Ragnasaur': 95,
    'Critter_Ursadon': 96,
    'Zerg_Lurker_Egg': 97,
    'Zerg_Lurker': 103,
    'Spell_Disruption_Web': 105,
    'Terran_Command_Center': 106,
    'Terran_Comsat_Station': 107,
    'Terran_Nuclear_Silo': 108,
    'Terran_Supply_Depot': 109,
    'Terran_Refinery': 110,
    'Terran_Barracks': 111,
    'Terran_Academy': 112,
    'Terran_Factory': 113,
    'Terran_Starport': 114,
    'Terran_Control_Tower': 115,
    'Terran_Science_Facility': 116,
    'Terran_Covert_Ops': 117,
    'Terran_Physics_Lab': 118,
    'Terran_Machine_Shop': 120,
    'Terran_Engineering_Bay': 122,
    'Terran_Armory': 123,
    'Terran_Missile_Turret': 124,
    'Terran_Bunker': 125,
    'Zerg_Infested_Command_Center': 130,
    'Zerg_Hatchery': 131,
    'Zerg_Lair': 132,
    'Zerg_Hive': 133,
    'Zerg_Nydus_Canal': 134,
    'Zerg_Hydralisk_Den': 135,
    'Zerg_Defiler_Mound': 136,
    'Zerg_Greater_Spire': 137,
    'Zerg_Queens_Nest': 138,
    'Zerg_Evolution_Chamber': 139,
    'Zerg_Ultralisk_Cavern': 140,
    'Zerg_Spire': 141,
    'Zerg_Spawning_Pool': 142,
    'Zerg_Creep_Colony': 143,
    'Zerg_Spore_Colony': 144,
    'Zerg_Sunken_Colony': 146,
    'Zerg_Extractor': 149,
    'Protoss_Nexus': 154,
    'Protoss_Robotics_Facility': 155,
    'Protoss_Pylon': 156,
    'Protoss_Assimilator': 157,
    'Protoss_Observatory': 159,
    'Protoss_Gateway': 160,
    'Protoss_Photon_Cannon': 162,
    'Protoss_Citadel_of_Adun': 163,
    'Protoss_Cybernetics_Core': 164,
    'Protoss_Templar_Archives': 165,
    'Protoss_Forge': 166,
    'Protoss_Stargate': 167,
    'Protoss_Fleet_Beacon': 169,
    'Protoss_Arbiter_Tribunal': 170,
    'Protoss_Robotics_Support_Bay': 171,
    'Protoss_Shield_Battery': 172,
    'Resource_Mineral_Field': 176,
    'Resource_Mineral_Field_Type_2': 177,
    'Resource_Mineral_Field_Type_3': 178,
    'Resource_Vespene_Geyser': 188,
    'Spell_Dark_Swarm': 202,
    'MAX': 233
}
_build_index(unit_types)

# Corresponds to BWAPI::BulletTypes::Enum
bullet_types = {
    'Melee': 0,
    'Fusion_Cutter_Hit': 141,
    'Gauss_Rifle_Hit': 142,
    'C_10_Canister_Rifle_Hit': 143,
    'Gemini_Missiles': 144,
    'Fragmentation_Grenade': 145,
    'Longbolt_Missile': 146,
    'Unused_Lockdown': 147,
    'ATS_ATA_Laser_Battery': 148,
    'Burst_Lasers': 149,
    'Arclite_Shock_Cannon_Hit': 150,
    'EMP_Missile': 151,
    'Dual_Photon_Blasters_Hit': 152,
    'Particle_Beam_Hit': 153,
    'Anti_Matter_Missile': 154,
    'Pulse_Cannon': 155,
    'Psionic_Shockwave_Hit': 156,
    'Psionic_Storm': 157,
    'Yamato_Gun': 158,
    'Phase_Disruptor': 159,
    'STA_STS_Cannon_Overlay': 160,
    'Sunken_Colony_Tentacle': 161,
    'Venom_Unused': 162,
    'Acid_Spore': 163,
    'Plasma_Drip_Unused': 164,
    'Glave_Wurm': 165,
    'Seeker_Spores': 166,
    'Queen_Spell_Carrier': 167,
    'Plague_Cloud': 168,
    'Consume': 169,
    'Ensnare': 170,
    'Needle_Spine_Hit': 171,
    'Invisible': 172,
    'Optical_Flare_Grenade': 201,
    'Halo_Rockets': 202,
    'Subterranean_Spines': 203,
    'Corrosive_Acid_Shot': 204,
    'Corrosive_Acid_Hit': 205,
    'Neutron_Flare': 206,
    'None': 209,
    'Unknown': 210,
    'MAX': 211
}
_build_index(unit_types)

# Corresponds to BWAPI::WeaponTypes::Enum
weapon_types = [
    "Gauss_Rifle", "Gauss_Rifle_Jim_Raynor", "C_10_Canister_Rifle",
    "C_10_Canister_Rifle_Sarah_Kerrigan", "Fragmentation_Grenade",
    "Fragmentation_Grenade_Jim_Raynor", "Spider_Mines", "Twin_Autocannons",
    "Hellfire_Missile_Pack", "Twin_Autocannons_Alan_Schezar",
    "Hellfire_Missile_Pack_Alan_Schezar", "Arclite_Cannon",
    "Arclite_Cannon_Edmund_Duke", "Fusion_Cutter", "", "Gemini_Missiles",
    "Burst_Lasers", "Gemini_Missiles_Tom_Kazansky", "Burst_Lasers_Tom_Kazansky",
    "ATS_Laser_Battery", "ATA_Laser_Battery", "ATS_Laser_Battery_Hero",
    "ATA_Laser_Battery_Hero", "ATS_Laser_Battery_Hyperion",
    "ATA_Laser_Battery_Hyperion", "Flame_Thrower", "Flame_Thrower_Gui_Montag",
    "Arclite_Shock_Cannon", "Arclite_Shock_Cannon_Edmund_Duke",
    "Longbolt_Missile", "Yamato_Gun", "Nuclear_Strike", "Lockdown",
    "EMP_Shockwave", "Irradiate", "Claws", "Claws_Devouring_One",
    "Claws_Infested_Kerrigan", "Needle_Spines", "Needle_Spines_Hunter_Killer",
    "Kaiser_Blades", "Kaiser_Blades_Torrasque", "Toxic_Spores", "Spines", "",
    "", "Acid_Spore", "Acid_Spore_Kukulza", "Glave_Wurm", "Glave_Wurm_Kukulza",
    "", "", "Seeker_Spores", "Subterranean_Tentacle", "Suicide_Infested_Terran",
    "Suicide_Scourge", "Parasite", "Spawn_Broodlings", "Ensnare", "Dark_Swarm",
    "Plague", "Consume", "Particle_Beam", "", "Psi_Blades", "Psi_Blades_Fenix",
    "Phase_Disruptor", "Phase_Disruptor_Fenix", "", "Psi_Assault",
    "Psionic_Shockwave", "Psionic_Shockwave_TZ_Archon", "",
    "Dual_Photon_Blasters", "Anti_Matter_Missiles", "Dual_Photon_Blasters_Mojo",
    "Anti_Matter_Missiles_Mojo", "Phase_Disruptor_Cannon",
    "Phase_Disruptor_Cannon_Danimoth", "Pulse_Cannon", "STS_Photon_Cannon",
    "STA_Photon_Cannon", "Scarab", "Stasis_Field", "Psionic_Storm",
    "Warp_Blades_Zeratul", "Warp_Blades_Hero", "", "", "", "", "",
    "Platform_Laser_Battery", "Independant_Laser_Battery", "", "",
    "Twin_Autocannons_Floor_Trap", "Hellfire_Missile_Pack_Wall_Trap",
    "Flame_Thrower_Wall_Trap", "Hellfire_Missile_Pack_Floor_Trap",
    "Neutron_Flare", "Disruption_Web", "Restoration", "Halo_Rockets",
    "Corrosive_Acid", "Mind_Control", "Feedback", "Optical_Flare", "Maelstrom",
    "Subterranean_Spines", "", "Warp_Blades", "C_10_Canister_Rifle_Samir_Duran",
    "C_10_Canister_Rifle_Infested_Duran", "Dual_Photon_Blasters_Artanis",
    "Anti_Matter_Missiles_Artanis", "C_10_Canister_Rifle_Alexei_Stukov", "", "",
    "", "", "", "", "", "", "", "", "", "", "", "None", "Unknown"
]

# Corresponds to BWAPI::UnitSizeTypes::Enum
unit_size_types = {
    'Independent': 0,
    'Small': 1,
    'Medium': 2,
    'Large': 3
}

# Corresponds to BWAPI::DamageTypes::Enum
damage_types = {
    'Independent': 0,
    'Explosive': 1,
    'Concussive': 2,
    'Normal': 3,
    'Ignore_Armor': 4,
    'None': 5
}

c = unit_command_types
o = orders

# Corresponds to BWAPI::UnitCommandTypes to BWAPI::Orders
command2order = {
    c['Halt_Construction']: [o['ResetCollision']],
    c['Upgrade']: [o['Upgrade']],
    c['Cancel_Morph']: [o['PlayerGuard'], o['ResetCollision']],
    c['Return_Cargo']: [o['ReturnGas'], o['ReturnMinerals'],
                        o['ResetCollision']],
    c['Attack_Unit']: [o['AttackUnit'], o['InterceptorAttack'],
                       o['ScarabAttack']],
    c['Cloak']: [o['Cloak']],
    c['Research']: [o['ResearchTech']],
    c['Attack_Move']: [o['AttackMove']],
    c['Build']: [o['PlaceBuilding'], o['BuildNydusExit'],
                 o['CreateProtossBuilding']],
    c['Right_Click_Unit']: [o['MoveToMinerals'], o['MoveToGas'],
                            o['ConstructingBuilding'], o['AttackUnit'],
                            o['Follow'], o['ResetCollision'],
                            o['EnterNydusCanal'], o['EnterTransport'],
                            o['Harvest1'], o['Harvest2'],
                            o['Harvest3'], o['Harvest4'],
                            o['InterceptorAttack'], o['HarvestGas'],
                            o['MedicHeal'], o['MiningMinerals'],
                            o['ReturnMinerals'], o['ReturnGas'],
                            o['RightClickAction'], o['ScarabAttack'],
                            o['WaitForGas'], o['WaitForMinerals']],
    c['Cancel_Upgrade']: [o['Nothing']],
    c['Siege']: [o['Sieging']],
    c['Train']: [o['Train'], o['TrainFighter']],
    c['Unload']: [o['Unload']],
    c['Stop']: [o['Stop'], o['Interrupted']],
    c['Cancel_Research']: [o['Nothing']],
    c['Lift']: [o['BuildingLiftOff']],
    c['Unburrow']: [o['Unburrowing']],
    c['Cancel_Train_Slot']: [o['Nothing']],
    c['Land']: [o['BuildingLand']],
    c['Set_Rally_Unit']: [o['RallyPointUnit']],
    c['Hold_Position']: [o['HoldPosition']],
    c['Morph']: [o['ZergUnitMorph'], o['ZergBuildingMorph']],
    c['Cancel_Construction']: [o['ResetCollision'], o['Die']],
    c['Gather']: [o['MoveToMinerals'], o['MoveToGas'], o['Harvest1'],
                  o['Harvest2'], o['Harvest3'], o['Harvest4'], o['HarvestGas'],
                  o['MiningMinerals'], o['WaitForGas'], o['WaitForMinerals'],
                  o['ResetCollision'], o['ReturnMinerals']],
    c['Cancel_Addon']: [o['Nothing']],
    c['Cancel_Train']: [o['Nothing']],
    c['Burrow']: [o['Burrowing']],
    c['Decloak']: [o['Decloak']],
    c['Unsiege']: [o['Unsieging']],
    c['Right_Click_Position']: [o['Move']],
    c['Unload_All']: [o['Unload'], o['MoveUnload']],
    c['Load']: [o['PickupBunker'], o['PickupTransport'], o['EnterTransport'],
                o['Pickup4']],
    c['Repair']: [o['Repair']],
    c['Unload_All_Position']: [o['MoveUnload']],
    c['Patrol']: [o['Patrol']],
    c['Move']: [o['Move']],
    c['Build_Addon']: [o['BuildAddon'], o['PlaceAddon']],
    c['Set_Rally_Position']: [o['RallyPointTile'], o['RallyPointUnit']],
    c['Follow']: [o['Follow']],
    c['Use_Tech']: [o['Cloak'], o['Decloak']],
    c['Use_Tech_Position']: [o['CastDarkSwarm'], o['CastDisruptionWeb'],
                             o['CastEMPShockwave'], o['CastEnsnare'],
                             o['CastNuclearStrike'], o['CastRecall'],
                             o['CastPsionicStorm'], o['CastPlague'],
                             o['CastScannerSweep'], o['CastStasisField'],
                             o['PlaceMine']],
    c['Use_Tech_Unit']: [o['ArchonWarp'], o['CastConsume'],
                         o['CastDefensiveMatrix'], o['CastFeedback'],
                         o['CastHallucination'], o['CastIrradiate'],
                         o['CastInfestation'], o['CastLockdown'],
                         o['CastMaelstrom'], o['CastMindControl'],
                         o['CastOpticalFlare'], o['CastParasite'],
                         o['CastRestoration'], o['CastSpawnBroodlings'],
                         o['DarkArchonMeld'], o['FireYamatoGun'],
                         o['InfestingCommandCenter'], o['RechargeShieldsUnit']]
}


def concat_cmd(cmd, *args):
    result = cmd
    for arg in args:
        result = str(result) + ',' + str(arg)
    return result


def is_building(unit_type_id):
    return unit_types['Terran_Command_Center'] <= unit_type_id \
           <= unit_types['Protoss_Shield_Battery']


def is_worker(unit_type_id):
    return unit_type_id == unit_types['Protoss_Probe'] \
           or unit_type_id == unit_types['Terran_SCV'] \
           or unit_type_id == unit_types['Zerg_Drone']


def is_mineral_field(unit_type_id):
    return unit_type_id == unit_types['Resource_Mineral_Field'] \
        or unit_type_id == unit_types['Resource_Mineral_Field_Type_2'] \
        or unit_type_id == unit_types['Resource_Mineral_Field_Type_3']


def is_gas_geyser(unit_type_id):
    return unit_type_id == unit_types['Resource_Vespene_Geyser'] \
        or unit_type_id == unit_types['Protoss_Assimilator'] \
        or unit_type_id == unit_types['Terran_Refinery'] \
        or unit_type_id == unit_types['Zerg_Extractor']
