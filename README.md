# Prestandatester

Lektion 3 i kursen testautomatisering och testverktyg.

Repot använder följande Python packages:
```
pytest
pytest-benchmark
```

Markers: TODO skriv vilka markers som används i pytest.ini

För att starta finns flera alternativ. Lägg till `python -m` först på raden om det inte går att köra pytest direkt.

```commandline
pytest -v -m "unit and not slow"
pytest -v -m "performance"
```