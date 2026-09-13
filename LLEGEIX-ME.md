# Prestatge

App d'una sola pàgina per catalogar els llibres (escanejant l'ISBN o a mà) i saber en quin nivell i posició de la prestatgeria van, segons tres regles: mida (gran / petit) → gènere → alfabètic.

Adreça: https://gerarnedo.github.io/prestatge/ (s'actualitza sola quan es fa push a GitHub). Al mòbil, afegeix-la a la pantalla d'inici.

## Les quatre parts de la pàgina

- **Afegeix llibres**: càmera per llegir el codi de barres, ISBN a mà, llibre sense ISBN, o col·lecció (enciclopèdies: una sola entrada amb el nombre de volums i el gruix de cada volum). Es consulta Open Library i després Google Books. Tu confirmes la mida (petit fins a 24 cm, gran més de 24 cm) i el gènere.
- **Prestatgeria**: alçat del moble a escala des del terra (dues columnes, escaló, arxivadors ratllats, nivells amb els lloms) i, per a cada nivell, a quants cm del terra va el tauló i la llista numerada de llibres. Als *Ajustos* hi ha les mides del moble, l'alçada fixa dels nivells (40 cm grans, 25 cm petits), l'ordre dels gèneres, les regles i la clau de l'assistent.
- **Llibres**: llista amb cerca, posició de cada llibre, edició, exportació JSON/CSV i importació.
- **Assistent**: xat per preguntar on és un llibre, classificar pendents o demanar canvis d'ordre; només aplica canvis si prems «Aplica». Cal una clau gratuïta de Groq (console.groq.com/keys). Sense clau, «Copia el catàleg» prepara el text per a qualsevol xat.

## El moble (predefinit als Ajustos)

Dues columnes de 95 cm d'ample útil, 223 cm d'alt, la dreta comença 7 cm amunt per l'escaló, taulons de 2 cm, sense tauló a dalt, i 40 cm reservats a baix per als arxivadors. Els nivells tenen alçada fixa: 40 cm els de llibres grans i 25 cm els de petits. L'app només decideix quants nivells van a cada columna i on va cada tauló; l'espai que sobra queda com a nivell lliure a baix.

## Dades

Tot es desa al navegador del mòbil, no a cap servidor. Fes *Exporta JSON* de tant en tant i guarda el fitxer: és la còpia de seguretat, i serveix per passar el catàleg a un altre dispositiu amb *Importa*.

## Servir-la des del Mac (alternativa)

`python3 serveix.py` la serveix per HTTPS a la WiFi de casa; cal acceptar el certificat autosignat el primer cop.
