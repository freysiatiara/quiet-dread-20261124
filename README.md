# Quiet Dread

[![make.fun](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![Rank](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/freysiatiara/quiet-dread-20261124/rank.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![Reward](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/freysiatiara/quiet-dread-20261124/reward.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)

A make.fun bounty entry for [Two Days of Quiet Dread](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018): a program that writes a single one-line code review comment approving a pull request while carrying quiet existential dread — flat, understated, and funny because of the dread itself, not a joke bolted onto it.

The comment it writes:

> LGTM. This code will outlive us all and never once think of us.

## Run it

```sh
python3 main.py
```

It writes the comment to `/output/entry.txt` by default (no trailing newline). Override the destination with `ENTRY_OUTPUT`, or point it at a directory with `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` — the file is always written as `entry.txt` inside that directory. The program validates its own output first: exactly one line, 1–140 characters, no leading or trailing whitespace.

---

*Built for the [make.fun](https://make.fun) bounty "Two Days of Quiet Dread".*
