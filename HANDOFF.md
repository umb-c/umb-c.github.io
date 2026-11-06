# Handoff: portfolio di Umberto

Data: 2026-11-06

## Stato
Il sito funziona e il ritratto è quello fornito dall'utente (`assets/head-art.png`) ricostruito con particelle, approvato come direzione ("prova ad usare questa").
Visto in anteprima su desktop e telefono: respiro delle particelle, sguardo che segue il cursore, battito, occhiolino, sopracciglia, sorriso.

Fatto:
- Ritratto di particelle da immagine, layout split su desktop e impilato su telefono.
- Sito bilingue IT/EN, nome in Archivo Black, slogan arcobaleno.
- Quattro sezioni con scheda immagine segnaposto e vista di dettaglio al click, bio, contatti segnaposto.
- Anteprima come Artifact privato: https://claude.ai/artifact/QyaTgjUqVLr8dQK4KRNxh8 (si rigenera con `tools/build_artifact.py`).
- Commit locale pronto. **Non ancora su GitHub**: la sessione non può creare repository; serve un repository privato vuoto creato dall'utente, poi `add_repo` e push.

## Da fare, in ordine
1. **Repository**: l'utente crea un repository privato vuoto su GitHub e lo comunica; attaccarlo con `add_repo` (access push) e fare push del branch `main`.
2. **Linguaccia e bocca che si apre**: richiesta fatta più volte, non ancora realizzata sul nuovo ritratto. Idea: particelle procedurali nello stesso stile (interno bocca nero, lingua con contorno), spostando le particelle di labbro inferiore e mento.
3. **Contenuti veri**: immagini e descrizioni dei progetti (Lamape Ops, Lesto, WooCommerce Pusher, siti, temi Shopify, inserzioni, opere). File in `images/`, campo `img` in `SECTIONS`.
4. **Bio**: confermare o riscrivere i dettagli inventati.
5. **Contatti**: scegliere come farsi contattare e sostituire il segnaposto.
6. **Pubblicazione sul web**: GitHub Pages. Con repository privato serve un piano a pagamento; altrimenti repository pubblico (tenendo conto che contiene `photo.png`).

## Cose non verificate
- Inclinazione del telefono (giroscopio): non testabile nell'anteprima, che blocca i sensori. Su iPhone serve il pulsante "enable motion".
- Prestazioni su telefono reale: circa 30 mila particelle; in un browser senza GPU il test è sceso a ~15 fps. Se scatta, abbassare `maxParticles` (es. 20000).
- Font: Archivo Black arriva da Google Fonts, serve rete. Il fallback è Impact.

## Dove sono le cose
- `index.html`: tutto il sito (stile, contenuti, ritratto).
- `assets/head-art.png`: ritratto sorgente delle particelle (fornito dall'utente).
- `photo.png`: foto originale, usata solo da `tools/stencil.py`. Contiene il volto di Umberto: tenere il repository privato o toglierla prima di renderlo pubblico.
- `assets/head-*.png`: cutout e stencil generati da `tools/stencil.py` (esperimenti, non usati dal sito).
- `tools/build_artifact.py`: versione a file unico per l'anteprima.
- `tools/stencil.py`: scontorno della testa e stencil dalla foto.
- `CLAUDE.md`: memoria del progetto (preferenze, scelte scartate, come funziona).
