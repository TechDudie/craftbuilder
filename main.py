import minecraft_launcher_lib
import os

minecraft_launcher_lib.install.install_minecraft_version(latest_version, os.getcwd())

options = {
    "username": "TechnoDot",
    "uuid": "uuidhere",
    "token": ""accesstokenhere"
}
minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)

print(minecraft_command)
