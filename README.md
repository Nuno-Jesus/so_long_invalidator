# Description

This tool was developed to help **42** students, specifically in **so_long**. At the time of the first launch (February 6th 2023), the tool was built using the most up-to-date version of the subject found so far on intra.

This tool is currently **ONLY** performing tests to ensure your project does not support wrongly formatted maps. Make sure you check the [**releases**](https://github.com/Nuno-Jesus/so_long_map_validator/releases) section to keep-up-to date on any new changes.

## This is great, you mind if I use your code?

**You are free to fork the repository and study/modify/test the code on your own**. However, I would really appreciate it if you could text me on Slack (**ncarvalh**) whenever you find a bug or you have a suggestion, so I can properly introduce hotfixes or deploy some quality-of-life patches that can benefit the 42 community in general.

## Are there any pre-requirements?
> Make sure your so_long project has a functional Makefile with all the mandatory rules.

In order to correctly execute the tool, you must:
- have [Python](https://www.python.org/downloads/) installed;
- have either [Ubuntu](https://ubuntu.com/download) or [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) on your computer;
- install [pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/) **ONLY IF** there is a missing package that you might need to install manually (text me, otherwise I won't know);

## Repository contents

<div align = center>

|Folder/File|Description|
|:--:|:--:|
|maps/valid/| Maps that your project should accept |
|maps/invalid/| Maps that your project should not accept (used by the py script) |
|maps/generated/| Generated maps after running the python script |
|generator.py| The python script to automate maps generation |
|tester.sh| The shell script used to fetch the output from your project |

</div>

## Next steps
**1.** Fork/download the code from the repository to any path of your choice in your computer (the best would be to sit right next to your **so_long** folder, like described below)

**2.** If your directory tree looks like this...

```txt
	│
	├── so_long_map_validator	(this directory)
	├── so_long 				(your repository)
	│
	...
```
then you can skip this step. Otherwise, you must change the **PROJ** variable on the **Makefile**. It should look something like this:

```Makefile
	#_/=\_/=\_/=\_/=\_/=\_/=\_/=\_/=\_/=\_/=\_ FOLDERS _/=\_/=\_/=\_/=\_/=\_/=\_/=\_/=\_/=\_/=\_
	PROJ = ../so_long
```

**3.** If you reached this step, you can finally execute it! This project uses a mix of shell and python scripts, so there are no compilations. Also, the Makefile was purposedly developed to easy the management of this programs, so this Makefile will compile yours and execute the tests. 

To compile the mandatory part, your executable must be named as `so_long`

```shell 
make
```

If you need to compile your bonus you must have your executable named as `so_long_bonus` and run the following command:

```shell 
make bonus
```

To generate a new map, use:

```shell 
make gen
```

To clean all the generated maps so far, use:

```shell 
make cleangen
```

The `fclean` and `clean` rules will clean your project object files.

The Makefile was configured to pull updates from the repository, so its ok if it is taking a while to start. After looking for updates, the tool should display something like this:

<div align = center>

| Correct Output |
|:--:|
|![Correct Output](https://user-images.githubusercontent.com/93390807/217015792-6d5bdd6f-4ca6-4e7e-9a4c-9761deb0e802.png)|

</div>

or this, if any misconfiguration of any kind happened:
<div align = center>

| Error Output |
|:--:|
|![Error Output](https://user-images.githubusercontent.com/93390807/217015797-c3455a92-69be-45de-9024-8cb896279614.png)|

</div>

## Generating maps

Alongside with the shell script, there is a generator.py file that can be used to generate a new map, valid or invalid (that's random for now) with given height and width specified by input.

The generated map will be placed inside the [maps/generated](/maps/generated) folder.

A glimpse on how the script should behave

<div align = center>

| Map Generation Script |
|:--:|
|![Map Generation Script](https://user-images.githubusercontent.com/93390807/217015799-e3aabe37-f8ea-4b21-9e94-7496a4825c8c.png)|

</div>

## Author

Nuno Jesus, 42 Porto, ncarvalh

