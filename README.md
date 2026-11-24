# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/renxweb3/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/renxweb3/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A one-page newspaper front page that sums up the world news of Tuesday
24 November 2026 in a single 1024×1024 image. The lead story is Nvidia
reinstating Jensen Huang after Trump intervened, above five more stories:
NATO's vow to defend space, the Zaporizhzhia strike, fourteen nations
backing the ICJ's Myanmar genocide verdict, the Gaza strikes, COP31
ending without a deal, and US states suing Musk's firms over Grok's
images. A footer strip adds the 700,000+ Russian war dead, the $41bn
Sanofi–Insmed deal, the Nepal quake, and Malaysia's Rohingya returns.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or
`/output/entry.png` when the variable is unset). No network, no
randomness: every run writes the same bytes.

## How the image was made

`draw.py` draws the whole front page from scratch with Pillow and the
system DejaVu fonts — masthead, headline, deck, a night-circuit band,
six story cells, and a numbers strip. Run it to regenerate the image:

```sh
python3 draw.py
```

All headlines were checked against real reporting from 24 November 2026
(Just Security, The Global Eye, 10 Things, Principia, Horizon, IQMIA).

---

<sub>Entered on [make.fun](https://make.fun/?ref=kacxzt8q&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
