from rich.console import Console

console = Console()

def printError(text):
    console.print("[!]",text,style="bold red")

def printSuccess(text):
    cosnole.print("[+] ",text,style="bold green")

printError("test")


