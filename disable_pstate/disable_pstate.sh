sudo python disable_pstate.py /etc/default/grub
sudo mv -f tmp.txt /etc/default/grub
sudo update-grub
