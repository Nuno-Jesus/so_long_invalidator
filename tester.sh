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

# Remove any previous generated output files
rm -rf $LOGFILE

# Check for the existence of the Makefile
if [ ! -f $1/Makefile ]; then
	echo "[$RED"Error"$RESET] No Makefile was found in the \"$1\" directory"
	return
fi

echo "[$CYAN"Compilation"$RESET] Compiling your project..."
make re -C $1 1> /dev/null

if [ $? -ne 0  ]; then
	echo "[$RED"Error"$RESET] Compilation failed"
	return
fi

echo "[$CYAN"Compilation"$RESET] $GREEN"Success"$RESET" && sleep 0.5s


echo "/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\-/==\\" >> $LOGFILE
echo "|==|                                                        |==|" >> $LOGFILE
echo "|==|                       $LOGFILE                       |==|" >> $LOGFILE
echo "|==|              $(date)              |==|" >> $LOGFILE
echo "|==|                                                        |==|" >> $LOGFILE
echo "\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/-\==/" >> $LOGFILE

i=1
for test_file in $(ls $TESTS)
do
	echo -n "$i: "
	echo "\n\t--------------------- TEST $i ---------------------\n" >> $LOGFILE
	echo -n "File: \"$test_file\" " >> $LOGFILE
	$1/so_long $1/$test_file > $TEMPFILE 2>&1

	if [ $(grep Error $TEMPFILE) ]; then
		echo -n "$GREEN"OK"$RESET " && echo ✅ >> $LOGFILE 
 	else
		echo -n "$RED"KO"$RESET " && echo ❌ >> $LOGFILE 
	fi
	echo "Output: " >> $LOGFILE
	cat $TEMPFILE >> $LOGFILE
	i=$(expr $i + 1)
done

rm -rf $TEMPFILE
echo "\nPlease consult $CYAN$LOGFILE$RESET for detailed information"