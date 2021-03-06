# State Preferences for Political Agendas and Policy Position Proximity: A Computational Content Analysis Project on the United Nations General Debate Corpus

Quantitative revelations of political agents’ preferences are of substantial interest in the field ofpolitical science. In this project, we employ computational methods to perform a content analysis of the [United Nations General Debate Corpus (UNGDC)](https://doi.org/10.7910/DVN/0TJX8Y). We infer state preferences for political agendas through features embedded in text data as well as word embeddings and topic modeling, based on which we examine policy position proximity between states based on our measurement. We embed the documented statements delivered by countries into a semantic space and infer state blocs based on their policy positions represented by document vectors. We also figure out the topics that the states are concerned about over the past half-century and investigate international relations in terms of common concerns. Finaly, we evaluate the validity and reliability of our methods and results. 

## Reproducible codes and notebooks

- [Notebooks](https://github.com/luxin-tian/UNGDC/tree/master/project)

## Documentation

- [Online documentation](./paper.pdf)
  - This paper is prohibited from circulating. Viewing online is welcomed.

## Repository structure

- `/docs` folder contains:
  - the [documentation paper](./paper.pdf);
  - the [intertopic distance map](./docs/pylda_topic.html) that visualizes the results of the LDA model;
  - the `index.md` file for the github page.
- `/project` folder contains 4 jupyter notebooks:
  - Explanatory Data Analysis
  - Topic Modeling (LDA model) and Semantic Networks
  - Dynamic Topic Modeling
  - BERT Text Generation
- `/pic` folder contains the graphs of network analysis
  - 49 [networks](./pic) constructed based on the topics revealed by the LDA model and normalized mutual information score.

## Reference

- Baturo, A., Dasandi, N., Mikhaylov, S.J., 2017. Understanding state preferences with text as data: Introducing the ungeneral debate corpus. Research & Politics 4, 2053168017712821.
- Blei, D.M., Ng, A.Y., Jordan, M.I., 2003.  Latent dirichlet allocation.  Journal of machine Learning research 3, 993–1022.
- Griffiths, T.L., Steyvers, M., Tenenbaum, J.B., 2007.  Topics in semantic representation.  Psychological review 114,211.
- Gurciullo, S., Mikhaylov, S., 2017. Topology analysis of international networks based on debates in the united nations.arXiv preprint arXiv:1707.09491.
- Jankin Mikhaylov, S., Baturo, A., Dasandi, N., 2017.  United Nations General Debate Corpus.  URL:https://doi.org/10.7910/DVN/0TJX8Y, doi:10.7910/DVN/0TJX8Y.
- Maaten, L.v.d., Hinton, G., 2008. Visualizing data using t-sne. Journal of machine learning research 9, 2579–2605.
- Mikolov, T., Chen, K., Corrado, G., Dean, J., 2013. Efficient estimation of word representations in vector space. arXivpreprint arXiv:1301.3781.
- Plan, M., . Marshall plan. Public law 80, 472.27

[website](http://luxintian.com/UNGDC/)
