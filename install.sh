mv name2radec_gui.sh ~/bin/name2radec_gui.sh
mv name2radec.py ~/bin/name2radec.py
chmod 700 ~/bin/name2radec_gui.sh
(echo "#----------------NAME TO R.A. DEC.---------------------")>>~/.bashrc
(echo "alias name2radec="~/bin/name2radec_gui.sh"")>>~/.bashrc
(echo "#----------------NAME TO R.A. DEC.---------------------")>>~/.bashrc
