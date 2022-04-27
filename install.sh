wget -c -q https://github.com/ren15/mold_ci/releases/download/latest/mold.tar.gz
tar xvf mold.tar.gz
chmod +x mold
mkdir -p /usr/local/lib/mold

rm mold.tar.gz
mv mold /usr/local/bin
mv mold-wrapper.so /usr/local/lib/mold