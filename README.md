# 5m_v5

Guarda il file [testo_verifica.md](5m_v5/testo_verifica.md) per le istruzioni dettagliate sugli esercizi da svolgere in questa versione dell'applicazione Flask.
Guarda le immagini nella cartella [5m_v5](5m_v5) per esempi visivi di come dovrebbe apparire l'applicazione dopo aver completato gli esercizi.
Consegna creando un fork di questo repository.

## Configurazione Ambiente di Sviluppo

1. Clona il repository:
   ```bash
   git clone <URL_DEL_REPOSITORY>
   cd <NOME_CARTELLA_REPOSITORY>
   ```

2. Crea un ambiente virtuale:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`
   ```

   Su Windows se Powershell non permette di eseguire script, esegui:
   ```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. Installa le dipendenze:
   ```bash  
    pip install flask
    ```

4. Inizializza il database:
    ```bash
    python setup_db.py
    ```

5. Avvia l'applicazione:    
   ```bash
   flask run
   ```

6. Apri il browser e vai a `http://localhost:5000` per vedere l'applicazione in esecuzione.

## Per fare il commit e push delle modifiche

```bash
 git config --global user.name "Tuo Nome"
 git config --global user.email "esempio@email.com"
```

Poi usa l'interfaccia di VSCode per fare commit e push delle modifiche al tuo fork del repository.