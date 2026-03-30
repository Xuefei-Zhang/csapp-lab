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

The repository includes a baseline GitHub Actions workflow at `.github/workflows/pr-validation.yml`.

It currently runs **compile-only** checks for the labs that can be validated reliably on the untouched starter handouts:

- `cachelab-handout`: `make clean && make csim tracegen`
- `shlab-handout`: `make clean && make`
- `proxylab-handout`: `make clean && make`

This scope is intentionally conservative. Some CS:APP handouts are expected to fail functional tests until you implement the lab, and some other labs require extra runtime/toolchain setup such as `-m32` multilib support or unpacking additional archives.

## Reproducing the current CI checks locally

Run these commands from the repository root:

```bash
make -C cachelab-handout clean
make -C cachelab-handout csim tracegen

make -C shlab-handout clean
make -C shlab-handout

make -C proxylab-handout clean
make -C proxylab-handout
```

## Notes

- The compile-only baseline is meant to keep pull request checks green on the starter code.
- Functional and performance tests can be added later as individual labs are actually implemented.
