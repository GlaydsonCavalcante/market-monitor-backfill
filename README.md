# 🧭 Como Configurar Suas Pesquisas (Guia Rápido)

Imagine que a variável `MONITORAMENTOS` é como uma **estante cheia de caixas organizadoras**:
1. **O Nome da Caixa (O Tema):** É o assunto geral que você quer acompanhar (exemplo: `"Inteligência Artificial"`). Fica sempre do lado esquerdo antes dos dois pontos `:`.
2. **O que tem dentro da Caixa (As Palavras de Busca):** É a listinha de frases que o robô vai procurar na internet para aquele tema. Fica sempre entre colchetes `[` e `]`.

---

### ⚠️ 3 Regrinhas de Ouro para não travar o robô:
* **Aspas Duplas e Simples:** Quando quiser que o robô busque palavras grudadas na ordem exata, use aspas duplas dentro de aspas simples: `'"inteligência artificial" bancos'`.
* **Atenção às Vírgulas:** Cada frase de busca precisa terminar com uma vírgula `,` para o robô saber que a frase acabou e vem outra em seguida.
* **Não apague as chaves `{ }` nem os colchetes `[ ]`:** Eles são as divisórias das caixas!

---

### 💡 Exemplos de como o robô entende:
* `'pix "banco central"'` $\rightarrow$ Vai buscar notícias que tenham a palavra **pix** e a expressão exata **banco central**.
* `'"fraude digital" biometria'` $\rightarrow$ Vai buscar notícias que tenham a expressão **fraude digital** junto com a palavra **biometria**.
* `'segurança -"futebol"'` $\rightarrow$ O sinal de menos `-` diz: "pegue notícias de segurança, mas jogue fora se falar de futebol".
