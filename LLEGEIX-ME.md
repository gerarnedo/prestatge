# Prestatge

App web d'un sol fitxer per catalogar els llibres escanejant l'ISBN i saber en quin ordre i a quin prestatge van, segons tres regles: mida (gran / petit) → gènere → alfabètic. L'app és a https://gerarnedo.github.io/prestatge/ i s'actualitza sola quan es fa push a GitHub.

## Posar-la en marxa

1. Obre un Terminal en aquesta carpeta i executa:

       python3 serveix.py

2. Al mòbil, connectat a la mateixa WiFi, obre l'adreça `https://…:8443/` que surt al Terminal.
3. El primer cop el navegador dirà que el certificat no és de confiança (és autosignat, creat al teu Mac). Accepta'l: *Avançat → Continua*.
4. A la pestanya **Escaneja**, prem *Obre la càmera* i dona permís.

Al Mac també funciona a `https://localhost:8443/` (sense càmera de mòbil, però pots escriure l'ISBN a mà).

## Com funciona

- **Escaneja**: llegeix el codi de barres (EAN-13 = ISBN). Consulta Open Library i després Google Books. Et proposa gènere i mida si la font en té dades; tu confirmes la mida (petit fins a 24 cm, gran més de 24 cm) amb un botó i deses. Amb l'assistent activat, el botó «IA» del gènere el suggereix.
- **Assistent**: xat amb Claude que veu el catàleg sencer amb les posicions. Serveix per preguntar on és un llibre, classificar els pendents, o demanar un ordre de gèneres millor. Els canvis que proposa només s'apliquen si prems «Aplica». Funciona amb una clau gratuïta de Groq (console.groq.com/keys, models de codi obert, sense targeta), de Google Gemini (aistudio.google.com/apikey) o, si es vol, amb una clau d'Anthropic de pagament. L'assistent no rep el catàleg sencer: el consulta per parts amb eines de cerca i llistat, per encaixar en els límits gratuïts. La clau es posa a Prestatgeria → Assistent IA i es guarda només al dispositiu. Sense cap clau, el botó «Copia el catàleg» prepara el text per enganxar-lo a qualsevol xat gratuït.
- **Llibres**: llista, cerca, edició. Els llibres sense alçada o gènere es marquen com a *pendents*. Exporta/importa JSON (còpia de seguretat) i CSV.
- **Prestatgeria**: ve predefinida amb els dos prestatges de 95 cm. L'alçada es deixa buida perquè és muntable: l'app la recomana. Aquí també s'ordenen els gèneres i es trien les regles.
- **Ordre**: alçat de la prestatgeria a escala (vista frontal amb les alçades de muntatge i els lloms), i per a cada prestatge, a quina alçada muntar-lo (passos de 5 cm des de 20), dibuix dels lloms i llista numerada de posició. Si no hi cap tot, diu quants cm falten i quins llibres queden fora.

## Dades

Tot es desa al navegador del mòbil (localStorage), no a cap servidor. Dues conseqüències:

- Si l'obres des d'una altra adreça o un altre dispositiu, comença buida. Passa-hi les dades amb *Exporta JSON* → *Importa*.
- Fes *Exporta JSON* de tant en tant (per exemple en acabar cada sessió d'escaneig) i desa el fitxer a Fitxers/Drive. És la teva còpia de seguretat: si esborres dades del navegador, es perd el catàleg.

## Límits coneguts

- Sense clau d'API, Google Books té un límit diari compartit; Open Library no en té. Pots posar una clau pròpia a *Prestatgeria → Fonts de dades*.
- L'alçada real gairebé mai ve a les APIs: la classe d'alçada la tries tu. El gruix s'estima a partir de les pàgines si no el poses.
- L'app necessita internet per consultar les fitxes; la resta funciona sense.
