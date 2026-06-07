---
id: 002
type: post-mortem
date: 2026-06-07
status: accepted
agenti: [hermes, max]
---

# Token Telegram revocato — gateway default down

## Cos'è successo
Il token del bot `@MassighermesBot` (profilo Hermes default) è stato revocato. L'API Telegram risponde 404 Not Found a qualsiasi richiesta (`getMe`, `getUpdates`, `sendMessage`).

## Causa
Probabilmente il token è stato rigenerato da @BotFather in una sessione precedente, oppure è scaduto.

## Impatto
- Gateway Hermes profilo **default** non funzionante
- I profili **mondoalegre** e **iro** continuano a funzionare (token diversi)
- Non si può parlare con Hermes via Telegram sul profilo default

## Soluzione
1. Rigenerare il token da @BotFather → `/mybots` → seleziona il bot → API Token → Revoke
2. Scrivere il nuovo token sul VPS in `/root/.hermes/.env`
3. Riavviare il gateway default

**Problema tecnico**: Il sistema Hermes oscura il token in output (sicurezza), quindi non è possibile scriverlo via comandi remoti — va fatto manualmente via SSH o con un file preparato localmente.

## Lezioni apprese
- Tenere una copia sicura dei token Telegram fuori da Hermes (es. vault Obsidian crittato)
- Nota: il vault non può contenere token in chiaro perché verrebbero oscurati anche lì
- Meglio salvare i token in un password manager esterno (es. 1Password, Bitwarden)
