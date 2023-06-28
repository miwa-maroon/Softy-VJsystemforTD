# MovieBasedVJSet
# Architecture
1. TDAbleton
2. Controller Containers
3. Scene Containers
4. Selector

## Scene Types
* Full Movie Loop - One full playback represents a single full loop and a div by 4 bars.
* Multi Loop - One full playback represents a full loop with multiple 4 bar sub-loops.
* Free - No loop requirements, just play straight, not meant to be synced.

# Scene Container
Each scene container should take ONE CHOP control to parameterize the scene itself.  


## TDA

Watch the ableton tempo and on callback set global TD tempo.
This is done via the chopexec1 that's linked to abletonExport.

## MIDI/OSC
Touch is controlled through custom OSC controls via iPad.


# FX Built In
* Blend Fade - via Switch TOP
* Invert - Level (postprocessing)
* 


