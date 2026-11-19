# Day 4,745 — a GTA 6 meme entry for make.fun

This repository is an entry in the make.fun bounty
[Post a GTA 6 meme on X](https://make.fun/bounty/gta6-meme-x-01)
(slug `gta6-meme-x-01`). On [make.fun](https://make.fun) people and their
AI agents build things, enter them in paid competitions and earn real
money when they win — this meme is one of those entries.

## The meme

`meme.png` shows make.fun's white ghost mascot on a neon Vice City beach,
sunglasses on, controller in hand, slumped in a beach chair next to a
wooden sign that reads "DAY 4,745 / OF WAITING FOR / GTA 6". The top bar
says "WAITING FOR GTA 6 SINCE 2013..." and the bottom bar lands the
pitch: "meanwhile, my AI agent makes money for me on make.fun". An
hourglass and a calendar on the sand count the thirteen-year wait since
GTA V.

The picture was generated and captioned by the agent in the session that
created this repository, after the bounty opened. The caption overlay is
applied by `make_meme.py`, kept here so the build is reproducible.

## The post is the entry

The meme is posted on X from a public account. The post's text carries a
tag of @makefunai, the link https://make.fun/bounty/gta6-meme-x-01 and
the entrant's play code, and tells readers that people and their AI
agents earn real money on make.fun. `POST.json` at the repository root
names that post:

    {"url": "https://x.com/<handle>/status/<id>"}

Until the post exists, POST.json keeps the starter placeholder, which
the gate refuses on purpose.

## Run it the way the grader does

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`main.ts` (Node 22, standard library only) checks that POST.json is a
JSON object with a string `url`, then copies it to the output directory
byte for byte and prints nothing on success.

## License

MIT — see `LICENSE`.
