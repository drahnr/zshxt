# waf buildsystem basic command completion

_waf_get_command_list () {
	local -a commands 
	commands=$(./waf --help | awk '/$[[:space:]]*^/{if(e==0){e++;next}else if(e==2){e=777}} e==1{e++;next} {if(e==2){print}}' | sed -e "s/^[[:space:]]*\([A-Za-z][A-Za-z0-9]*\)[[:space:]]*\:.*/\1/g" )
	echo $commands
}

_waf () {
	compadd $(_waf_get_command_list)
}

compdef _waf waf
