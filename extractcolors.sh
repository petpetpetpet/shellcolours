# Scan a text file for colour declarations in #RRGGBB format.
# Print just the colour declarations to stdout.

INPUTFILE=$1

egrep -e '.*#[0-9A-Fa-f]{2}[0-9A-Fa-f]{2}[0-9A-Fa-f]{2}.*' $INPUTFILE | perl -lpe 's/.*#([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2}).*/#\1\2\3/g'
