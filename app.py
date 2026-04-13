from flask import Flask, render_template

app = Flask(__name__)

hayvonlar = ["Sher", "Fil", "Tulki", "Bo'ri", "Quyon", "Maymun"]

@app.route('/hayvonlar/<int:i>/taqqosla')
def hayvon_taqqosla(i):
    if 0 <= i < len(hayvonlar):
        hayvon = hayvonlar[i]
        uzunlik = len(hayvon)

        # barcha uzunliklar
        uzunliklar = [len(h) for h in hayvonlar]

        if uzunlik == max(uzunliklar):
            natija = "Eng uzun"
        elif uzunlik == min(uzunliklar):
            natija = "Eng qisqa"
        else:
            natija = "O'rtacha"

        return render_template(
            'taqqosla.html',
            hayvon=hayvon,
            uzunlik=uzunlik,
            natija=natija
        )
    else:
        return "Noto'g'ri indeks ❌"


if __name__ == "__main__":
    app.run(debug=True)
