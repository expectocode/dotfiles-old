#!/bin/bash
# by streetwalrus, i think? or mrmetric? its on a gist somewhere

gdb /usr/bin/telegram-desktop << EOF
tbreak _ZN3App9initMediaEv
commands
    set {char}_ZN3App9msgRadiusEv=0xB8
    set {int}(_ZN3App9msgRadiusEv+1)=3
    set {char}(_ZN3App9msgRadiusEv+5)=0xC3
    set {char}_Z25replaceStringWithEntitiesRK13QLatin1String5QCharR7QStringP5QListI12EntityInTextEb = 0xC3
end
run
detach
quit
EOF
