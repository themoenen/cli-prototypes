<!--&rarr;-->

# IBMAD CLI

Documentation on the top level functionality of **ibmad** - the IBM Discovery Platform common CLI.

This document is meant as the single-source-of-truth based on which we'll build out the ibmad functionality. As such, functionality described in this document is representing what we **intend** to build, as opposed to what has _already_ been built.

## About

The ibmad shell is an umbrella CLI that exposes DS4SD, GT4SD, ST4SD and RXN through a unified interface.

### Objective
 
 - **Provide homogenized access** to the different modules
	 - Lower the bar for learning nomenclature and functionality patterns
	 - Making it easier to work across modules
	 - Have a singlar authentication
 - **Provide additional value**
	 - Out-of-the-box domain-specific functionality, hiding much of the complexity.
	 - A superb user experience, Eg:
		 - More user-friendly menu-like navigation
		 - Integrated web-browser UI (for previewing molecules, data, etc.)
		 - Ability to run scripts via Jupyter
	 - Extensive and integrated documentation
		 - Via the standard --help flag
		 - Via centralized documentation at [accelerate.science/docs](https://accelerate.science/docs)

<br><br>
## Installation
- Requirements:
	
		Python 3.x.x

- Installation:
	
		pip install ibmad

<br><br>
<span style="color:#d00">To discuss:</span><br>

- Will there be anything more to it?
- Maybe instructions on how to set up a virtualenv?
- Can we build this in Python 3.11?

<br><br>
## Basic commands
<!--<span style="color:#07b">Input</span>-->

	ibmad

<span style="color:#094">Output:</span> Welcome message and high-level overview.
<br><br>


	ibmad ds
	ibmad gt
	ibmad st
	ibmad dc

<span style="color:#094">Output:</span> High-level overview per module.
<br><br>

	ibmad --help
	ibmad ds --help

<span style="color:#094">Output:</span> Overview of the available commands & parameters.

<br>
### Accessing module functionality

Use any function from any module:

	ibmad gt inference --foo=bar

Switch to a module context:

	ibmad enter gt
	(gt) inference --foo=bar


Switch between modules:
	
	(gt) enter ds
	(ds) enter dc
	(dc) ...

Exit from a module context (alternative options):
	
	(dc) exit
	(dc) enter ibmad


<br><br>
<span style="color:#d00">To discuss:</span><br>
	
- Can it be possible to access functionality from a different module without switching contexts? And how trivial would an implementation be? For example:
	
		(ds) gt inference --foo=bar
- If we make this possible, will there be any complications, eg. regarding where we write the files?


<br><br>
## Project management

We're standardizing the project architecture, which is already implemented in RXN and... <span style="color:#d00">??</span><br>

<span style="color:#07b">Input</span>

	list projects
	
<span style="color:#094">Output</span>

	# FPO
	
	Name     Files    Last edit
	-----    -----    ------------
	Sun         23    Apr 11, 2023
	Earth        1    Apr 01, 2023
	Moon         7    Mar 16, 2023
	Mars       134    Mar 16, 2023

<span style="color:#07b">Input</span>

	create project foobar
	
<span style="color:#094">Output</span>

	?

<br><br>
<span style="color:#d00">To discuss:</span><br>

- Can we list the project name in the CLI start string?
- Do we force user to create a project before they can do anything?


<br><br>
<span style="color:#d00">To discuss (Karl?):</span><br>

- What other modules aside from RXN havw this implemented
- Is Narciso still the person who owns this decision making?
- Has the homogenized project architecture been properly thought through?
- For example, is an RXN project in today's GUI the same as a project in the CLI?
- Is there any documentation for the project architecture (how it's structured, how it works)
- Is there a general single-source-of-truth regarding the architecture, similar to this doc for the CLI?

