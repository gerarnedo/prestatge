# Prestatge

App d'una sola pàgina per catalogar els llibres (escanejant l'ISBN o a mà) i saber en quin nivell i posició de la prestatgeria van, segons tres regles: mida (gran / petit) → gènere → alfabètic.

Adreça: https://gerarnedo.github.io/prestatge/ (s'actualitza sola quan es fa push a GitHub). Al mòbil, afegeix-la a la pantalla d'inici.

## Les dues pàgines (menú de baix)

- **Afegeix**: càmera per llegir el codi de barres, ISBN a mà, llibre sense ISBN, o col·lecció (enciclopèdies: una sola entrada amb el nombre de volums i el gruix de cada volum). Es consulta Open Library i després Google Books; tu confirmes la mida (petit fins a 24 cm, gran més de 24 cm) i el gènere. En desar, l'app diu on va el llibre: nivell, posició, entre quins llibres, i a quants cm del terra és el tauló.
- **Prestatgeria**: cercador dels llibres que ja tens, alçat del moble a escala (els llibres cercats o l'acabat d'afegir surten ressaltats) i la llista amb la posició de cada llibre. Plegats a sota: la *Guia de muntatge* (nivells, taulons i ordre de cada nivell, imprimible), l'*Assistent* (xat; cal una clau gratuïta de Groq, o «Copia el catàleg» per a qualsevol xat) i els *Ajustos* (mides del moble, alçada fixa dels nivells, ordre dels gèneres, regles, claus).

## El moble (predefinit als Ajustos)

Dues columnes de 95 cm d'ample útil, 223 cm d'alt, la dreta comença 7 cm amunt per l'escaló, taulons de 2 cm, sense tauló a dalt, i 40 cm reservats a baix per als arxivadors. Els nivells tenen alçada fixa: 40 cm els de llibres grans i 25 cm els de petits. L'app només decideix quants nivells van a cada columna i on va cada tauló; l'espai que sobra queda com a nivell lliure a baix.

## Dades

Tot es desa al navegador del mòbil, no a cap servidor. Fes *Exporta JSON* de tant en tant i guarda el fitxer: és la còpia de seguretat, i serveix per passar el catàleg a un altre dispositiu amb *Importa*.

## Servir-la des del Mac (alternativa)

`python3 serveix.py` la serveix per HTTPS a la WiFi de casa; cal acceptar el certificat autosignat el primer cop.
