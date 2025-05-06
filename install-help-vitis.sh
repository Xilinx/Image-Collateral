#!/bin/bash
xmessage-print "This utility copies the webhelp files to the recommended location so that you can access the help from within the Vitis IDE. Click OK to continue."
for i in `ls`; do  cp -R $i $HOME/.Xilinx/Vitis/2024.1/helpdocs/vitis/;  done
rm -Rf  $HOME/.Xilinx/Vitis/2024.1/helpdocs/vitis/install-help-vitis.sh
xmessage -print "Operation Completed! You can now access the Vitis documentation from within the Vitis IDE. Launch the Vitis IDE and select Help - Vitis Documentation."
