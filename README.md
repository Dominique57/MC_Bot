# MC_bot: Discord Minecraft Bot

Personnal project which aims to manage a computer from another computer.
This makes a lot of sense when for instance the managed computer is ernergy
consumming and the manager isn't.

## What is it ?

This is a small python discord bot that runs on the manager and the managed 
computer and listen to discord requests. For each requests, the managed may 
handle them for actions such as reboot, start services, etc..., and the 
manager must check if they are correctly formed and handle special requests 
such as reboot.

## Setup

To be able to compile and run the program you need :
- [Python](https://www.python.org/) (Language runtime)
- [Pip](https://pypi.org/project/pip/) (Package Manager)
- Install the requirements.txt using pip
```bash
42sh$ pip install -r requirements.txt
```
## Usage

### Running the program

It is recommanded to create a service which will run when
starting the computer.

No docker image has been supplied since docker doesn't allow
sending magic packets for WOL.

```bash
42sh$ python minecraft.py
```

## Known issues
> None for the moment, that's great

## Contributions
- Dominique MICHEL <dominique.michel@epita.fr>
