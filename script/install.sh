#!/bin/sh

script_path=$(dirname "$(readlink -f "$0")")
echo "(Re)-Installing the discord bot service"

if [ "$(id -u)" -ne 0 ]; then
    echo "You are not root, run this target as root please"
    exit 1
fi

"$script_path/generate_service.sh" > /dev/null
mv -f "./mc_bot.service" "/etc/systemd/system/"
echo "Installed 'mc_bot.service' in '/etc/systemd/system/'"
