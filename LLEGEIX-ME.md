# Prestatge

App web d'un sol fitxer per catalogar els llibres escanejant l'ISBN i saber en quin ordre i a quin prestatge van, segons tres regles: alçada → gènere → alfabètic.

## Posar-la en marxa

1. Obre un Terminal en aquesta carpeta i executa:

       python3 serveix.py

2. Al mòbil, connectat a la mateixa WiFi, obre l'adreça `https://…:8443/` que surt al Terminal.
3. El primer cop el navegador dirà que el certificat no és de confiança (és autosignat, creat al teu Mac). Accepta'l: *Avançat → Continua*.
4. A la pestanya **Escaneja**, prem *Obre la càmera* i dona permís.

Al Mac també funciona a `https://localhost:8443/` (sense càmera de mòbil, però pots escriure l'ISBN a mà).

## Com funciona

- **Escaneja**: llegeix el codi de barres (EAN-13 = ISBN). Consulta Open Library i després Google Books. Et proposa gènere i classe d'alçada si la font en té dades; tu confirmes la classe d'alçada amb un botó i deses.
- **Llibres**: llista, cerca, edició. Els llibres sense alçada o gènere es marquen com a *pendents*. Exporta/importa JSON (còpia de seguretat) i CSV.
- **Prestatgeria**: ve predefinida amb els dos prestatges de 95 cm. L'alçada es deixa buida perquè és muntable: l'app la recomana. Aquí també s'ordenen els gèneres i es trien les regles.
- **Ordre**: per a cada prestatge, a quina alçada muntar-lo (passos de 5 cm des de 20), dibuix dels lloms i llista numerada de posició. Si no hi cap tot, diu quants cm falten i quins llibres queden fora.

## Dades

Tot es desa al navegador del mòbil (localStorage), no a cap servidor. Dues conseqüències:

- Si l'obres des d'una altra adreça o un altre dispositiu, comença buida. Passa-hi les dades amb *Exporta JSON* → *Importa*.
- Fes *Exporta JSON* de tant en tant (per exemple en acabar cada sessió d'escaneig) i desa el fitxer a Fitxers/Drive. És la teva còpia de seguretat: si esborres dades del navegador, es perd el catàleg.

## Límits coneguts

- Sense clau d'API, Google Books té un límit diari compartit; Open Library no en té. Pots posar una clau pròpia a *Prestatgeria → Fonts de dades*.
- L'alçada real gairebé mai ve a les APIs: la classe d'alçada la tries tu. El gruix s'estima a partir de les pàgines si no el poses.
- L'app necessita internet per consultar les fitxes; la resta funciona sense.
