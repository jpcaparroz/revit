# Revit

<h6>The loopdevs document ai</h6>

---


#####
    https://huggingface.co/facebook/bart-large-cnn



## Fluxo
Fluxo da arquitetura do Revit:


``` mermaid
architecture-beta
    group front(cloud)[Front End]
    group back(cloud)[Back End]

    service react(server)[React with Nextjs] in front

    service fastapi(server)[FastAPI] in back
    service transformer(server)[Transformer] in back
    service model(database)[Model mT5_multilingual_XLSum] in back
    service python(server)[Python] in back

    service user(internet)[Usuario]


    user:R <--> L:react

    react:R <--> L:fastapi
    fastapi:R <--> L:python
    python:R <--> L:transformer
    transformer:R <--> L:model



```


<!-- admin:R <--> T:gateway{group} -->