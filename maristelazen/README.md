# Mari'Stela Zen — site (Great Pages)

Publicação: https://marketing.agenciacapp.com.br/maristelazen

## Home — `home.html`

1. No Great Pages, abra o bloco **Mari'Stela Zen** (`#b_3673729_2_179511681424173873`).
2. Adicione um elemento **HTML** dentro dele e cole o conteúdo inteiro de `home.html`.
3. Deixe o elemento visível **também na versão mobile** do Great Pages.
4. Publique. Ao carregar, o script faz o bloco ocupar 100% da largura e crescer com o conteúdo,
   então a altura definida no editor não importa.

Se o ID do bloco mudar, troque a constante `BLOCK_ID` no início do `<script>`.

## Sobre — `sobre.html`

Publicação: https://marketing.agenciacapp.com.br/maristelazen/sobre

Mesmo procedimento: um elemento **HTML** no bloco da página, com o conteúdo inteiro de `sobre.html`
(visível também no mobile). O script **detecta o bloco sozinho** (`BLOCK_ID` vazio); se preferir fixar,
coloque o ID do bloco em `BLOCK_ID`.

Imagens novas desta página vêm do Great Pages (`files.greatpages.com.br/images/67944/...`); a galeria
reaproveita as fotos da Home.

## Código compartilhado entre as páginas

As duas páginas usam o **mesmo `<script id="msz-script">`** (só muda o `BLOCK_ID`) e os mesmos tokens de CSS.
Ao corrigir algo no script ou nos estilos base, aplique nas duas. Os links entre páginas usam o endereço
completo (`https://marketing.agenciacapp.com.br/maristelazen...`); os do menu que apontam para seções da Home
(`#msz-areas`, `#msz-procedimentos`, `#msz-contato`) posicionam a seção logo abaixo do cabeçalho.

### O que dá para editar com facilidade

| O quê | Onde |
|---|---|
| Número do WhatsApp | constante `WHATSAPP` no `<script>` (e o `href` de fallback dos links `data-msz-wa`) |
| Mensagem pronta de cada botão | atributo `data-msz-wa="..."` do link (vazio = mensagem padrão de agendamento) |
| Cores e fontes | variáveis `--msz-*` no início do `<style>` |
| Imagens | URLs `cdn.jsdelivr.net/gh/analistacapp2-create/capp-maristelazen@main/...` |

### Animações (reaproveitáveis nas próximas páginas)

Basta colocar o atributo no elemento; `style="--d:.2s"` define o atraso.

| Atributo | Efeito |
|---|---|
| `data-reveal` | desabrocha: sobe de leve, sai do desfoque e ganha opacidade |
| `data-reveal="words"` | título surge palavra por palavra |
| `data-reveal="petal"` | card pousa como pétala (leve inclinação) |
| `data-reveal="photo"` | foto se abre do centro para as bordas |
| `data-reveal="grow"` | flor decorativa brota de baixo para cima e depois balança devagar |
| `data-reveal="flower"` | ornamento de flor (`svg.msz-flower`) abre pétala por pétala |

Os ícones de linha se desenham sozinhos ao aparecer.

**Modo de movimento.** Se o computador estiver com "reduzir movimento" ligado (no Windows: *Configurações > Acessibilidade >
Efeitos visuais > Efeitos de animação* desligado), a página entra no **modo suave**: tudo continua surgindo com fade e
desfoque, mas sem deslocamentos, pétalas ou balanço. Para ver o **modo completo** em qualquer máquina, abra a página com
`?msz-motion=full` no fim do link. O console do navegador (F12) mostra qual modo está ativo.

**Execução garantida.** Se o Great Pages inserir o código sem rodar o `<script>`, a imagem invisível no fim do arquivo
o executa (uma única vez).

Todas as classes têm o prefixo `msz-` e todo o CSS fica restrito a `#msz`, para não conflitar com o Great Pages.
