import random

games = [ "Halo CE", "Halo 2 Classic", "Halo 2 Anniversary", "Halo 3", "Halo 4" ]

halo_ce_maps = [ "Battle Creek", "Blood Gulch", "Boarding Action", "Chill Out", "Chiron TL-34", "Damnation", "Derelict", "Hang 'Em High", "Longest", "Prisoner", "Rat Race", "Sidewinder", "Wizard", "Danger Canyon", "Death Island", "Gephyrophobia", "Ice Fields", "Infinity", "Timberland" ]

halo_ce_game_types = [ "Slayer:Slayer", "Slayer:Team Slayer", "Slayer:Classic Slayer", "Slayer:Classic Slayer Pro", "Slayer:Classic Phantoms", "Slayer:Classic Elimination", "Slayer:Classic Endurance", "Slayer:Classic Rockets", "Slayer:Classic Snipers",  "Capture The Flag:CTF", "Capture The Flag:Classic CTF", "Capture The Flag:Classic Invasion", "Capture The Flag:Classic Iron CTF", "Capture The Flag:Classic CTF Pro", "Capture The Flag:Assault", "King Of The Hill:King", "King Of The Hill:Crazy King", "King Of The Hill:Team King", "King Of The Hill:Classic King" "King Of The Hill:Classic King Pro", "King Of The Hill:Classic Crazy King", "King Of The Hill:Classic Team King", "Oddball:Oddball", "Oddball:Team Oddball", "Oddball:Classic Oddball", "Oddball:Classic Reverse Tag", "Oddball:Classic Accumulation", "Oddball:Classic Team Oddball", "Oddball:Juggernaut", "Oddball:Classic Juggernaut", "Oddball:Classic Stalker", "Race:Race", "Race:Classic Race", "Race:Classic Rally", "Race:Team Race", "Race:Classic Team Race", "Race:Classic Team Rally" ]

halo_2_classic_maps = [ "Ascension", "Backwash", "Beaver Creek", "Burial Mounds", "Coagulation", "Colossus", "Containment", "Desolation", "Elongation", "Foundation",  "Gemini", "Headlong", "Ivory Tower", "Lockout", "Midship", "Relic", "Scantuary", "Terminal", "Tombstone", "Turf", "Warlock", "Waterworks", "Zanzibar", "District", "Uplift" ]

halo_2_classic_game_types = [ "Slayer:Slayer", "Slayer:Team Slayer", "Slayer:Rockets", "Slayer:Swords", "Slayer:Snipers", "Slayer:Phantoms", "Slayer:Team Phantoms", "Slayer:Elimination", "Slayer:Phantom Elim", "Slayer:SWAT", "Capture The Flag:Mult Flag CTF", "Capture The Flag:CTF Classic", "Capture The Flag:1 Flag CTF", "Capture The Flag:1 Flag CTF Fast", "King Of The Hill:King", "King Of The Hill:Team King", "King Of The Hill:Phantom King", "King Of The Hill:Crazy King", "King Of The Hill:Team Crazy King", "Oddball:Oddball", "Oddball:Rocktetball", "Oddball:Swordball", "Oddball:Team Ball", "Oddball:Low Ball", "Oddball:Fiesta", "Juggernaut:Ninjanaut", "Juggernaut:Phantom Fodder", "Juggernaut:Dreadnaut", "Assault:Multi Bomb", "Assault:Single Bomb", "Assault:Single Bomb Fast", "Assault:Neutral Bomb", "Assault:Blast Resort", "Territories:3 Plots", "Territories:Land Grab", "Territories:Gold Rush", "Territories:Control Issues", "Territories:Contention" ]

halo_2_anniversary_maps = [ "Bloodline", "Lockdown", "Shrine", "Stonetown", "Warlord", "Zenith" ]

halo_2_anniversary_game_types = [ "Slayer:Slayer", "Slayer:Slayer Pro", "Slayer:Team Slayer BR", "Slayer:Slayer BR", "Slayer:Team Slayer", "Slayer:Rockets", "Slayer:Swords", "Slayer:Snipers", "Slayer:Phantoms", "Slayer:Team Phantoms", "Slayer:Elimination", "Slayer:Phantom Elimination", "Slayer:Phantoms", "Slayer:Team Phantoms", "Slayer:Team Snipers", "Slayer:SWAT", "Slayer:SWAT Arsenal", "Capture The Flag:Mult Flag CTF", "Capture The Flag:CTF Classic", "Capture The Flag:1 Flag CTF", "Capture The Flag:1 Flag Classic CTF", "Capture The Flag:Neutral Flag CTF", "Capture The Flag: Gungoose CTF", "Capture The Flag:1 Flag CTF Fast", "King Of The Hill:King", "King Of The Hill:Team King", "King Of The Hill:Phantom King", "King Of The Hill:Kill From The Hill", "King Of The Hill:Crazy King", "King Of The Hill:Team Crazy King", "Oddball:Oddball", "Oddball:Rocktetball", "Oddball:Team Swordball", "Oddball:Swordball", "Oddball:Team Ball", "Oddball:Low Ball", "Oddball:Fiesta", "Juggernaut:Ninjanaut", "Juggernaut:Juggernaut", "Juggernaut:Multi-naut", "Juggernaut:Naut-tacular", "Juggernaut:Juggernaut Elimination", "Juggernaut:Nauticide", "Juggernaut:Phantom Fodder", "Juggernaut:Dreadnaut", "Assault:Multi Bomb", "Assault:Single Bomb", "Assault:Single Bomb Fast", "Assault:Neutral Bomb", "Assault:Blast Resort", "Territories:3 Plots", "Territories:Incursion", "Territories:Lockdown", "Territories:Land Grab", "Territories:Gold Rush", "Territories:Control Issues", "Territories:Contention" "Infection:Infection", "Infection:Cadre", "Infection:Flight", "Infection:Hunted", "Ricochet:Ricochet", "Ricochet:Half-time Ricochet", "Ricochet:Quickochet", "Ricochet:Mult-team Ricochet" ]


halo_3_maps = [ "Assembly", "Avalanche", "Blackout", "Citadel", "Cold Storage", "Construct", "Epitaph", "Foundry", "Ghost Town", "Guardian", "Heretic", "High Ground", "Isolation", "Last Resort", "Longshore", "Narrows", "Orbital", "The Pit", "Rat's Nest", "Sandbox", "Sandtrap", "Snowbound", "Standoff", "Valhalla" ]

halo_3_game_types = [ "Slayer:Slayer", "Slayer:Team Slayer", "Slayer:Rockets", "Slayer:Elimination", "Slayer:Duel", "Capture The Flag:Mult Flag", "Capture The Flag:1 Flag CTF", "Capture The Flag:Tank Flag", "Capture The Flag:Attrition CTF", "King Of The Hill:Team King", "King Of The Hill:Crazy King", "King Of The Hill:Mosh Pit", "Oddball:Oddball", "Oddball:Rocktetball", "Oddball:Team Ball", "Oddball:Low Ball", "Oddball:Ninja Ball", "Juggernaut:Juggernaut", "Juggernaut:Mad Dash", "Juggernaut:Ninjanaut", "Assault:Single Bomb", "Assault:Neutral Bomb", "Assault:Attrition Assault", "Assault:Assault", "Territories:Territories", "Territories:Land Grab", "Territories:Flag Rally", "Infection:Infection", "Infection:Save One Bullet", "Infection:Alpha Zombie", "Infection:Hide and Seek", "VIP:VIP", "VIP:One-sided VIP", "VIP:Escort", "Influential VIP" ]


halo_4_maps = [ "Abandon", "Adrift", "Complex", "Daybreak", "Erosion", "Exile", "Forge Island", "Harvest", "Haven", "Impact", "Landfall", "Longbow", "Meltdown", "Monolith", "Outcast", "Perdition", "Pitfall", "Ragnarok", "Ravine", "Shatter", "Skyline", "Solace", "Vertigo", "Vortex", "Wreckage" ] 

halo_4_game_types = [ "Slayer:Infinity Slayer", "Slayer:Infinity Rumble", "Slayer:SWAT", "Capture The Flag", "King Of The Hill", "Oddball", "Extraction", "Flood", "Regicide" ]

game = games[random.randrange(0,4)]

if game == "Halo CE":
  game_map = halo_ce_maps[random.randrange(0,len(halo_ce_maps)-1)]
  game_type = halo_ce_game_types[random.randrange(0,len(halo_ce_game_types)-1)]
elif game == "Halo 2 Classic":
  game_map = halo_2_classic_maps[random.randrange(0,len(halo_2_classic_maps)-1)]
  game_type = halo_2_classic_game_types[random.randrange(0,len(halo_2_classic_game_types)-1)]
elif game == "Halo 2 Anniversary":
  game_map = halo_2_anniversary_maps[random.randrange(0,len(halo_2_anniversary_maps)-1)]
  game_type = halo_2_anniversary_game_types[random.randrange(0,len(halo_2_anniversary_game_types)-1)]
elif game == "Halo 3":
  game_map = halo_3_maps[random.randrange(0,len(halo_3_maps)-1)]
  game_type = halo_3_game_types[random.randrange(0,len(halo_3_maps)-1)]
else:
  game_map = halo_4_maps[random.randrange(0,len(halo_4_maps)-1)]
  game_type = halo_4_game_types[random.randrange(0,len(halo_4_game_types)-1)]

print game + "\n" + game_type + " on " + game_map




