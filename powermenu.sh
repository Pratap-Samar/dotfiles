#!/bin/sh

exec &> /tmp/powermenu.log

echo "--- Power menu script started at $(date) ---"

shutdown=" Shutdown"
reboot=" Reboot"
lock=" Lock"
suspend="󰤄 Suspend"
logout="󰗼 Logout"

echo "Defined options. Preparing to launch Rofi..."

chosen=$(printf "%s\n%s\n%s\n%s\n%s" "$shutdown" "$reboot" "$lock" "$suspend" "$logout" | /usr/bin/rofi -dmenu -p "Power Menu" -config /home/solaris/.config/rofi/config.rasi)

echo "Rofi finished. User chose: $chosen"

case "$(echo "$chosen" | cut -d' ' -f2)" in
    Shutdown)
        echo "Executing: /usr/bin/loginctl poweroff"
        systemctl poweroff
        ;;
    Reboot)
        echo "Executing: /usr/bin/loginctl reboot"
        systemctl  reboot
        ;;
    Lock)
        echo "Executing: /usr/bin/betterlockscreen -l"
        /usr/bin/betterlockscreen -l
        ;;
    Suspend)
        echo "Executing: /usr/bin/loginctl suspend"
        systemctl suspend
        ;;
    Logout)
        echo "Executing: /usr/bin/qtile cmd-obj -o cmd -f shutdown"
        /usr/bin/qtile cmd-obj -o cmd -f shutdown
        ;;
    *)
        echo "No valid option chosen. Exiting."
        ;;
esac

echo "--- Power menu script finished ---"

