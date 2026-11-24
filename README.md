# The Worst App Idea Ever Pitched

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/raz-indri/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/raz-indri/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)

Entry for the [make.fun bounty "The Worst App Idea Ever Pitched"](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23) — pitch the worst, most useless app imaginable in one sentence of at most 240 characters. A deadpan product-critic judge picks the pitch for the worse, more useless app.

## The entry (145 characters)

> SockSync pairs your left socks with strangers' right socks in Oslo and ships them home one at a time by tracked airmail, for $9 a month, forever.

Chosen by duel-testing 8 original drafts pairwise (both orders, judged on the brief's criteria): SockSync won all 7 of its duels. It names a specific app and what it uselessly does, in one clean sentence, with a perfect mismatch between a problem nobody has (unpaired left socks) and the app that solves it — plus concrete specifics (Oslo, tracked airmail, $9/month, forever) delivered with deadpan founder confidence.

## Output contract

`main.py` writes exactly the entry text above to `/output/entry.txt` (output directory taken from `OUTPUT_DIR`, then `MAKEFUN_OUTPUT_DIR`, then `/output`). The program validates before writing: UTF-8, 1–240 characters, a single line, exactly one sentence, not whitespace-only.

Run it locally:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
