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
pytest -v -m "performance"
```

## prime.py
Tre versioner av en funktion som kontrollerar om ett tal är ett primtal. Kör prestandatestet och se vilken som är snabbast!
