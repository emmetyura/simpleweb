cd emmet
python3 ../vidhelper.py > ../vids.html
cd ..

python3 gifhelper.py > .gifs.html

cd p
python3 ../pichelper.py > ../pics.html
cd ..

python3 -m http.server 8080
