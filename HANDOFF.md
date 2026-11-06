# Handoff: portfolio di Umberto

Aggiornato: 2026-11-06

## Stato
**Il sito è online: https://umb-c.github.io** (GitHub Pages, ramo `main`, cartella root, attivo da solo perché il repository si chiama `umb-c.github.io`).
Repository: https://github.com/umb-c/umb-c.github.io (pubblico, account `umb-c`).
Anteprima privata su claude.ai (non pubblica, sensori bloccati): https://claude.ai/artifact/QyaTgjUqVLr8dQK4KRNxh8

Fatto e verificato dall'utente: il sito si apre, il ritratto si compone. Verificato solo in simulazione: inclinazione del telefono.

Contenuto del sito:
- Ritratto di particelle ricostruito da `assets/head-art.png` (disegno fornito dall'utente), niente di fisso: respiro, scostamento al cursore, esplosione al tocco, sguardo veloce, battito, occhiolino, sopracciglia, sorriso.
- IT/EN, nome in Archivo Black, slogan arcobaleno, quattro sezioni con scheda immagine e vista di dettaglio al click, bio, contatti segnaposto.

## Cose da sapere per lavorare su questo progetto
- **Ambiente di sessione**: la sessione cloud non può creare repository, né attivare Pages, né chiamare endpoint GitHub non legati ai repository collegati. `add_repo` ha funzionato solo dopo che l'utente ha collegato l'account (`claude.ai/connect-github`), installato la Claude GitHub App sul repository e creato il repository a mano. Il controllo di sicurezza ha bloccato il tentativo di collegare `umb-c/capi` (repository non pertinente): non farlo.
- Flusso di pubblicazione: clonare `umb-c/umb-c.github.io`, modificare `index.html`, commit, `git push origin main`. Pages ripubblica da solo in 1-2 minuti. Un push vuoto riavvia la pubblicazione se compare il 404.
- Anteprima locale: `python3 -m http.server 8765` nella cartella (si ferma se la sessione si riavvia). Test visivi con Playwright preinstallato; il sito espone `window.__setExpression(i)`, `window.__setGaze(x, y)`, `window.__gaze`.
- L'account GitHub `umb-c` è provvisorio: l'utente vuole cambiare username più avanti (voleva `umberto`). Se lo fa, il repository deve chiamarsi `NUOVONOME.github.io`, l'indirizzo cambia e quello vecchio smette di funzionare.
- Foto originale (`photo.png`) e script `tools/stencil.py` esistono solo nella cartella di lavoro locale (`/home/user/portfolio`), **non** nel repository pubblico. Nel repository ci sono `index.html`, `assets/head-art.png`, `tools/build_artifact.py`, documenti.

## Da fare, in ordine
1. **Linguaccia e bocca che si apre**: richiesta più volte, mai realizzata sul ritratto attuale. Idea: particelle procedurali nello stesso stile (interno bocca nero, lingua con contorno), spostando le particelle di labbro inferiore e mento. Le coordinate della bocca sono in `CONFIG.mouth` (pixel dell'immagine 768x1024).
2. **Inclinazione del telefono**: farla verificare all'utente sul telefono reale. Se non va, `https://umb-c.github.io/?debug` mostra i valori dei sensori in basso a sinistra.
3. **Contenuti veri**: immagini e descrizioni dei progetti (Lamape Ops, Lesto, WooCommerce Pusher, siti, temi Shopify, inserzioni, opere). File in `images/`, campo `img` in `SECTIONS`.
4. **Bio**: confermare o riscrivere i dettagli inventati (primo programma, smontare le macchine).
5. **Contatti**: scegliere come farsi contattare (email, LinkedIn, GitHub, form), sostituire il segnaposto. Non pubblicare l'email senza il suo ok.
6. **Username**: cambiare username GitHub, poi rinominare il repository.
7. **Prestazioni**: circa 30 mila particelle, nel test senza GPU ~15 fps. Se scatta su telefoni, abbassare `CONFIG.maxParticles` (es. 20000).

## Errori già fatti, per non ripeterli
- Rigidità delle molle troppo alta rispetto al passo di tempo: le particelle degli occhi esplodevano e gli occhi sparivano. Ora la rigidità è limitata da `kmax = (0.85 / dt)^2`. Non rimuovere il limite.
- Pulsante dei sensori dentro il testo di aiuto nascosto su telefono: su iPhone non si poteva attivare. Ora il pulsante è fuori dal testo nascosto.
- Ascolto dei sensori condizionato all'assenza di `requestPermission`: alcuni browser la espongono comunque. Ora si ascolta sempre.
- Le pagine pubblicate come Artifact su claude.ai bloccano i sensori: l'inclinazione lì non funziona mai, si prova solo sul sito vero.

## Dove sono le cose
- `index.html`: tutto il sito (stile, contenuti `SECTIONS` e `I18N`, ritratto `CONFIG`).
- `assets/head-art.png`: ritratto sorgente delle particelle.
- `tools/build_artifact.py`: versione a file unico per l'anteprima su claude.ai.
- `CLAUDE.md`: memoria del progetto (preferenze, scelte scartate, come funziona).
