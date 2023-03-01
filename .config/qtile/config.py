from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
import re, os, subprocess
from libqtile.widget import base, Spacer 
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
from libqtile.dgroups import simple_key_binder

colors = [["#d3c6aa"],
          ["#e67e80"],
          ["#e69875"],
          ["#dbbc7f"],
          ["#a7c080"],
          ["#83c092"],
          ["#2d353b"],
          ["#343f44"],
          ["#475258"],
          ["#1e2326"],
          ["#d699b6"],
]

def lts(x): #(list to string)
   x = str(x).replace("'", "").replace("[", "").replace("]", "")
   return x

mod = "mod4"
defaultfont = "Cantarell"
terminal = "alacritty"
browser2 = "brave"
browser1 = "librewolf"
ide = "emacs"
file_manager = "thunar"
dmenu = "dmenu_run" + " -sb " + lts(colors[4]) + " -nb " + lts(colors[7]) + " -p Launch: " + " -fn " + defaultfont
editor_cmd = "alacritty -e vim"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"), # Toggle between split and unsplit sides of stack.  # Split = all windows displayed # Unsplit = 1 window displayed, like Max layout, but still with # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "q", lazy.spawn("archlinux-logout"), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),  
    Key([mod], "n", lazy.window.toggle_minimize(), desc="Toggle minimize"),  
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),  
    # Application launchers
    Key([mod, "shift"], "Return", lazy.spawn(dmenu), desc="Run dmenu"),
    Key([mod, "shift"], "e", lazy.spawn(ide), desc="Open ide gui"),
    Key([mod, "shift"], "v", lazy.spawn(editor_cmd), desc="Open vim in a terminal"),
    Key([mod], "o", lazy.spawn("libreoffice"), desc="Open libreoffice"),
    Key([mod, "shift"], "f", lazy.spawn(file_manager), desc="Open thunar"),
    Key([mod], "w", lazy.spawn(browser1), desc="Open brave"),
    Key([mod, "shift"], "w", lazy.spawn(browser2), desc="Open librewolf"),
    Key([mod, "shift"], "m", lazy.spawn("deadbeef"), desc="Open deadbeef"),
    Key([mod, "shift"], "d", lazy.spawn("webcord"), desc="Open discord"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Launch flameshot"),
    #KeyChords
    KeyChord([mod], "e", [
        Key([], "e", lazy.spawn("element-desktop")),
        Key([], "g", lazy.spawn("gdlauncher")),
        Key([], "v", lazy.spawn("alacritty -e vim")),
        Key([], "t", lazy.spawn("transmission-gtk")),
        Key([], "s", lazy.spawn("surf")),

    ])
]
groups = [Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns'),
          Group("", layout='columns')]

dgroups_key_binder = simple_key_binder("mod4")

layout_default = {
        "border_focus": colors[4],
        "border_normal": colors[9],
        "border_width": 2,
        "margin": 5,
        }

layouts = [
    layout.MonadTall(**layout_default),
    # layout.Tile(**layout_default),
    #layout.Zoomy(**layout_default),
    layout.Columns(**layout_default),
    # layout.Max(**layout_default),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_defaults),
    # layout.Matrix(),
    layout.MonadWide(**layout_default),
    layout.RatioTile(**layout_default),
    # layout.TreeTab(**layout_default),
    # layout.VerticalTile(**layout_default),
]

widget_defaults = dict(
    font= defaultfont,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

defaut_font = "Cantarell"

powerline = {
    "decorations": [
        RectDecoration(use_widget_background=True, padding_x=-2, filled=True, size = 8),
        PowerLineDecoration(
            path="back_slash",
            #path=[(0, 0), (1, 0), (0.3, 0.5), (1, 1), (0, 1)], #Variation of the normal left pointing arrow
            padding_y=0,
        )
    ]
}

powerline_left = {
    "decorations": [
        RectDecoration(use_widget_background=True, padding_x=-2, filled=True, size = 8),
        PowerLineDecoration(path="arrow_left", padding_y=0)
    ]
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                background = colors[8],
                length = 6,   
                ),
                widget.CurrentLayout(
                    foreground = colors[4],
                    background = colors[8],
                    **powerline_left,

                ),
                widget.GroupBox(
                    background = colors[7],
                    block_highlight_text_color = colors[1],
                    highlight_color = colors[8],
                    foreground = colors[4],
                    inactive = colors[4],
                    active = colors[5],
                    fontsize = 15,
                    highlight_method='line',
                    urgent_border = colors[10],
                    this_current_screen_border = colors[1],
                    **powerline_left,
                ),
                widget.TaskList(
                    icon_size = 0,
                    background = colors[6],
                    foreground = colors[4],
                    border = colors[1],
                    fontsize = 12,
                    **powerline,
                ),
                widget.CPU(
                    font = defaut_font,
                    background = colors[5],
                    # tag_sensor = 'edge',
                    foreground = colors[9],
                    **powerline,
                ),
                widget.Net(
                    font = defaut_font,
                    background = colors[4],
                    foreground = colors[9],
                    padding = 5,
                    **powerline,
                ),
                widget.Memory(
                    background = colors[3],
                    measure_mem ='M',
                    foreground = colors[9],
                    **powerline,
                ),
                widget.Systray(
                    padding = 5,
                    background = colors[2],
                    foreground = colors[9],
                    icon_size = 20,
                ),
                #Spacer is to fix issue with the systray
                widget.Spacer(
                    background = colors[2],
                    length = 1,
                    **powerline,
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    padding = 4,
                    background = colors[1],
                    foreground = colors[9],
                ),
            ],
            28,
        background = "#2d353b",
        opacity = 1.0,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus = colors[4],
    border_normal = colors[9],
    margin = 5,
    border_width= 2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "qtile"

@hook.subscribe.startup_once
def autostart():
    processes = [
        ['sh','.config/qtile/autostart.sh'],
        ['swaybg', '-i', '/home/zhawitche/.config/qtile/wallpapers/forest-fog.jpg'],
    ]

    for p in processes:
        subprocess.Popen(p)

@hook.subscribe.startup_once
def _():
    top.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
