# Turtle example backups (recovered from trinket.io)

trinket.io is **shutting down on 2026-08-31**. All Python source that used to live
on trinket has been recovered and saved here so it is never lost. These are the
`.py` files behind every `trinket.io` link on the CSCI 127 site.

## Examples

| File | Used on | Original trinket link | Extra assets needed |
|------|---------|-----------------------|---------------------|
| `hexagon.py` | index.html, week 1 (Hexagon example) | trinket.io/python/88a94dfc75 | — |
| `hexagon_stamp.py` | index.html, week 1 (Fancier hexagon) | trinket.io/python/a3bede6db8 | — |
| `color_dots.py` | index.html, week 3 (Color Challenges) | trinket.io/python/8e9edc0a1b | — |
| `random_walk.py` | index.html, week 10 + lab_10 (Random Walk) | trinket.io/python/ab6cddc880 | — |
| `quakes_map.py` | index.html, week 13 (Turtle Quakes Demo) | trinket.io/python/c06d30262b | `mapNASA.jpg`, `allWeek2017Jan17.csv` |
| `square.py` | lab_01 (Draws a square) | trinket.io/python/22709f8349 | — |
| `two_turtles.py` | lab_03 (multi-colored turtles) | trinket.io/python/b594e53e4a | — |
| `rgb_color.py` | lab_03 (RGB color) | trinket.io/python/11f1644654 | needs `colormode(255)` in CPython |
| `usgs_plot.py` | lab_09 (Plotting USGS data) | trinket.io/python/7705126110 | `map3.jpg` |
| `random_walk_bounded.py` | lab_10 (bounded random walk) | trinket.io/python/6738c47304 | — |

## Notes / gotchas

- **`quakes_map.py` is Python 2** (`print "..."`). Convert to `print(...)` for
  Python 3 or any browser runner.
- The two mapping demos (`quakes_map.py`, `usgs_plot.py`) need a background image
  and, for the quakes one, the USGS CSV. Those asset files were NOT yet pulled off
  trinket — they can be re-downloaded from USGS, or extracted from the trinket
  before 2026-08-31. The `.py` code (the irreplaceable part) is fully saved.
- `rgb_color.py` uses 0–255 color values; trinket defaulted to that. In standard
  Python add `turtle.colormode(255)` after `import turtle`.

## Links that are NOT at risk

- **pythontutor.com** (29 links on index.html): the full program is encoded inside
  the URL itself, so the code can never be lost even if the site goes away.
- **onlinegdb.com** (10 C++ links on index.html): a separate, still-operating
  service — but the same "code lives on their server" risk applies. Worth backing
  up the same way if you want to be safe.
