# Example programs + in-browser runner

trinket.io (which used to host the live turtle demos) **shuts down 2026-08-31**.
This folder replaces it with a **self-hosted runner** so the demos keep working
with no dependency on any outside service.

## The runner

`run.html` runs Python — including `turtle` graphics — entirely in the browser
using **Skulpt** (vendored under `skulpt/`, so nothing is fetched from a CDN).
Link to an example like:

```
examples/run.html?file=hexagon.py
examples/run.html?file=quakes_map_runner.py&data=allWeek2017Jan17.csv
```

- `file=` — the `.py` program to load (shown in an editable box; students can tweak and re-run).
- `data=` — optional comma-separated data file(s) the program `open()`s (e.g. a CSV).

Nothing is sent to a server; it all runs client-side.

## Turtle examples (recovered from trinket, now run in `run.html`)

| File | Used on | Live link on the site? |
|------|---------|------------------------|
| `hexagon.py` | index.html wk 1 (Hexagon example) | ✅ repointed |
| `hexagon_stamp.py` | index.html wk 1 (Fancier hexagon) | ✅ repointed |
| `color_dots.py` | index.html wk 3 (Color Challenges) | ✅ repointed |
| `random_walk.py` | index.html wk 10 + lab_10 (Random Walk) | ✅ repointed |
| `quakes_map_runner.py` | index.html wk 13 (Turtle Quakes Demo) | ✅ repointed (map + `allWeek2017Jan17.csv`) |
| `quakes_map.py` | faithful Python-2 original of the above | backup only |
| `usgs_plot_runner.py` | lab_09 city-plot demo (LA + Tokyo on the map) | ready — point lab_09 here when restored |
| `usgs_plot.py` | faithful original of the above (expects `map3.jpg`) | backup only |
| `square.py` | lab_01 (Draws a square) | in a removed lab — repoint when restored |
| `two_turtles.py` | lab_03 (multi-colored turtles) | in a removed lab |
| `rgb_color.py` | lab_03 (RGB color) | in a removed lab |
| `random_walk_bounded.py` | lab_10 (bounded random walk) | in a removed lab |

When you restore lab_01/03/09/10 for a future semester, point their turtle links at
`run.html?file=<name>.py` the same way.

### Notes
- `quakes_map_runner.py` / `usgs_plot_runner.py` are Python-3, browser-runnable
  versions of the two mapping demos (the originals `quakes_map.py` / `usgs_plot.py`
  are kept as faithful backups). The quakes runner also fixes the Python-2 `print`
  and turns off turtle animation so ~1,300 points plot in ~2s.
- `allWeek2017Jan17.csv` is the real USGS "past week" earthquake feed from Jan 2017
  (1,365 quakes) that the quakes demo reads.
- `world_map.jpg` is a public-domain equirectangular world map used as the background
  for both mapping demos.
- **Map alignment gotcha:** Skulpt draws `bgpic()` at the image's *native pixel size,
  top-left aligned* — it does NOT stretch it to `setworldcoordinates`. So the turtle
  `setup(W, H)` must exactly match the image's pixel dimensions or the points drift
  (worst near the right/east edge). `world_map.jpg` is 1000x500 and both demos use
  `setup(1000, 500)`. If you swap in a different map, match `setup()` to its size.

## C++ examples (`cpp/`)

The 10 `.cpp` files are the C++ programs that were hosted on **onlinegdb.com**
(index.html weeks 12–13). onlinegdb is not shutting down, so those links are left as
they are — these files are just a safety backup. Skulpt runs Python only, so the
runner does not execute C++.

## pythontutor examples (`pythontutor/`)

27 Python programs decoded from the `pythontutor.com` links on index.html. These were
never at risk (pythontutor encodes the whole program inside the link), but local
copies are handy and they also run in `run.html?file=pythontutor/<name>.py`.
