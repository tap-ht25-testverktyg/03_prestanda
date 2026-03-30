# Prestandatester

Lektion 3 i kursen testautomatisering och testverktyg.

Repot använder följande Python packages:
```
pytest
pytest-benchmark
```

Markers: unit, performance

För att starta finns flera alternativ. Lägg till `python -m` först på raden om det inte går att köra pytest direkt.

```commandline
pytest -v -m "unit"
pytest -v -m "performance" --benchmark-columns="min,max,mean"
```

## prime.py
Tre versioner av en funktion som kontrollerar om ett tal är ett primtal. Kör prestandatestet och se vilken som är snabbast!

Resultat vid tidigare körning

| Algoritm                          | Medeltid (ms) | Procent |
|-----------------------------------|---------------|---------|
| Intuitiv                          | 1000          | 100%    |
| Förbättrad (testa inte jämna tal) | 500           | 50%     |
| Roten ur n                        | 5             | 99.5%   |
