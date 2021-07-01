import mysql.connector
import typer

app = typer.Typer()

@app.command()
def fetch(fet : str = typer.Argument(default='')):
    mdb = mysql.connector.connect(host='localhost', user='root', password='Postgres@1', database='intelligence')
    cur = mdb.cursor()
    cur.execute(f"SELECT malware_name FROM intelligence.malware WHERE malware_hash = '{fet}'")
    myr = cur.fetchone()
    print(myr[0])

if __name__ == "__main__":
    app()