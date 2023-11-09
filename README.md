This is a tool to help you convert homes from the MyCommands mod to the FTBU format.

You will need to locate the following files:

- `homes.txt` in the `world/mycommands/homes` directory
- `LMPlayers.dat` in the `world/Latmod` directory
- `LMPlayers.txt` in the `world/Latmod` directory

Place these files in a subfolder named "server" located in the same directory as `convert.py`.

Next, run `convert.py`, and it will generate a file named "LMPlayers_with_homes.dat" in the "server" folder.

`/home` commands were not behaving correctly in FTBU version 1.7.10 before the GTNH team [fixed](https://github.com/GTNewHorizons/FTB-Utilities/pull/1) the problem. Before the fix, I was using the broken version on my server, so I used [MyCommands](https://www.curseforge.com/minecraft/mc-mods/mycommands) together with FTBU. Now, I want to revert to using FTBU alone (or [ServerUtilities](https://github.com/GTNewHorizons/ServerUtilities)), but I don't want to lose my homes, so I created this tool to transfer the homes from MyCommands to the FTBU format.

This script assumes that both mods are in use on your server. If you have not had FTBU installed while you were using MyCommands, the script will not work because the user information will not be present in `LMPlayers.dat`.
