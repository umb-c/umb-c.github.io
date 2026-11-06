# Memory: portfolio di Umberto

Sito personale statico (HTML/CSS/JS in un unico `index.html`, nessuna dipendenza da installare). **Online su https://umb-c.github.io** (repository `umb-c/umb-c.github.io`, GitHub Pages dal ramo `main`).
Hero con un ritratto di Umberto fatto di particelle nere su sfondo bianco, in stile stencil. Sotto: schede di sezione, bio, contatti.

## Chi è l'utente e come vuole lavorare
- Si chiama Umberto, nato a Napoli nel 1981. Scrive in italiano, vuole il sito in **italiano e inglese** (pulsante IT/EN).
- Tagline: "I imagine and create." / "Immagino e creo." con effetto arcobaleno animato.
- Il font del nome deve essere molto spesso (Archivo Black).
- Il volto deve essere **simpatico**: sorriso di base, occhiolino, linguaccia. Mai severo o "tossico".
- Si cambia idea in fretta e il giudizio è diretto ("orrendo", "sembro grasso"). Meglio mostrare una versione e correggere che fare domande lunghe.
- Non pubblicare la sua email né altri contatti finché non decide come farsi contattare.
- Vuole poter provare il sito su altri telefoni, quindi serve un indirizzo pubblico, non link privati di claude.ai.
- Ha un account GitHub provvisorio (`umb-c`) e vuole cambiarlo più avanti (idea: `umberto`): vedi HANDOFF.md.
- Gli occhi devono seguire anche l'inclinazione del telefono e vuole i sensori attivi di default (su iPhone non è possibile senza tocco e permesso di Safari: si chiede al primo tocco).

## Il ritratto: storia e stato attuale
Scartati dall'utente (non ripetere): punti sparsi con ombre dure, contorno automatico dalla foto (doppio sui capelli, mascella larga),
occhi/bocca disegnati proceduralmente, barba come massa grigia ("sembro grasso"), collo e maglione visibili ("solo testa!"), stencil troppo scarno.

**Soluzione adottata (2026-11-06):** l'utente ha fornito un suo ritratto in bianco e nero stile stencil/incisione (`assets/head-art.png`, 768x1024, solo testa).
Il sito lo ricostruisce con particelle nere: ogni particella nasce da un pixel scuro. Richieste dell'utente su questo ritratto:
- niente di fisso: solo particelle che si muovono (respiro, scostamento al cursore) e gli occhi che seguono il puntatore;
- espressioni dal movimento delle particelle: battito, occhiolino, sopracciglia, sorriso;
- la **linguaccia** era stata chiesta (e anche la bocca che si apre) ma con questo ritratto non è ancora fatta. Da proporre/fare: bocca aperta + lingua come particelle nello stesso stile.

Come funziona (`index.html`, blocco `CONFIG` e funzione `build`): le coordinate di iridi, palpebre, sopracciglia e bocca sono in pixel dell'immagine 768x1024.
Se si cambia ritratto vanno rimisurate. `maxParticles` regola dettaglio/prestazioni (30000 ora; su telefono si può scendere).
Su schermo largo il volto sta a destra e il nome a sinistra; su telefono il volto sta sopra al nome.

Movimento: respiro continuo, cursore che sposta le particelle con un vortice (raggio 130), esplosione al tocco (`burst`), sguardo veloce, iridi più rigide delle altre particelle. La rigidità delle molle è limitata da `kmax = (0.85/dt)^2` per evitare l'instabilità: non toglierlo, senza gli occhi spariscono.
Inclinazione: si ascolta sempre `deviceorientation`; su iPhone il permesso si chiede al primo tocco e dal pulsante "Attiva i sensori". `?debug` nell'indirizzo mostra i valori dei sensori. Nelle pagine Artifact di claude.ai i sensori sono bloccati.

Prima di arrivare qui è stato fatto anche `tools/stencil.py`: scontorna la testa da `photo.png` e ne ricava uno stencil. Resta come strumento, non è usato dal sito.

## Contenuti e lingua
- Testi nel dizionario `I18N` (en/it), sezioni e progetti nell'array `SECTIONS`, in cima allo script.
- Ogni sezione ha una scheda con immagine; il click apre una vista con tutti i lavori (hash `#art-design`, `#web`, `#apps-tools`, `#marketing`).
- Per aggiungere un'immagine: `img: 'images/nome.jpg'` sull'elemento (o `cover` sulla sezione). Per un link: `link: 'https://...'`.
- Progetti reali citati dall'utente: Lamape Ops, Lesto, WooCommerce Pusher (descrizioni ancora segnaposto).
- Bio: Napoli 1981, appassionato di computer da piccolo, ora sperimenta AI locale per migliorare i processi produttivi. Il dettaglio dell'avventura testuale e dello smontare le macchine è inventato su richiesta dell'utente: da confermare o sostituire.

## Strumenti
- Anteprima locale: `python3 -m http.server 8765` nella cartella, poi `http://localhost:8765/`. Serve un server (l'immagine viene letta dal canvas).
- Pubblicazione: commit e `git push origin main` su `umb-c/umb-c.github.io`; Pages ripubblica in 1-2 minuti. La sessione cloud non può creare repository né attivare Pages.
- `tools/build_artifact.py` genera una versione a file unico con l'immagine del ritratto incorporata per l'anteprima come Artifact su claude.ai (https://claude.ai/artifact/QyaTgjUqVLr8dQK4KRNxh8).
- Test visivi: Playwright preinstallato (il server locale va riavviato se la sessione si riavvia); il sito espone `window.__setExpression(i)` e `window.__setGaze(x, y)` per i fotogrammi.
