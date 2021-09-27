# Generates changelogs based on git repo.
#
# Credits to Krutoy242 @ github for making this in javascript
# wake-code @ github ported this file to python.
# Original link: https://github.com/Krutoy242/Enigmatica2Expert-Extended/blob/master/dev/automation/changelog.js

import asyncio
import colorama
import click

colorama.init()

ALL_CONFLICTS = []


def no_conflicts():
    click.echo(f"  {colorama.Fore.LIGHTBLUE_EX}.. No conflicts found!")


async def init():
    click.echo(f" {colorama.Fore.LIGHTBLUE_EX}.. Checking for recipe conflicts")

    CRAFTTWEAKER_LOG = open("crafttweaker.log", encoding="utf-8")
    CONFLICTING_START_TEXT = "[SERVER_STARTED][SERVER][INFO] Conflicting: \n"

    for idx, line in enumerate(CRAFTTWEAKER_LOG, start=1):
        if line in CONFLICTING_START_TEXT:
            print("found conflicts")
        elif line not in CONFLICTING_START_TEXT:
            return no_conflicts()


def main():
    asyncio.run(init())


if __name__ == "__main__":
    main()
