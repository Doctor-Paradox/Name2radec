a='-g'
if [ -z "$1" ] 
then echo "Please enter valid option..."
echo "For GUI:"
echo "name2radec -g "
echo "For CLI:"
echo "name2radec -c "
elif [ $1 == $a ]
then

Response=$(zenity --entry --text "Enter your search term" --title "Name to R.A. Dec. converter" --entry-text="")
(python ~/bin/name2radec.py $Response || echo "ERROR: NAME NOT FOUND" )| zenity --text-info --title "Name to R.A. Dec. converter" #--width=100 --height=100
else
echo "Enter the name of object"
read ans
python ~/bin/name2radec.py $ans || echo "ERROR: NAME NOT FOUND"
fi
