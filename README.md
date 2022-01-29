# mold_ci

Download and compile mold https://github.com/rui314/mold

Build for linux x64

## Status
Use github action to automate building and host artifacts.
Artifacts is downloadable via link.


## Download the artifacts

For more details, check this [link](https://nightly.link/ren15/mold_ci/workflows/build/main/mold_complie_art)

```bash
bash install.sh

## in any project dir
mold -run make
```

Or better:

```bash
curl -fsSL https://raw.githubusercontent.com/ren15/mold_ci/HEAD/install.sh | bash
```