import typer
from pathlib import Path
import os


def list_rec_files(chemin : Path):
    liste = []
    for f in chemin.iterdir():
        if f.is_file():
            liste.append(f)
        else :
            liste += list_rec_files(f)
    return liste

app = typer.Typer()

@app.command("run")
def run_program(argument : str = typer.Argument(..., help="Cherche les fichiers de l'extenion spésifier"),
                option1 : Path = typer.Argument(Path(__file__).resolve().parent, help = "indique le repértoire où chercher "),
                delete : bool = typer.Option(False, help= "supprimer les fichiers dont l' extension est spécifié")
                ): 
    liste_de_fichier = list_rec_files(Path(f"{option1}"))
    if delete :
        message_confirmation = typer.style("Voulez-vous vraiment supprimer tous les fichiers trouvé",bold=True)
        typer.confirm(message_confirmation, abort=True)
        for i in liste_de_fichier:
            if i.suffix == f".{argument}" : 
                typer.secho(f"Suppression du fichier {i}",fg=typer.colors.RED)
                os.remove(i)
    else :
        liste_de_fichier = list_rec_files(Path(f"{option1}"))
        typer.secho(f"Les fichiers Trouvée de l'extension {argument}:", bg=typer.colors.BLUE, fg=typer.colors.WHITE, bold=True)
        for i in liste_de_fichier:
            if i.suffix == f".{argument}" : 
                typer.echo(i)


@app.command("search")
def search (extension : str = typer.Argument(..., help="Cherche les fichiers de l'extenion spésifier")):
    chemin = Path(__file__).resolve().parent
    liste_de_fichier = list_rec_files(Path(f"{chemin}"))
    typer.secho(f"Les fichiers Trouvée de l'extension {extension}:", bg=typer.colors.BLUE, fg=typer.colors.WHITE, bold=True)
    for i in liste_de_fichier:
        if i.suffix == f".{extension}" : 
            typer.echo(i)
    

@app.command("delete")
def supprimer(extension : str = typer.Argument(..., help="Cherche les fichiers de l'extenion spésifier")):
    chemin = Path(__file__).resolve().parent
    liste_de_fichier = list_rec_files(Path(f"{chemin}"))
    message_confirmation = typer.style("Voulez-vous vraiment supprimer tous les fichiers trouvé",bold=True)
    typer.confirm(message_confirmation, abort=True)
    for i in liste_de_fichier:
            if i.suffix == f".{extension}" : 
                typer.secho(f"Suppression du fichier {i}",fg=typer.colors.RED)
                os.remove(i)


if __name__=="__main__":
    app()