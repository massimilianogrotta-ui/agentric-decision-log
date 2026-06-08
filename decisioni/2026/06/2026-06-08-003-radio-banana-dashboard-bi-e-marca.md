---
id: 003
type: decision
date: 2026-06-08
status: accepted
agenti: [claude, max]
---

# Radio Banana — dashboard, BI e marca

## Decisione
Definita l'app **Radio Banana** (rete di intelligence sui prezzi del banano EC, *Powered by All-io*)
con due prodotti — **Export** (compra finca + FOB) e **Import** (CIF + FOT T1/T2) — e una **capa BI**
(piano Medio+). Decisioni chiave prese oggi:

- **Due grafici, due ruoli**: Tab "Compra finca" = vista pulita (anni + **linea BI** rossa punteggiata,
  banda ±8%). **Tolta la "media storica"** dal grafico principale perché somigliava alla linea BI e
  confondeva (la BI è l'unica che guarda al futuro).
- **Tab "Inteligencia" = grafico-laboratorio interattivo** con bottoni toggle: Proiezione BI, Banda,
  Marcatori, Produzione (embolse→cosecha), Media storica, PMS, Eventi + assi Settimana/Data e Recente/Anno.
- **Zoom per settimana (stile trading, recharts Brush)** su entrambi i grafici. Il business si misura
  a SETTIMANA.
- **Login bilingue ES/EN** + simulatore di piani (free / base / medio / enterprise + gate contributor).
- **Marca**: navy `#15294E`, arancio `#F2901C`, giallo `#F5C23B`; font Fira Sans/Code. Pack creato
  (SVG vettoriali via VTracer, favicon, social, login). NB: il logo lo sta ridisegnando un'altra app.

## Contesto
La BI nasce dalla skill `radio-banana-bi` (3 capas: modello quantitativo stagionale+clima, dati clima
freschi, deep research obbligatorio). **Backtest validati** (pico feb, valle marzo, repunte maggio):
il modello dà la tendenza, il **contesto** cattura picchi/crolli. Regola d'oro: mai inventare dati,
sempre "no es asesoría de inversión". PMS 2026 = $7.50/caja.

## Conseguenze / Prossimi passi
- Demo viva: `~/Claude/Projects/radio-banana-demo/` → `bundle.html` (copia `~/Downloads/radio-banana-proposta.html`).
- Brand pack: `~/Claude/Projects/Agente Mondo Alegre/brand-radio-banana/` (+ zip in Downloads).
- TODO: landing page bilingue; collegare la linea BI del demo all'output reale della skill (oggi dati
  statici); portare i grafici in produzione (`ecuador-precios/page.tsx`); opz. zoom tipo TradingView e
  vista "cadena de valor" finca→FOB→CIF.
