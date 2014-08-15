#!/bin/bash
#
# Effects Script for ZevenOS by Leszek Lesner
if [ -e ~/.compmgr_fadein ] && [ -e ~/.compmgr_shadow ]
then
	xcompmgr -c -f -C -F &
elif [ -e ~/.compmgr_fadein ]
then
 	xcompmgr -f -F &
elif [ -e ~/.compmgr_shadow ]
then
  	xcompmgr -c -C &
else
	xcompmgr &
fi
