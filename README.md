# mold_ci

Download and compile mold https://github.com/rui314/mold

Build for linux x64

## Status
Use github action to automate and host artifacts.
Use python as the build scripting.
Artifacts is downloadable.


## Download the artifacts

For more details, check this [link](https://nightly.link/ren15/mold_ci/workflows/build/main/mold_complie_art)

```bash
wget -c https://nightly.link/ren15/mold_ci/workflows/build/main/mold_complie_art.zip 
unzip mold_compile_art.zip

chmod +x mold
sudo mkdir -p /usr/local/lib/mold

sudo mv mold /usr/local/bin
sudo mv mold-wrapper.so /usr/local/lib/mold

## in any project dir
mold -run make
```

