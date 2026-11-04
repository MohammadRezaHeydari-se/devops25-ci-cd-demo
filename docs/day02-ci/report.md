# Dag 2 – Continuous Integration

## Syfte

Jag ville förstå hur GitHub Actions startar en CI-pipeline, vilka kontroller som körs och hur jag kan använda loggarna för att hitta fel.

## Demo 2A – CI-konfiguration

Jag läste `.github/workflows/ci.yml` utan att ändra filen.

Workflowen startar vid push till main eller en pull request mot main.

Pipelinen har två jobb:

- `test`: installerar Python 3.12 och beroenden, kör Ruff och Pytest.
- `build-image`: bygger en Docker-image om testjobbet lyckas.

`needs: test` gör att Docker-bygget inte fortsätter om testerna misslyckas.

## Demo 2B – Automatisk körning

Jag skapade branchen `demo/dag2-ci-MReza`, lade till en kort text i README och pushade ändringen.

Sedan skapade jag en pull request mot lärarens repository.

Körningen där väntar på godkännande från en maintainer. För att kunna genomföra och analysera CI använde jag därför även min tidigare praktiska övning i mitt eget forkade repository.

## Demo 2C – Loggar och felsökning

I den praktiska övningen testade jag tre situationer: fungerande kod, ett avsiktligt fel och en rättning.

Först lyckades Ruff, Pytest och Docker-bygget.

Sedan ändrade jag `return a + b` till `return a - b` i `app/service.py`.

Ruff hittade inget fel, men Pytest rapporterade två misslyckade tester:

- `tests/test_service.py::test_add`
- `tests/test_api.py::test_add_endpoint`

Felmeddelandet var `assert -1 == 5`.

Jag kunde följa felet från testloggarna tillbaka till beräkningen i `app/service.py`. Eftersom testjobbet misslyckades hoppades `build-image` över.

Efter rättningen gick alla fem tester igenom igen och båda jobben lyckades.

## Demo 2D – Runners

Workflow-filen använder `runs-on: ubuntu-latest`. Det betyder att jobben körs på en GitHub-hosted runner med Linux.

I loggarna såg jag att Python 3.12 användes.

En GitHub-hosted runner tillhandahålls och hanteras av GitHub. En self-hosted runner sköts i stället av organisationen själv och kan behövas för särskild hårdvara eller åtkomst till interna system.

En runner kör jobbet. Docker-imagen är något som jobbet bygger, inte själva runnern.

## Reflektion

Jag lärde mig att Ruff och Pytest kontrollerar olika saker. En grön lint-kontroll betyder inte att programmets logik är korrekt.

CI kan upptäcka problem tidigt och ge snabb feedback, men den kan inte garantera att all funktionalitet fungerar. Fel som inte täcks av testerna kan fortfarande passera.

Det viktigaste för mig var att lära mig läsa loggarna och förstå varför pipelinen stoppade.

## Resultat och bevis

- [Praktisk CI-rapport med fyra skärmbilder](https://github.com/MohammadRezaHeydari-se/devops25-ci-cd-demo/blob/exercise/day02-practical-MReza/docs/day02-practical/report.md)
- [Första lyckade körningen](https://github.com/MohammadRezaHeydari-se/devops25-ci-cd-demo/actions)
- [Avsiktligt misslyckad körning](https://github.com/MohammadRezaHeydari-se/devops25-ci-cd-demo/actions/runs/41622795290)
- [Lyckad körning efter rättning](https://github.com/MohammadRezaHeydari-se/devops25-ci-cd-demo/actions/runs/41704482858)
- [Pull request för den praktiska övningen](https://github.com/MohammadRezaHeydari-se/devops25-ci-cd-demo/pull/1)
- [Pull request till läraren](https://github.com/cloudfactoreu/devops25-ci-cd-demo/pull/26)

## Slutsats

Övningen visade mig hur en liten kodändring kan kontrolleras automatiskt, hur fel kan stoppas före ett bygge och varför det är viktigt att förstå resultaten bakom en grön eller röd pipeline.
