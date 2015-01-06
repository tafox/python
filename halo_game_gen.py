import random

games = [ "Halo CE", "Halo 2 Classic", "Halo 2 Anniversary", "Halo 3", "Halo 4" ]

game_types = [ "Slayer", "Oddball", "Crazy King", "Capture The Flag", "Assault" ]

halo_ce_maps = [ "Battle Creek", "Blood Gulch", "Boarding Action", "Chill Out", "Chiron TL-34", "Damnation", "Derelict", "Hang 'Em High", "Longest", "Prisoner", "Rat Race", "Sidewinder", "Wizard", "Danger Canyon", "Death Island", "Gephyrophobia", "Ice Fields", "Infinity", "Timberland" ]

halo_2_classic_maps = [ "Ascension", "Backwash", "Beaver Creek", "Burial Mounds", "Coagulation", "Colossus", "Containment", "Desolation", "Elongation", "Gemini", "Headlong", "Ivory Tower", "Lockout", "Midship", "Relic", "Scantuary", "Terminal", "Tombstone", "Turf", "Warlock", "Waterworks", "Zanzibar", "District", "Uplift" ]

halo_2_anniversary_maps = [ "Awash", "Bloodline", "Lockdown", "Shrine", "Stonetown", "Warlord", "Zenith" ]

halo_3_maps = [ "Assembly", "Avalanche", "Blackout", "Citadel", "Cold Storage", "Construct", "Epitaph", "Foundry", "Ghost Town", "Guardian", "Heretic", "High Ground", "Isolation", "Last Resort", "Longshore", "Narrows", "Orbital", "The Pit", "Rat's Nest", "Sandbox", "Snowbound", "Standoff", "Valhalla" ]

halo_4_maps = [ "Abandon", "Adrift", "Complex", "Daybreak", "Erosion", "Exile", "Forge Island", "Harvest", "Haven", "Impact", "Landfall", "Longbow", "Meltdown", "Monolith", "Outcast", "Perdition", "Pitfall", "Ragnarok", "Ravine", "Shatter", "Skyline", "Solace", "Vertigo", "Vortex", "Wreckage" ] 

game = games[random.randrange(0,4)]
game_type = game_types[random.randrange(0,len(game_types)-1)]

if game == "Halo CE":
  game_map = halo_ce_maps[random.randrange(0,len(halo_ce_maps)-1)]
elif game == "Halo 2 Classic":
  game_map = halo_2_classic_maps[random.randrange(0,len(halo_2_classic_maps)-1)]
elif game == "Halo 2 Anniversary":
  game_map = halo_2_anniversary_maps[random.randrange(0,len(halo_2_anniversary_maps)-1)]
elif game == "Halo 3":
  game_map = halo_3_maps[random.randrange(0,len(halo_3_maps)-1)]
else:
  game_map = halo_4_maps[random.randrange(0,len(halo_4_maps)-1)]

print game + "\n" + game_type + " on " + game_map



