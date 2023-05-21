## The Hacker Way


### TMUX
Windows
tmux new -s mysession -n mywindow
start a new session with the name mysession and window mywindow

Ctrl + b c
Create window

Ctrl + b ,
Rename current window

Ctrl + b &
Close current window

Ctrl + b w
List windows

Ctrl + b p
Previous window

Ctrl + b n
Next window

Ctrl + b 0 ... 9
Switch/select window by number

Ctrl + b l
Toggle last active window

swap-window -s 2 -t 1
Reorder window, swap window number 2(src) and 1(dst)

swap-window -t -1
Move current window to the left by one position

Panes
Ctrl + b ;
Toggle last active pane

Ctrl + b %
Split pane with horizontal layout

Ctrl + b "
Split pane with vertical layout

Ctrl + b {
Move the current pane left

Ctrl + b }
Move the current pane right

Ctrl + b 
Ctrl + b 
Ctrl + b 
Ctrl + b 
Switch to pane to the direction

setw synchronize-panes
Toggle synchronize-panes(send command to all panes)

Ctrl + b Spacebar
Toggle between pane layouts

Ctrl + b o
Switch to next pane

Ctrl + b q
Show pane numbers

Ctrl + b q 0 ... 9
Switch/select pane by number

Ctrl + b z
Toggle pane zoom

Ctrl + b !
Convert pane into a window

Ctrl + b + 
Ctrl + b Ctrl + 
Ctrl + b + 
Ctrl + b Ctrl + 
Resize current pane height(holding second key is optional)

Ctrl + b + 
Ctrl + b Ctrl + 
Ctrl + b + 
Ctrl + b Ctrl + 
Resize current pane width(holding second key is optional)

Ctrl + b x

ပြင်ရန် 
the_hacker_way launch ဖိုင်အား delay, wait, isExists များဖြင့်ပြင်ရေးရန်