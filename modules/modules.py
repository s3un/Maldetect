import pefile
import typer

app = typer.Typer(add_completion=False, )

@app.command("iM")
def impha(filepath : str = typer.Argument(default='')):
    """
    - Provides import hash information
    """
    pe = pefile.PE(filepath)
    hasp = pe.get_imphash()
    print("[+] Import Hash: ", hasp)


@app.command("cS")
def check_sum(check_su : str = typer.Argument(default='')):
    """
    - Generate file check sum information
    """
    pe = pefile.PE(check_su)
    hasp = pe.generate_checksum()

    print("[+] Checksum hash: ", hasp)


@app.command("O")
def outpu(fp : str = typer.Argument(default='')):
    """
        - Save output
    """
    fp = open("output.txt", "w")
    fp.close()

@app.command("iM")
def importv(im_hash : str = typer.Argument(default="")):
    """
    - Displays dynamic libraries used by the application and their
        import function
    """
    im_look = pefile.PE(im_hash)
    if hasattr(im_look, "DIRECTORY_ENTRY_IMPORT"):
        for key in im_look.DIRECTORY_ENTRY_IMPORT:
            print("[+] Imported dynamic library and functions")
            print("[+] Dynamic Library", key.dll)
            for imp in key.imports:
                if imp.name != None:
                    print(imp.name)
                else:
                    print(imp.ordinal)
            print("\n")

@app.command("eX")
def search():
    print("work in progress")


if __name__ == "__main__":
   app()

