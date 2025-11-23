# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#

import os
import subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import psutil
import time

mod = "mod4"
terminal = "alacritty"

# --- "Sunset Swing" Colors (Inspired by Spider-Man  wallpaper) ---
colors = {
    "background": "#24283b",      # Deep blue/grey from city shadows
    "foreground": "#c0caf5",      # Light, soft color from the clouds
    "black":      "#1f2335",      # A slightly lighter dark for widgets
    "red":        "#f7768e",      # Classic Spider-Man suit red
    "green":      "#9ece6a",      # Contrasting green for system monitors
    "yellow":     "#e0af68",      # Accent yellow from the sunset
    "blue":       "#7aa2f7",      # A brighter blue accent
    "magenta":    "#bb9af7",      # A soft magenta
    "cyan":       "#7dcfff",      # A bright cyan
    "white":      "#a9b1d6",      # A dimmer white for inactive text
    "orange":     "#ff9e64",      # Accent orange from the sunset
    "focus":      "#ff9e64"       # Using orange as the main accent
}

# --- Keybindings ---
keys = [
    Key([mod], "h", lazy.layout.left()), Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()), Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()), Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()), Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()), Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()), Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.reload_config()), Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "f", lazy.spawn("rofi -show drun")),
    Key([mod], "x", lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu.sh")), desc="Spawn Rofi Powermenu"),
    Key([mod], "s", lazy.spawn("flameshot gui"),desc='screenshot'),
]

# ## Custom Iconic Workspaces ##
group_names = ["1", "2", "3", "4", "5", "6", "7", "8"]
group_labels = ["", "", "", "", "", "", "󰓇", ""]
# Home, Files, Bash, Terminal, Web, GitHub, Music, Discord

groups = [Group(name, label=label) for name, label in zip(group_names, group_labels)]

for i, group in enumerate(groups):
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name, switch_group=True)),
    ])

# --- Layouts ---
layouts = [
    layout.MonadTall(border_focus=colors["focus"], border_normal=colors["black"], border_width=2, margin=8),
    layout.Columns(border_focus=colors["focus"], border_normal=colors["black"], border_width=2, margin=8),
    layout.Max(margin=10),
]

# --- Widget Defaults ---
widget_defaults = dict(font="JetBrains Mono Nerd Font", fontsize=14, padding=3)
extension_defaults = widget_defaults.copy()

# ## FINAL BAR CONFIGURATION - SLEEK & BALANCED ##
screens = [
    Screen(
        top=bar.Bar(
            [
                # LEFT SIDE: Unified block with clear separation
                widget.TextBox(
                    "", # Your chosen Spider Icon
                    foreground=colors["background"],
                    background=colors["red"],
                    padding=10, fontsize=22,
                ),
                widget.TextBox("", fontsize=28, padding=0, foreground=colors["red"], background=colors["background"]),
                widget.GroupBox(
                    font="JetBrainsMono Nerd Font", fontsize=20, borderwidth=3, highlight_method='block',
                    active=colors["focus"], inactive=colors["blue"],
                    block_highlight_text_color=colors["red"],
                    highlight_color=colors["black"],
                    this_current_screen_border=colors["background"], urgent_border=colors["red"],
                    background=colors["background"], rounded=True, disable_drag=True, padding_x=5,
                ),
                widget.TextBox("", fontsize=28, padding=0, foreground=colors["background"], background=colors["blue"]),
                widget.CurrentLayout(background=colors["blue"], foreground=colors["background"], padding=5),

		widget.TextBox("󱣵",fontsize=28, padding=6, foreground=colors["black"], background=colors["blue"],
		mouse_callbacks={'Button1': lazy.spawn('flameshot gui'), 'Button3':lazy.spawn('flameshot full -c')}),

		widget.TextBox("",fontsize=28, padding=0, foreground=colors["blue"],background='#000000CC'),
		
                widget.Spacer(background='#000000CC'),

                # MIDDLE: Window Name
                widget.WindowName(
                    background='#000000CC', foreground=colors["focus"],
                    max_chars=40, font="JetBrainsMono Nerd Font Bold",
                ),
                widget.Spacer(background='#000000CC'),

                # RIGHT SIDE
                widget.TextBox("", fontsize=28, padding=0, foreground=colors["black"], background='#000000CC'),
		widget.TextBox(
			text="",fontsize=20,
			background=colors["black"], foreground=colors["green"],
			padding=10,
			mouse_callbacks={'Button1':lazy.spawn('spotify-launcher')}
                ),
		widget.Volume(
			backend='pamixer',
			background=colors["black"],
			foreground=colors["green"],
			fmt=' {}',
			padding=5
		),
                widget.Battery(
                    background=colors["black"], foreground=colors["green"],
                    format=' {char}{percent:2.0%}', padding=5
                ),
                widget.TextBox("", fontsize=28, padding=0, foreground=colors["blue"], background=colors["black"]),
                widget.Clock(
                    format=' %d-%m-%y  %I:%M %p', background=colors["blue"],
                    foreground=colors["background"], padding=10, font="JetBrainsMono Nerd Font Bold",
                ),
                widget.TextBox("", fontsize=28, padding=0, foreground=colors["red"], background=colors["blue"]),
                widget.TextBox(
                    '⏻ ', foreground=colors["background"], background=colors["red"],
                    padding=5, fontsize=20,
                    mouse_callbacks={'Button1': lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu.sh"))}
                ),
            ],
            30, # Bar height
            background="#00000000", # Fully transparent background
            margin=[8, 12, 4, 12], # Margin for floating effect
        ),
    ),
]

# --- Other Settings ---
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating()),
    Drag([mod], "Button3", lazy.window.set_size_floating()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules, Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"), Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"), Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    border_focus=colors["focus"]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

# --- Autostart Hook ---
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
