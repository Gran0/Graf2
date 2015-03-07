__author__ = 'Lukas Granzer'

from flask import Flask, request, render_template
from random import randrange

app = Flask(__name__)

@app.route("/graf", methods=['GET', 'POST'])
def dalsi():
    popisek = "Venkovni teplota behem roku 2015"
    napoveda = "Kliknutim a tazenim mysi lze priblizit danou oblast grafu"
    popisekYosy = "Teplota v mistnosti"
    komentBublina = "Teplota C"
    teploty = ""
    y = 0

    for x in range(0,356, 1):                       #nahodny generator teplot
        y += (randrange(0, 50, 1) - 25)/10.0
        teploty = teploty + str(y)+", "

    html_graf = "<div id=\"prvni_graf\" style=\"height: 500px;width=100%\"><!--Tady se vykresli graf. --></div>"

    dataKodeslani = {'popisek': popisek, 'napoveda': napoveda, 'popisekYosy': popisekYosy, 'komentBublina': komentBublina, 'teploty': teploty}

    if request.method == "GET":                      # pozadavek na zaslani stranky
        return render_template("druha.tmpl",data=dataKodeslani)

    if request.method == "POST":                    # tzn. byla odeslana nejaka data z formulare
        parametr = request.form['tlacitko'].strip()
        if parametr == "Zobrazit informacni zpravu":
            return render_template("druha.tmpl", text="Tato stranka byla vygenerovana Flaskem.", data=dataKodeslani)

        if parametr == "Zobraz graf":
            return render_template("druha.tmpl", data=dataKodeslani, text="Data odeslana", html_graf=html_graf)


@app.route('/', methods=['GET', 'POST'])
def index():
    zprava = "Vita te Python na teto strance.:D"
    if request.method == "GET":  # prvni nacteni stranky
        return render_template("index.tmpl")
    else:
        return render_template("index.tmpl", text=zprava)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=int("5000"))  # adresa a port, na ktere se ma stranka zobrazit

