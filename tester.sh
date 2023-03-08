#! /bin/bash

RESET="\033[0m"
BLACK="\033[1;30m"
RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
BLUE="\033[1;34m"
PURPLE="\033[1;35m"
CYAN="\033[1;36m"
WHITE="\033[1;37m"

LOGFILE="output.log"
TEMPFILE="temp"
TESTS="maps/invalid"

EXEC="so_long"
EXEC_BONUS="so_long_bonus"

# $S1 = path to the project directory
# $S2 = makefile rule to run

log_title()
{
	echo "/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\\" >> $LOGFILE
	echo "|==|                                                        |==|" >> $LOGFILE
	echo "|==|                       $LOGFILE                       |==|" >> $LOGFILE
	echo "|==|              $(date)              |==|" >> $LOGFILE
	echo "|==|                                                        |==|" >> $LOGFILE
	echo "\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/" >> $LOGFILE
}

log_terminal()
{
	if [ $output ]; then
		echo -n "$i: $GREEN"OK"$RESET "  
	else
		echo -n "$i: $RED"KO"$RESET "
	fi
}

log_file()
{
	if [ $output ]; then
		echo "\n[$WHITE#$i$RESET][$GREEN"SUCCESS"$RESET] $CYAN$test_file$RESET\n" >> $LOGFILE 
	else
		echo "\n[$WHITE#$i$RESET][$RED"FAILURE"$RESET] $CYAN$test_file$RESET\n" >> $LOGFILE 
	fi

	# echo "======== START OF OUTPUT ========" >> $LOGFILE
	cat -e $TEMPFILE >> $LOGFILE
	# echo "========= END OF OUTPUT =========" >> $LOGFILE
	if [ ! $output ]; then
		valgrind $path/$program $TESTS/$test_file >> $LOGFILE 2>&1
	fi	
}

compile()
{
	# Remove any previous generated output files
	rm -rf $LOGFILE
	
	# Check for the existence of the Makefile
	if [ ! -f $path/Makefile ]; then
		echo "[$RED"Error"$RESET] No Makefile was found in the \"$path\" directory"
		exit 0
	fi

	echo "[$CYAN"Compilation"$RESET] Compiling your project..."
	make fclean -C $path 1> /dev/null
	make $rule -C $path 1> /dev/null

	# Checks the return value of the make command to assert a successful compilation
	if [ $? -ne 0  ]; then
		echo "[$RED"Error"$RESET] Compilation failed"
		exit 0
	fi

	echo "[$CYAN"Compilation"$RESET] $GREEN"Success"$RESET" && sleep 0.5s
}

execute()
{
	log_title

	i=1
	for test_file in $(ls $TESTS)
	do
		$path/$program $TESTS/$test_file > $TEMPFILE 2>&1
		
		output="$(grep Error $TEMPFILE)"
		log_terminal $i $output
		log_file $i $output $program

		i=$(expr $i + 1)
	done

	rm -rf $TEMPFILE
	echo "\nPlease consult $CYAN$LOGFILE$RESET for detailed information"

}

main()
{
	path=$1
	rule=$2

	compile
	if [ "$rule" = "bonus" ]; then
		program=$EXEC_BONUS
	else 
		program=$EXEC
	fi
	execute 
}

main $1 $2