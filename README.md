# Descrição

Simples implementação de um naive bayes para classificar emails em SPAM ou HAM, inspirado no livro **Machine Learning for Hackers** de Drew Conway e John Miles White.

Este projeto foi implementado para a disciplina PMR5228 da Escola Politécnica da USP.

# Arquivos

* training_data.py - implementação de uma classe que lê os arquivos csv de treinamento e constrói dois dicionários dados pelas propriedades: *spam* e *ham*.
A chave de cada item do dicionário é uma string representando um termo e o seu valor é a ocorrência.
* classifier.py - implementa a classe **Classifier** utilizada para classificar um texto em **spam** ou **ham**. Prior padrão é 0.5. **c** é uma constante de pequeno valor utilizada para caso o termo não seja encontrado no dicionário de treino.
* test.py - le todas as mensagens das pastas **easy_ham_2**, **hard_ham**, **hard_ham_2** e **spam_2**, extrai o texto dos emails e utiliza o classificador de **classifier.py** para classificar cada mensagem. Para
cada pasta imprime a porcentagem de mensagens classificadas como SPAM e HAM.

# Utilização

Certifique-se que tenha o python 2.7.x instalado. Não funciona corretamente com o python 3.x.

No terminal, apenas execute: **python test.py**