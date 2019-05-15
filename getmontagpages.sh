curl https://www.montag.wtf/ -o ~/Desktop/montagpages/montagpage1.html
for p in {2..27}
do
  curl https://www.montag.wtf/page/$p/ -o ~/Desktop/montagpages/montagpage$p.html
done 
