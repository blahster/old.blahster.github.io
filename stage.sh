make clean
rm -fr author/ category/ tag/ theme/
make html
if [ -d "output" ]; then
    mv output/* .
else
   echo 'output directory not found'
fi
make clean
