# Overpass Queries

A collection of my overpass queries. Includes a python script to update this readme.

## Queries

### [crossing!=traffic_signals Near Traffic Signals](crossing!=traffic_sginals.txt)
Returns crossings without crossing=traffic_signals near traffic signals.
### [Crossing Nodes without Crossing Ways](crossing-nodes-wo-crossing-ways.txt)
Returns crossing nodes that are not attached to a crossing way. Also includes crossing nodes attached directly to sidewalks.
### [Crossings without Kerbs](crossings-wo-kerbs.txt)
Returns crossing ways that are not attached to a kerb node. Will not return crossings that have incomplete kerbs, such as only at one end.
### [Features Edited During a Time Window](edited-features.txt)
Returns all features last edited by the specified user as of a chosen time with a start time as well. Good for seeing everything edited on a mapping excursion.
### [Intersections of Alberta and Prescott](intersection-alberta-prescott.txt)
Query to resolve a long running inside joke about the intersection of paralell roads Alberta and Prescott in Portland, OR.
### [Miniature Railways](miniature-railroads.txt)
Returns all miniature railways in US, styled to indicate whether gauge is specified.
### [Roads without Surface](roads-wo-surface.txt)
Returns a selection of roads without surface values.
### [Sett and Similar Surface Roads](sett-etc-roads.txt)
Finds sett, cobblesotn, paving_stones, and unhewn_cobblestone surface values.
### [Sett and Similar Surfaces with Nearby Unspecified Surfaces](sett-etc-w-nearby.txt)
Finds all sett, cobblestone, unhewn_cobblestone, and paving_stones road sufaces. In addition finds all roads nearby them with no surface values.