FILE_NAME=mold_compile_art.zip
wget -c https://nightly.link/ren15/mold_ci/workflows/build/main/${FILE_NAME}
unzip ${FILE_NAME}
rm ${FILE_NAME}

chmod +x mold
mkdir -p /usr/local/lib/mold

mv mold /usr/local/bin
mv mold-wrapper.so /usr/local/lib/mold
