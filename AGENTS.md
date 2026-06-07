# Agentric Decision Log

Benvenuto. Questo repository è il **sistema di memoria condivisa** tra tutti gli agenti AI (Hermes, Claude, ChatGPT, Codex, ecc.) e gli umani (Max, Iro, ecc.).

## Regola principale

**Ogni decisione, idea o conversazione importante va salvata qui.**

## Struttura

```
decisioni/
  YYYY/
    MM/
      YYYY-MM-DD_NNN-titolo-breve.md
```

Ogni file usa questo frontmatter:

```yaml
---
id: NNN                    # Numero progressivo
type: decision | idea | post-mortem | procedure
date: YYYY-MM-DD
status: proposed | accepted | deprecated | implemented
agenti: [hermes, max, claude, chatgpt, codex]  # Chi ha partecipato
---
```

## Come contribuire

### 1. Clona il repo
```bash
git clone git@github.com:massimilianogrotta-ui/agentric-decision-log.git
```

### 2. Crea un file
Crea un nuovo file nella cartella giusta con il prossimo ID progressivo.

### 3. Commit e push
```bash
git add -A
git commit -m "decision: titolo breve"
git push
```

## Se sei un agente AI (Claude, ChatGPT, Codex, ecc.)

1. **Leggi** il repo prima di rispondere per capire il contesto
2. **Scrivi** una decisione quando l'umano approva qualcosa
3. **Usa** il repository come memoria persistente tra sessioni

## Workflow tipico

1. L'umano dice "vorrei...", "ho deciso che...", "mi piacerebbe..."
2. L'agente propone: "Salvo questa decisione/idea? 📝"
3. Se confermato, crea file + commit + push
4. Tutti gli altri agenti vedranno la modifica al prossimo clone/pull

## Template minimo per decisioni/idee

```markdown
---
id: PROSSIMO_ID
type: decision | idea
date: OGGI
status: accepted | proposed
agenti: [chi, ha, partecipato]
---

# Titolo

## Decisione / Idea
Cosa è stato deciso o proposto.

## Contesto
Perché.

## Conseguenze / Prossimi passi
Cosa succede ora.
```

## Note

- Non cancellare mai file — usa `status: deprecated` se una decisione è superata
- Un file = una decisione/idea
- La cronologia git è la fonte di verità
