![Luokkakaavio](./kuvat/arkkitehtuuri-luokkakaavio.png)

Uuden langan lisäämistä kuvaava sekvenssikaavio:

sequenceDiagram
    actor User
    participant UI
    participant YarnService
    participant YarnRepository
    participant yarn
    User->>UI: click "Lisää varastoon"
    UI->>YarnService: add_yarn("lanka", "harmaa", ...)
    YarnService->>yarn: Yarn("lanka", "harmaa", ...)
    YarnService->>YarnRepository: add(yarn)
    YarnRepository-->>YarnService: yarn
    UI->>UI: initialize_entry_fields()
