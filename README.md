# CS:APP Lab Handouts

This repository contains self-study handout materials from the CS:APP 3e lab page, unpacked into separate directories.

## Included labs

- `datalab-handout/`
- `bomb/`
- `target1/`
- `buflab32-handout/`
- `archlab-handout/`
- `archlab32-handout/`
- `cachelab-handout/`
- `perflab-handout/`
- `shlab-handout/`
- `malloclab-handout/`
- `proxylab-handout/`

## GitHub Actions PR validation

The repository includes a GitHub Actions workflow at `.github/workflows/pr-validation.yml`.

It currently validates all included lab groups, using the lightest check that is stable for each handout type:

- `cachelab-handout`: compile `csim` and `tracegen`
- `datalab-handout`: 32-bit build of `btest` plus `./dlc bits.c`
- `malloclab-handout`: 32-bit build of `mdriver` plus `./mdriver -f short1-bal.rep`
- `perflab-handout`: 32-bit build of `driver` plus `./driver -t -g`
- `archlab-handout`: verify `sim.tar` exists and is a valid tar archive file
- `archlab32-handout`: verify `sim.tar` exists and is a valid tar archive file
- `bomb/`: smoke-test the `bomb` binary startup path
- `target1/` (attacklab instance): smoke-test `ctarget`, `rtarget`, and `hex2raw`
- `buflab32-handout/`: verify binary dependencies for `bufbomb` and `makecookie`, plus a light `hex2raw` smoke test
- `shlab-handout`: compile starter programs
- `proxylab-handout`: compile `proxy`

The workflow intentionally mixes compile checks, smoke tests, and archive validation. Some handouts are starter code that will not pass full correctness tests until the lab is implemented, while others are distributed as prebuilt binaries or archived simulator sources.

## Reproducing the current CI checks locally

Run these commands from the repository root:

```bash
make -C cachelab-handout clean
make -C cachelab-handout csim tracegen

sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y build-essential gcc-multilib libc6-dev-i386 libc6:i386

make -C datalab-handout clean
make -C datalab-handout btest
(cd datalab-handout && ./dlc bits.c)

make -C malloclab-handout clean
make -C malloclab-handout mdriver
(cd malloclab-handout && ./mdriver -f short1-bal.rep)

make -C perflab-handout clean
make -C perflab-handout driver
(cd perflab-handout && ./driver -t -g)

test -s archlab-handout/sim.tar
file archlab-handout/sim.tar | grep -i 'tar archive'

test -s archlab32-handout/sim.tar
file archlab32-handout/sim.tar | grep -i 'tar archive'

(cd bomb && printf '' | ./bomb > bomb-smoke.out 2>&1 || true)

(cd target1 && ./ctarget -h && ./rtarget -h && ./hex2raw < /dev/null > /dev/null 2>&1 || true)

ldd buflab32-handout/bufbomb
ldd buflab32-handout/makecookie
./buflab32-handout/hex2raw < /dev/null > /dev/null 2>&1 || true

make -C shlab-handout clean
make -C shlab-handout

make -C proxylab-handout clean
make -C proxylab-handout
```

## Notes

- The source-based 32-bit labs require multilib packages on CI runners.
- The architecture labs are currently validated via `sim.tar` presence/type checks rather than full simulator builds.
- The bomb / attack / buflab groups are distributed primarily as prebuilt binaries, so CI focuses on smoke and dependency checks instead of full source builds.
