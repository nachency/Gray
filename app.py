# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from datetime import datetime

# from flask import request

# CHANGE ALL THE PEOPLE NAMES TO ALL THE COUNTRY NAMES !!!!!!!!!!!!!!
# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())


@app.route('/asia')
def asia():
    return render_template('asia.html', time=datetime.now())


@app.route('/asia/afganistan')
def asiaafganistan():
    return render_template('asia/afganistan.html', time=datetime.now())


@app.route('/asia/armenia')
def asiaarmenia():
    return render_template('asia/armenia.html', time=datetime.now())


@app.route('/asia/azerbaijan')
def asiaazerbaijan():
    return render_template('asia/azerbaijan.html', time=datetime.now())


@app.route('/asia/bahrain')
def asiabahrain():
    return render_template('asia/bahrain.html', time=datetime.now())


@app.route('/asia/bangladesh')
def asiabangladesh():
    return render_template('asia/bangladesh.html', time=datetime.now())


@app.route('/asia/bhutan')
def asiabhutan():
    return render_template('asia/bhutan.html', time=datetime.now())


@app.route('/asia/brunei')
def asiabrunei():
    return render_template('asia/brunei.html', time=datetime.now())


@app.route('/asia/burma')
def asiaburma():
    return render_template('asia/burma.html', time=datetime.now())


@app.route('/asia/cambodia')
def asiacambodia():
    return render_template('asia/cambodia.html', time=datetime.now())


@app.route('/asia/china')
def asiachin():
    return render_template('asia/china.html', time=datetime.now())


@app.route('/asia/cyprus')
def asiacyprus():
    return render_template('asia/cyprus.html', time=datetime.now())


@app.route('/asia/eastTimor')
def asiaeastTimor():
    return render_template('asia/eastTimor.html', time=datetime.now())


@app.route('/asia/georgia')
def asiageorgia():
    return render_template('asia/georgia.html', time=datetime.now())


@app.route('/asia/hongkong')
def asiahongkong():
    return render_template('asia/hongkong.html', time=datetime.now())


@app.route('/asia/india')
def asiaindia():
    return render_template('asia/india.html', time=datetime.now())


@app.route('/asia/indonesia')
def asiaindonesia():
    return render_template('asia/indonesia.html', time=datetime.now())


@app.route('/asia/iran')
def asiairan():
    return render_template('asia/iran.html', time=datetime.now())


@app.route('/asia/iraq')
def asiairaq():
    return render_template('asia/iraq.html', time=datetime.now())


@app.route('/asia/israel')
def asiaisrael():
    return render_template('asia/israel.html', time=datetime.now())


@app.route('/asia/japan')
def asiajapan():
    return render_template('asia/japan.html', time=datetime.now())


@app.route('/asia/jordan')
def asiajordan():
    return render_template('asia/jordan.html', time=datetime.now())


@app.route('/asia/kazakhstan')
def asiakazakhstan():
    return render_template('asia/kahzakhstan.html', time=datetime.now())


@app.route('/asia/kuwait')
def asiakuwait():
    return render_template('asia/kuwait.html', time=datetime.now())


@app.route('/asia/kyrgyzstan')
def asiakyrgyzstan():
    return render_template('asia/kyrgyzstan.html', time=datetime.now())


@app.route('/asia/laos')
def asialaos():
    return render_template('asia/laos.html', time=datetime.now())


@app.route('/asia/lebanon')
def asialebanon():
    return render_template('asia/lebanon.html', time=datetime.now())


@app.route('/asia/malaysia')
def asiamalaysia():
    return render_template('asia/malaysia.html', time=datetime.now())


@app.route('/asia/myanmar')
def asiamyanmar():
    return render_template('asia/myanmar.html', time=datetime.now())


@app.route('/asia/mongolia')
def asiamongolia():
    return render_template('asia/mongolia.html', time=datetime.now())


@app.route('/asia/nepal')
def asianepal():
    return render_template('asia/nepal.html', time=datetime.now())


@app.route('/asia/northKorea')
def asiakorea():
    return render_template('asia/korea.html', time=datetime.now())


@app.route('/asia/oman')
def asiaoman():
    return render_template('asia/oman.html', time=datetime.now())


@app.route('/asia/pakistan')
def asiapakistan():
    return render_template('asia/pakistan.html', time=datetime.now())


@app.route('/asia/papuaNewGuinea')
def asiapapuaNewGuinea():
    return render_template('asia/papuaNewGuinea.html', time=datetime.now())


@app.route('/asia/philippines')
def asiaphilippines():
    return render_template('asia/philippines.html', time=datetime.now())


@app.route('/asia/qatar')
def asiaqatar():
    return render_template('asia/qatar.html', time=datetime.now())


@app.route('/asia/russia')
def asiarussia():
    return render_template('asia/russia.html', time=datetime.now())


@app.route('/asia/saudiArabia')
def asiasaudiArabia():
    return render_template('asia/saudiArabia.html', time=datetime.now())


@app.route('/asia/singapore')
def asiasingapore():
    return render_template('asia/singapore.html', time=datetime.now())


@app.route('/asia/southKorea')
def asiasouthKorea():
    return render_template('asia/southKorea.html', time=datetime.now())


@app.route('/asia/sriLanka')
def asiasriLanka():
    return render_template('asia/sriLanka.html', time=datetime.now())


@app.route('/asia/syria')
def asiasyria():
    return render_template('asia/syria.html', time=datetime.now())


@app.route('/asia/taiwan')
def asiataiwan():
    return render_template('asia/taiwan.html', time=datetime.now())


@app.route('/asia/tajikstan')
def asiatajikstan():
    return render_template('asia/tajikstan.html', time=datetime.now())


@app.route('/asia/thailand')
def asiathailand():
    return render_template('asia/thailand.html', time=datetime.now())


@app.route('/asia/turkey')
def asiaturkey():
    return render_template('asia/turkey.html', time=datetime.now())


@app.route('/asia/turkmenistan')
def asiaturkmenistan():
    return render_template('asia/turkmenistan.html', time=datetime.now())


@app.route('/asia/unitedArabEmirates')
def asiaunitedArabEmirates():
    return render_template('asia/unitedArabEmirates.html', time=datetime.now())


@app.route('/asia/uzbekistan')
def asiauzbekistan():
    return render_template('asia/uzbekistan.html', time=datetime.now())


@app.route('/asia/vietnam')
def asiavietnam():
    return render_template('asia/vietnam.html', time=datetime.now())


@app.route('/asia/yemen')
def asiayemen():
    return render_template('asia/yemen.html', time=datetime.now())


# LATIN AMERICA
@app.route('/latinAmerica')
def latinAmerica():
    return render_template('latinAmerica.html', time=datetime.now())


@app.route('/latinAmerica/antiguaAndBarbuda')
def latinAmericaantiguaAndBarbuda():
    return render_template('latinAmerica/antiguaAndBarbuda.html', time=datetime.now())


@app.route('/latinAmerica/argentina')
def latinAmericaargentina():
    return render_template('latinAmerica/argentina.html', time=datetime.now())


@app.route('/latinAmerica/bahamas')
def latinAmericabahamas():
    return render_template('latinAmerica/bahamas.html', time=datetime.now())


@app.route('/latinAmerica/barbados')
def latinAmericabarbados():
    return render_template('latinAmerica/barbados.html', time=datetime.now())


@app.route('/latinAmerica/belize')
def latinAmericabelize():
    return render_template('latinAmerica/belize.html', time=datetime.now())


@app.route('/latinAmerica/bolivia')
def latinAmericabolivia():
    return render_template('latinAmerica/bolivia.html', time=datetime.now())


@app.route('/latinAmerica/brazil')
def latinAmericabrazil():
    return render_template('latinAmerica/brazil.html', time=datetime.now())


@app.route('/latinAmerica/chile')
def latinAmericachile():
    return render_template('latinAmerica/chile.html', time=datetime.now())


@app.route('/latinAmerica/colombia')
def latinAmericacolombia():
    return render_template('latinAmerica/colombia.html', time=datetime.now())


@app.route('/latinAmerica/costaRica')
def latinAmericacostaRica():
    return render_template('latinAmerica/costaRica.html', time=datetime.now())


@app.route('/latinAmerica/cuba')
def latinAmericacuba():
    return render_template('latinAmerica/cuba.html', time=datetime.now())


@app.route('/latinAmerica/dominica')
def latinAmericadominica():
    return render_template('latinAmerica/dominica.html', time=datetime.now())


@app.route('/latinAmerica/dominicanRepublic')
def latinAmericadominicanRepublic():
    return render_template('latinAmerica/dominicanRepublic.html', time=datetime.now())


@app.route('/latinAmerica/ecuador')
def latinAmericaecuador():
    return render_template('latinAmerica/ecuador.html', time=datetime.now())


@app.route('/latinAmerica/elSalvador')
def latinAmericaelSalvador():
    return render_template('latinAmerica/elSalvador.html', time=datetime.now())


@app.route('/latinAmerica/grenada')
def latinAmericagrenada():
    return render_template('latinAmerica/grenada.html', time=datetime.now())


@app.route('/latinAmerica/guatemala')
def latinAmericaguatemala():
    return render_template('latinAmerica/guatemala.html', time=datetime.now())


@app.route('/latinAmerica/guyana')
def latinAmericaguyana():
    return render_template('latinAmerica/guyana.html', time=datetime.now())


@app.route('/latinAmerica/haiti')
def latinAmericahaiti():
    return render_template('latinAmerica/haiti.html', time=datetime.now())


@app.route('/latinAmerica/honduras')
def latinAmericahonduras():
    return render_template('latinAmerica/honduras.html', time=datetime.now())


@app.route('/latinAmerica/jamaica')
def latinAmericajamaica():
    return render_template('latinAmerica/jamaica.html', time=datetime.now())


@app.route('/latinAmerica/mexico')
def latinAmericamexico():
    return render_template('latinAmerica/mexico.html', time=datetime.now())


@app.route('/latinAmerica/nicaragua')
def latinAmericanicaragua():
    return render_template('latinAmerica/nicaragua.html', time=datetime.now())


@app.route('/latinAmerica/saintKitts&Nevis')
def latinAmericasaintKittsAndNevis():
    return render_template('latinAmerica/saintKitts&Nevis.html', time=datetime.now())


@app.route('/latinAmerica/saintLucia')
def latinAmericasaintLucia():
    return render_template('latinAmerica/saintLucia.html', time=datetime.now())


@app.route('/latinAmerica/stVincent&Grenadines')
def latinAmericastVincentAndGrenadines():
    return render_template('latinAmerica/stVincent&Grenadines.html', time=datetime.now())


@app.route('/latinAmerica/suriname')
def latinAmericasuriname():
    return render_template('latinAmerica/suriname.html', time=datetime.now())


@app.route('/latinAmerica/trinidadAndTobago')
def latinAmericatrinidadAndTobago():
    return render_template('latinAmerica/trinidadAndTobago.html', time=datetime.now())


@app.route('/latinAmerica/panama')
def latinAmericamexicopanama():
    return render_template('latinAmerica/panama.html', time=datetime.now())


@app.route('/latinAmerica/paraguay')
def latinAmericaparaguay():
    return render_template('latinAmerica/paraguay.html', time=datetime.now())


@app.route('/latinAmerica/peru')
def latinAmericaperu():
    return render_template('latinAmerica/peru.html', time=datetime.now())


@app.route('/latinAmerica/uruguay')
def latinAmericauruguay():
    return render_template('latinAmerica/uruguay.html', time=datetime.now())


@app.route('/latinAmerica/venezuela')
def latinAmericavenezuela():
    return render_template('latinAmerica/venezuela.html', time=datetime.now())


# LATIN AMERICA DEPENDENCIES

@app.route('/latinAmerica/anguilla')
def latinAmericaanguilla():
    return render_template('latinAmerica/anguilla.html', time=datetime.now())


@app.route('/latinAmerica/aruba')
def latinAmericaaruba():
    return render_template('latinAmerica/aruba.html', time=datetime.now())


@app.route('/latinAmerica/britishVirginIslands')
def latinAmericabritishVirginIslands():
    return render_template('latinAmerica/britishVirginIslands.html', time=datetime.now())


@app.route('/latinAmerica/caribbeanNetherlands')
def latinAmericacaribbeanNetherlands():
    return render_template('latinAmerica/caribbeanNetherlands.html', time=datetime.now())


@app.route('/latinAmerica/caymanIslands')
def latinAmericacaymanIslands():
    return render_template('latinAmerica/puertoRico.html', time=datetime.now())


@app.route('/latinAmerica/curacao')
def latinAmericacuracao():
    return render_template('latinAmerica/curacao.html', time=datetime.now())


@app.route('/latinAmerica/falklandIslands')
def latinAmericafalklandIslands():
    return render_template('latinAmerica/falklandIslands.html', time=datetime.now())


@app.route('/latinAmerica/frenchGuiana')
def latinAmericafrenchGuiana():
    return render_template('latinAmerica/frenchGuiana.html', time=datetime.now())


@app.route('/latinAmerica/guadeloupe')
def latinAmericaguadelope():
    return render_template('latinAmerica/guadelope.html', time=datetime.now())


@app.route('/latinAmerica/martinique')
def latinAmericamartinique():
    return render_template('latinAmerica/martinique.html', time=datetime.now())


@app.route('/latinAmerica/montserrat')
def latinAmericamontserrat():
    return render_template('latinAmerica/montserrat.html', time=datetime.now())


@app.route('/latinAmerica/sintMaarten')
def latinAmericasintMaarten():
    return render_template('latinAmerica/sintMaarten.html', time=datetime.now())


@app.route('/latinAmerica/turksAndCaicos')
def latinAmericaturksAndCaicos():
    return render_template('latinAmerica/turksAndCaicos.html', time=datetime.now())


@app.route('/latinAmerica/USVirginIslands')
def latinAmericaUSVirginIslands():
    return render_template('latinAmerica/USVirginIslands.html', time=datetime.now())


@app.route('/latinAmerica/puertoRico')
def latinAmericapuertoRico():
    return render_template('latinAmerica/puertoRico.html', time=datetime.now())
