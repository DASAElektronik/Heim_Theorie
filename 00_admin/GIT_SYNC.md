# Git-Synchronisierung in dieser Windows-Sitzung

Stand2026-10-18. Branch normalization-review, origin unverändert.

Vier ausstehende Commits f241ee1,2802434,ce0d311,738a4f6 wurden erfolgreich
als Fast-forward von b2c1113 auf738a4f6 gepusht. Remote-Hash anschließend
über ls-remote bestätigt; lokaler Tracking-Branch stimmt überein.

## Funktionierender Zugriff

Windows-Schannel scheiterte mit SEC_E_NO_CREDENTIALS. Git mit OpenSSL erreicht
GitHub mit aktivierter Zertifikatsprüfung. Die vorhandene GitHub-CLI-Anmeldung
funktioniert (API-Profil geprüft); der separate App-Connector meldete dagegen
einen widerrufenen OAuth-Token. Keine neue Anmeldung oder Tokensuche notwendig.

Der erfolgreiche Push verwendete eine explizite Argumentliste mit OpenSSL,
leerem credential.helper als Reset und `!gh auth git-credential` als Helper.
Die direkten Shellversuche hatten zuvor keine verwertbare Fehlermeldung geliefert.
Der genaue Grund dieses Shell-Unterschieds ist nicht abschließend bestimmt.

Reproduzierbar ohne dauerhafte Konfigurationsänderung:

```powershell
py -3.13 scripts/git_remote.py check
py -3.13 scripts/git_remote.py push
```

Der Helper liest keine Token selbst aus, zeigt keine Secrets an und enthält
kein Force-Push. Änderungen vorher gezielt prüfen, stagen und committen.
Ein erfolgreicher Push ist von einem erfolgreichen Pull getrennt zu berichten.

## Verbleibende lokale Grenze

`git pull --ff-only` wurde beim Schreiben von .git/FETCH_HEAD mit Permission
denied abgewiesen. ACL-Lesung zeigt explizite Sandbox-Deny-Einträge; auch das
Sitzungsprofil schützt .git. Diese Berechtigungen wurden nicht geändert oder
umgangen. Das ist keine durch SSL oder Anmeldung behobene Schreibsperre.
Beim geprüften Remote-Stand lag keine fremde Änderung zum Integrieren vor.
Falls der Remote später vorläuft oder divergiert, vor dem nächsten Push
regulär integrieren, sobald der erforderliche Git-Schreibzugriff verfügbar ist.
