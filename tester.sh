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

compile()
{
	path=$1
	rule=$2

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
	path=$1
	program=$2

	echo This is the program: $program

	i=1
	for test_file in $(ls $TESTS)
	do
		echo -n "$i: "
		echo "\n\t--------------------- TEST $i ---------------------\n" >> $LOGFILE
		echo -n "File: \"$test_file\" " >> $LOGFILE
		$path/$program $TESTS/$test_file > $TEMPFILE 2>&1
		
		if [ "$(grep Error $TEMPFILE)" ]; then
			echo -n "$GREEN"OK"$RESET " && echo ✅ >> $LOGFILE 
			echo "-------- START OF OUTPUT --------" >> $LOGFILE
			cat -e $TEMPFILE >> $LOGFILE
			echo "--------- END OF OUTPUT ---------" >> $LOGFILE
		else
			echo -n "$RED"KO"$RESET " && echo ❌ >> $LOGFILE
			valgrind $path/so_long $TESTS/$test_file >> $LOGFILE 2>&1
		fi
		i=$(expr $i + 1)
	done

	rm -rf $TEMPFILE
	echo "\nPlease consult $CYAN$LOGFILE$RESET for detailed information"

}

main()
{
	compile $1 $2
	if [ "$2" = "bonus" ]; then
		execute $1 $EXEC_BONUS
	else 
		execute $1 $EXEC
	fi
}

main $1 $2