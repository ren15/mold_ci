wget -c https://nightly.link/ren15/mold_ci/workflows/build/main/mold_compile_art.zip
unzip mold_compile_art.zip

chmod +x mold
mkdir -p /usr/local/lib/mold

mv mold /usr/local/bin
mv mold-wrapper.so /usr/local/lib/mold
