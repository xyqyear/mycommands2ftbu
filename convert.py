from nbt import nbt

player_id_to_uuid = {}
with open("./server/LMPlayers.txt") as f:
    lines = f.readlines()
    for line in lines:
        pid, name, uuid = line.split()
        player_id_to_uuid[pid] = uuid

player_homes = {}
with open("./server/homes.txt", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        uuid, homestr = line.split(",", 1)
        # because the uuids in LMPlayers.txt don't have dashes
        uuid = uuid.replace("-", "")

        home_name, home_pos = homestr.rsplit("(", 1)
        home_pos = home_pos[:-2]
        x, y, z, dim = home_pos.split(",")
        x = int(float(x))
        y = int(float(y))
        z = int(float(z))
        dim = int(dim)

        home = nbt.TAG_Int_Array(home_name)
        home.value = [x, y, z, dim]

        if uuid in player_homes:
            player_homes[uuid].append(home)
        else:
            player_homes[uuid] = [home]

with open("./server/LMPlayers.dat", "rb") as f:
    nbtfile = nbt.NBTFile(buffer=f)

for tag in nbtfile["Players"].tags:
    homes = tag["Homes"]
    pid = tag.name
    uuid = player_id_to_uuid[pid]
    if uuid in player_homes:
        for home in player_homes[uuid]:
            homes.tags.append(home)

with open("./server/LMPlayers_with_homes.dat", "wb") as f:
    nbtfile.write_file(buffer=f)
