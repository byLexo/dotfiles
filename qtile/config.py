from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Change window size (MonadTail)
    Key([mod, "shift"], "h", lazy.layout.shrink(),
        desc="Shrink the window"),
    Key([mod, "shift"], "l", lazy.layout.grow(),
        desc="Grow the window"),

    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), 
        desc="Move window up"),

    # Toggle between different layaouts as defined below
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(),
        desc="Move window focus to previous window"),

    # Kill window
    Key([mod], "w", lazy.window.kill(), 
        desc="Kill focused window"),
    
    # Switch focus of monitors
    #Key([mod], "period", lazy.next_screen()),
    #Key([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    # Shutdown Qtile
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
    #    desc="Toggle between split and unsplit sides of stack"),

    #Key([mod], "r", lazy.spawncmd(),
    #    desc="Spawn a command using a prompt widget"),

    # ------------ App Configs ------------

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    key([mod], "b", lazy.spawn("firefox")),

    # File Explorer
    Key([mod, "shift"], "e", lazy.spawn("pcmanfm")),

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn(
    "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
    "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
    "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),


]

groups = [Group("WWW", {'layout': 'monadtall'}),
              Group("DEV", {'layout': 'monadtall'}),
              Group("SYS", {'layout': 'monadtall'}),
              Group("DOC", {'layout': 'monadtall'})]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

layout_conf = {"border_width": 1,
                "margin": 4,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ]
    #border_focus=colors["color4"][0]
)

colors = {
    "dark": [
        "#0f101a",
        "#0f101a"
    ],
    "grey": [
        "#353c4a",
        "#353c4a"
    ],
    "light": [
        "#f1ffff",
        "#f1ffff"
    ],
    "text": [
        "#0f101a",
        "#0f101a"
    ],
    "focus": [
        "#a151d3",
        "#a151d3"
    ],
    "active": [
        "#f1ffff",
        "#f1ffff"
    ],
    "inactive": [
        "#4c566a",
        "#4c566a"
    ],
    "urgent": [
        "#F07178",
        "#F07178"
    ],
    "color1": [
        "#a151d3",
        "#a151d3"
    ],
    "color2": [
        "#F07178",
        "#F07178"
    ],
    "color3": [
        "#fb9f7f",
        "#fb9f7f"
    ],
    "color4": [
        "#ffd47e",
        "#ffd47e"
    ]
}

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        #text="D", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True,
            visible_groups=["WWW","DEV","SYS","DOC"]
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text='⟳'), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color3', 'color4'),

    icon(bg="color3", text=''),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color3'), interface='enp1s0'),

    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
    widget.QuickExit(),
]


widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()

def status_bar(widgets):
    return bar.Bar(widgets, size=24, opacity=0.92)


screens = [Screen(top=status_bar(primary_widgets))]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
#floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
#    *layout.Floating.default_float_rules,
#    Match(wm_class='confirmreset'),  # gitk
#    Match(wm_class='makebranch'),  # gitk
#    Match(wm_class='maketag'),  # gitk
#    Match(wm_class='ssh-askpass'),  # ssh-askpass
#    Match(title='branchdialog'),  # gitk
#    Match(title='pinentry'),  # GPG key password entry
#])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
