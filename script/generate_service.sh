#!/bin/sh

script_path=$(dirname "$(readlink -f "$0")")
cd $(dirname "$script_path")

system_text="[Unit]
Description=Minecraft server handler bot
After=multi-user.target

[Service]
Type=simple
Restart=always
WorkingDirectory="$(pwd)"
ExecStart="$(pwd)/env/bin/python3" "$(pwd)/minecraft.py"

[Install]
WantedBy=multi-user.target
"
echo "Move the '$(pwd)/mc_bot.service' file to /etc/systemd/system"
echo "$system_text" > mc_bot.service
