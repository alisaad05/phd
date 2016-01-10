:: Ali SAAD 2014
:: Script to create an animation from the command line using MEncoder command (MPlayer)

echo off

:: Output the sorted (by name) list of image files
dir /b /o *.png > files.txt

:: Call mencoder (executable directory is pointed in environment variables)
mencoder mf://@files.txt -mf type=png:w=800:h=600:fps=10 -ovc lavc -lavcopts vcodec=mpeg4 -oac copy -o my_animation.avi


echo %CD%
pause