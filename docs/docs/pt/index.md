# Revit

<h6>The loopdevs document ai</h6>

---


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



##

1. ## <a name="_toc393284199"></a><a name="_toc182333996"></a>**INTRODUÇÃO**
   1. <a name="_toc182333997"></a><a name="_toc1563775225"></a>**INTRODUÇÃO EM LINGUA NATIVA**

   Com o crescente volume de informações disponíveis em formato digital, surge a necessidade de ferramentas que facilitem o acesso rápido e eficiente ao conteúdo essencial. Pensando nisso, o projeto Revit foi desenvolvido como uma solução inovadora voltada para resumir arquivos PDF de maneira automatizada. Utilizando técnicas avançadas de inteligência artificial e processamento de linguagem natural, o Revit transforma documentos extensos em resumos curtos e claros, facilitando a compreensão e economizando tempo para os usuários. Este trabalho explora o desenvolvimento do Revit, destacando sua arquitetura e funcionalidades.

   **PALAVRAS-CHAVE:** Revit – resumir PDF – economizar tempo – solução inovadora – inteligência artificial


   2. <a name="_toc182333998"></a><a name="_toc1594747007"></a>**INTRODUÇÃO EM LINGUA ESTRANGEIRA**

   With the increasing volume of information available in digital format, there is a growing need for tools that allow quick and efficient access to essential content. With this in mind, the Revit project was developed as an innovative solution for automated PDF summarization. Utilizing advanced artificial intelligence and natural language processing techniques, Revit transforms lengthy documents into concise and clear summaries, enhancing comprehension and saving user's time. This paper explores the development of Revit, highlighting its architecture and functionalities

   **KEYWORDS:** Revit – PDF summarization – saving time – innovative solution – artificial intelligence



1. ## <a name="_toc487280376"></a><a name="_toc182333999"></a>**DESENVOLVIMENTO**

O Revit foi um desafio muito legal de se concluir. Aprendizado e trabalho em equipe resume todo esforço gasto no projeto. Abaixo, citamos detalhadamente toda as etapas desse projeto.
##
1. <a name="_toc182334000"></a><a name="_toc1803384557"></a>**TECNOLOGIAS USADAS**

   -------------------------------------------------------------------------------
Este projeto utiliza uma combinação de tecnologias para entregar uma solução robusta e escalável. A arquitetura é dividida em três componentes principais: back-end, front-end e documentação, cada um com ferramentas específicas que otimizam o desenvolvimento, a execução e a apresentação do projeto. Abaixo, detalhamos as escolhas tecnológicas de cada parte e o motivo de sua seleção.

1. **Back-End**



O back-end é desenvolvido em **Python** e utiliza várias bibliotecas especializadas para oferecer uma API eficiente e de alta performance para processar documentos em PDF e gerar resumos. Fora as bibliotecas padrões já fornecidas na instalação do python, foram utilizadas:



1. **FastAPI:** FastAPI é o framework principal usado para criar a API do projeto. Ele é conhecido pela sua alta performance e suporte nativo para operações assíncronas, o que permite que o sistema lide com múltiplas requisições simultâneas de forma eficiente. A FastAPI também facilita a criação de endpoints bem documentados, tornando a integração com o front end mais simples e segura.



1. **Transformers:** A biblioteca transformers, desenvolvida pela **Hugging Face**, é utilizada para trabalhar com modelos de aprendizado profundo, como o **mT5**. Essa biblioteca permite fácil integração com modelos **pré-treinados** para tarefas de **NLP** (Processamento de Linguagem Natural), incluindo sumarização. A utilização de transformers possibilita o processamento e a geração de resumos de forma eficiente e com alto nível de precisão.



1. **Datasets:** Também da **Hugging Face**, a biblioteca datasets oferece acesso a uma vasta gama de conjuntos de dados, incluindo o **XLSum**, que é essencial para treinar e avaliar o modelo de sumarização. Essa biblioteca permite carregar e manipular conjuntos de dados de maneira eficiente, o que é crucial para o desempenho do sistema de resumo.



1. **TensorFlow:** TensorFlow é uma das bibliotecas de aprendizado de máquina mais populares, especialmente para treinamento e implementação de modelos de deep <a name="_int_l1nfmp4z"></a>learning. No projeto, TensorFlow é utilizado para ajustar e otimizar o modelo **transformer**, garantindo que o modelo possa realizar inferências rápidas e gerar resumos de qualidade.



1. **PyPDF2:** A biblioteca PyPDF2 é utilizada para manipular arquivos PDF. Ela permite extrair o texto dos documentos, o que é o primeiro passo no fluxo de processamento antes da geração do resumo. A escolha do PyPDF2 se deve à sua **simplicidade** e **eficácia** na manipulação de PDFs, oferecendo funções para leitura e manipulação de páginas e texto com facilidade.



1. **Front-End**



O front-end é desenvolvido com **React** e utiliza **TypeScript** e **Next.js** para criar uma interface de usuário dinâmica, responsiva e escalável.



1. **React:** React é uma das bibliotecas mais populares para o desenvolvimento de interfaces de usuário. Ele permite a criação de componentes reutilizáveis e facilita o gerenciamento do estado da aplicação. No projeto, React permite criar uma interface intuitiva, onde os usuários podem fazer o upload de arquivos PDF e visualizar os resumos gerados.



1. **TypeScript:** A escolha por TypeScript em conjunto com React traz benefícios significativos em termos de **segurança** e **manutenção** do código. TypeScript adiciona <a name="_int_cnnth8eh"></a>**tipagem estática** a JavaScript, o que ajuda a evitar erros comuns durante o desenvolvimento e facilita a escalabilidade da aplicação.



1. **Next.js:** Next.js é um <a name="_int_u8p7nj3m"></a>**framework** React que facilita o desenvolvimento de aplicações web com renderização no lado do servidor (Server Side Rendering, SSR) e geração de páginas estáticas. Ele oferece uma excelente otimização de performance e SEO, além de suportar a criação de rotas dinâmicas, o que é útil para organizar as diferentes páginas da aplicação. No projeto, Next.js permite uma experiência de usuário rápida e otimizada.



1. **Documentação**



A documentação é uma parte fundamental do projeto, facilitando o entendimento do sistema para novos desenvolvedores e usuários. Para isso, foram utilizadas duas ferramentas principais:



1. **Word:** O Microsoft Word é utilizado para a elaboração de documentação formal e detalhada. Também foi o software principal para a entrega do projeto seguindo as normas ABNT. 



1. **MkDocs**: MkDocs é uma ferramenta de código aberto para geração de documentação em **sites estáticos**. Ele permite criar documentação amigável e acessível, com um layout moderno e navegação fácil. Foi escolhido para ficar como documentação disponível no próprio repositório do código fonte do Revit.


1. ## <a name="_toc916808632"></a><a name="_toc182334001"></a>**MODELO**
##
A escolha de um modelo adequado para a tarefa de resumo automático de textos foi um passo crucial na construção de um sistema eficiente e preciso. No contexto da arquitetura apresentada, o modelo <a name="_int_g5uluo5a"></a>**csebuetnlp/mT5\_multilingual\_XLSum** foi selecionado devido à sua capacidade de lidar com múltiplos idiomas e sua especialização em sumarização de textos longos. Este modelo combina a robustez do **transformer mT5** com o extenso dataset **XLSum**, características que justificam seu uso em uma aplicação que visa fornecer resumos concisos e contextualizados de documentos PDF. 

O **mT5** é uma variante multilíngue do modelo **T5** (Text-To-Text Transfer Transformer), que transforma qualquer tarefa de processamento de linguagem em um problema de texto para texto. Essa abordagem permite que o modelo **mT5** execute diversas tarefas de **NLP**, como tradução, resposta a perguntas e, especialmente, **sumarização**, sem a necessidade de ajustes específicos para cada idioma.



A estrutura do **mT5** é baseada na arquitetura Transformer, que utiliza mecanismos de atenção para capturar relações complexas entre palavras em uma frase e ao longo de frases em um texto. Esse modelo é capaz de processar textos longos e extrair informações contextuais ricas, o que é essencial para produzir resumos que preservem o significado do documento original. Para uma aplicação que lida com documentos em português e outros idiomas, o **mT5** é ideal, pois foi treinado para ser eficaz em uma grande variedade de línguas, garantindo flexibilidade e precisão na tarefa de sumarização.

O **XLSum** é um **dataset** extenso e diversificado, desenvolvido para atender às necessidades de sumarização em múltiplos idiomas. Este dataset inclui dados de notícias e artigos informativos em mais de quarenta idiomas, incluindo o português, o que permite ao modelo aprender padrões linguísticos e contextuais específicos de cada idioma. A inclusão do **XLSum** no treinamento do **mT5** permitiu que o modelo se adaptasse melhor a **variações linguísticas** e culturais, essenciais para produzir resumos que capturem o tom e a intenção originais do texto.



No contexto deste sistema, o uso do **XLSum** aprimora a capacidade do modelo de gerar resumos de alta qualidade para documentos PDF em português. Esse <a name="_int_kczspoqu"></a>aspecto é particularmente relevante, pois garante que o modelo não apenas traduza as ideias principais, mas também respeite nuances linguísticas e contextuais, tornando os resumos mais relevantes e compreensíveis para os usuários finais.

A combinação do modelo **mT5** com o dataset **XLSum** resultou no modelo **csebuetnlp/mT5\_multilingual\_XLSum**, uma versão especializada para tarefas de sumarização em múltiplos idiomas. Esse modelo oferece vários benefícios específicos para o sistema de resumos:



- **Multilinguismo:** Ao utilizar o **mT5** e o **XLSum,** o modelo é capaz de gerar resumos em mais de quarenta idiomas, o que o torna adequado para usuários de diferentes regiões e origens linguísticas.
- **Precisão Contextual:** O modelo não apenas sintetiza o conteúdo, mas também mantém a precisão contextual, reproduzindo fielmente as principais ideias do documento original.
- **Adaptabilidade a Textos Longos:** Projetado para documentos extensos e informativos, o **csebuetnlp/mT5\_multilingual\_XLSum** consegue lidar com textos complexos, mantendo a coerência no resumo final.



1. ` `**<a name="_toc182334002"></a>TREINAMENTO DO MODELO**

   --------------------------------------------------------
O modelo foi treinado com o datase **xlsum** por **csebuetnlp.** Dataset completo e um ponto muito importate: Sua quantidade extensa de linguages (ao todo 45). A maior origem de seus dados é a própria BBC (site de noticias).

Os campos contidos em seus dados são:

- Id = Código da reportagem/noticia
- url = Caminho da web para reportagem/noticia
- title = Título da reportagem/noticia
- summary = Resumo da reportagem/noticia
- text = Reportagem/noticia

1. ## <a name="_toc1832265406"></a><a name="_toc182334003"></a>**FLUXO DA INFORMACÃO**
   ##
A [arquitetura](#bookmark1) apresentada abaixo busca fornecer um serviço de resumo de textos a partir de arquivos PDF, utilizando um modelo de aprendizado capaz de processar documentos em diversas línguas. O fluxo divide-se em duas principais camadas: o **Front-End** e o **Back-End**, cada uma com responsabilidades específicas que, em conjunto, permitem ao usuário interagir e obter resumos precisos e relevantes. A seguir, detalhamos cada componente.


No **front-end**, temos uma interface de usuário desenvolvida com **React** em conjunto com o **Next.js**, uma estrutura que facilita a renderização de páginas no lado do servidor (SSR - Server Side Rendering), além de possibilitar a construção de aplicações web altamente responsivas e escaláveis. Este ambiente permite que o usuário faça upload de arquivos PDF e envie as requisições para o back-end, buscando uma experiência intuitiva e rápida.

O **back-end,** por sua vez, é composto por uma série de camadas especializadas, cada uma desempenhando uma função crítica para o funcionamento do sistema de resumo. Esse módulo é desenvolvido em **Python** e utiliza **FastAPI** como **framework** principal para a construção de **APIs RESTful**, o que facilita a comunicação entre o front-end e as camadas de processamento e modelagem. A **FastAPI** é uma escolha ideal para este tipo de aplicação devido à sua alta performance e suporte a operações assíncronas, o que permite o manuseio eficiente de múltiplas requisições simultâneas.

No núcleo do processamento de linguagem natural, a arquitetura utiliza a tecnologia **Transformer**[^1], que é o padrão atual para modelos de aprendizado profundo em tarefas de **NLP** [^2](Natural Language Processing). 

O modelo específico utilizado para o resumo é o **mT5** (Multilingual Text-To-Text Transfer Transformer), uma variante multilíngue do **T5** (Text-To-Text Transfer Transformer), que é treinado em uma vasta gama de idiomas e capaz de realizar várias tarefas de **NLP**, incluindo sumarização. O **dataset XLSum**, adaptado para o **português** e **outros idiomas**, é utilizado para o treinamento do modelo, garantindo que os resumos produzidos sejam adequados a contextos e nuances linguísticas variadas. A escolha deste modelo e dataset é estratégica para maximizar a precisão e relevância dos resumos gerados, independentemente do idioma do documento.

<a name="bookmark1"></a><a name="_toc182333981"></a>*Figura 2 - Fluxo*
##

1. <a name="_toc182334004"></a><a name="_toc1712057182"></a>**BACKEND**

   --------------------------------------------------------------------
Como a biblioteca escolhida foi a **FastAPI**, o desenvolvimento da **API** [^3]e **Endpoints**[^4]** foi acelerado e muito conciso.

No geral, apenas uma rota foi necessária para a criação do Revit. Basicamente a rota serviu para exercer as seguintes funções:

1. **Receber** um arquivo .pdf
1. **Ler** o arquivo
1. **Resumir** o arquivo
1. **Retornar** o resumo e seus detalhes

<a name="_toc182333982"></a>*Figura 3 - FastAPI*

1. <a name="_toc182334005"></a><a name="_toc183835806"></a>**FRONTEND**

   --------------------------------------------------------------------
O <a name="_int_hnjeivvz"></a>**front-end** se tornou uma tarefa menos árdua devido a todo detalhamento/desenho previamente feito utilizando a ferramenta **figma**[^5]**.**

Ao todo foram desenhadas 6 telas (contando com seus respectivos temas: claro, escuro).


O usuário tem as possíveis **5** ações dentro do **Revit**:

- **Avançar** para a página de upload do arquivo
- **Realizar** upload do arquivo
- **Alterar** o tema
- **Navegar** pela resposta do resumo (caso ela ocupe um espaço maior do predefinido)
- **Voltar** para a home


1. ## <a name="_toc1166364700"></a><a name="_toc182334007"></a>**CONTRIBUIÇÃO / CÓDIGO FONTE**

O Revit é uma aplicação de código aberto. Você pode contribuir e ver o código fonte do mesmo.

Através do [repositório](https://github.com/jpcaparroz/revit) você pode cessar o código fonte e também realizar uma contribuição através de um **pull <a name="_int_i0munzpy"></a>request**, ou até mesmo utilizar como base para um projeto pessoal através de um <a name="_int_vlgxv5zw"></a>**fork**!



1. ## <a name="_toc1684588113"></a><a name="_toc182334008"></a>**CONCLUSÃO**

Este trabalho apresentou o desenvolvimento de um sistema completo para geração de resumos automáticos de arquivos PDF, combinando tecnologias de ponta para atender a uma demanda crescente por soluções de processamento de linguagem natural (NLP). Através de uma arquitetura bem planejada, dividida em camadas de front-end, back-end e documentação, o sistema consegue oferecer resumos precisos e contextuais de documentos em múltiplos idiomas, proporcionando uma experiência prática e eficiente aos usuários.

No back-end, o uso de Python junto com bibliotecas como FastAPI, transformers, datasets, TensorFlow e PyPDF2 foi essencial para criar uma API robusta, capaz de processar PDFs e gerar resumos com alta precisão. A escolha do modelo csebuetnlp/mT5\_multilingual\_XLSum, treinado para entender diferentes idiomas, possibilitou que o sistema atendesse a uma ampla gama de usuários, independentemente da língua dos documentos.

O front-end, desenvolvido com React, TypeScript e Next.js, permitiu a criação de uma interface intuitiva e responsiva, onde os usuários podem facilmente interagir com o sistema, fazendo upload de documentos e visualizando os resumos. A renderização no lado do servidor oferecida pelo Next.js garante um desempenho otimizado e uma experiência rápida para o usuário.



Em resumo, o trabalho conseguiu integrar tecnologias avançadas de NLP e desenvolvimento web em uma solução coesa, escalável e bem documentada. Esta plataforma de resumo automático de PDF tem potencial para ser aplicada em diversos contextos, como acadêmico e empresarial, auxiliando usuários a obter insights rápidos e precisos de documentos complexos. A solução apresentada oferece uma base sólida para futuras melhorias e extensões, como a adaptação para outros formatos de documentos ou a incorporação de novos modelos de NLP, consolidando o sistema como uma ferramenta poderosa para análise e compreensão de grandes volumes de informações textuais.

## <a name="_toc1198925307"></a><a name="_toc182334009"></a>**REFERÊNCIAS**


“Fine-Tune a Pretrained Model.” Huggingface.co, **HuggingFace**, huggingface.co/docs/transformers/en/training. **Accessed 10 Nov. 2024**.

csebuetnlp. “MT5-Multilingual-XLSum” Huggingface.co, **HuggingFace**, huggingface.co/csebuetnlp/mT5\_multilingual\_XLSum. **Accessed 10 Nov. 2024.**

Hasan, Tahmid, et al. “XL-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages.” ACLWeb, A**ssociation for Computational Linguistics**, 1 Aug. 2021, aclanthology.org/2021.findings-acl.413. **Accessed 10 Nov. 2024.**


[^1]: Biblioteca Python da HuggingFace
[^2]: Processamento de Linguagem Natural
[^3]: APIs são mecanismos que permitem que dois componentes de software se comuniquem usando um conjunto de definições e protocolos
[^4]: Um <a name="_int_rkju8qz9"></a>endpoint de API é o ponto de comunicação entre uma interface de programação de aplicativos (API) e um cliente.
[^5]: Figma é uma ferramenta de design versátil e bastante popular entre designers.