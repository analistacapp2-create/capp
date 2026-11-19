# Mari'Stela Zen — site (Great Pages)

Publicação: https://marketing.agenciacapp.com.br/maristelazen

## Home — `home.html`

1. No Great Pages, abra o bloco **Mari'Stela Zen** (`#b_3673729_2_179511681424173873`).
2. Adicione um elemento **HTML** dentro dele e cole o conteúdo inteiro de `home.html`.
3. Deixe o elemento visível **também na versão mobile** do Great Pages.
4. Publique. Ao carregar, o script faz o bloco ocupar 100% da largura e crescer com o conteúdo,
   então a altura definida no editor não importa.

Se o ID do bloco mudar, troque a constante `BLOCK_ID` no início do `<script>`.

### O que dá para editar com facilidade

| O quê | Onde |
|---|---|
| Número do WhatsApp | constante `WHATSAPP` no `<script>` (e o `href` de fallback dos links `data-msz-wa`) |
| Mensagem pronta de cada botão | atributo `data-msz-wa="..."` do link (vazio = mensagem padrão de agendamento) |
| Cores e fontes | variáveis `--msz-*` no início do `<style>` |
| Imagens | URLs `cdn.jsdelivr.net/gh/analistacapp2-create/capp-maristelazen@main/...` |

Todas as classes têm o prefixo `msz-` e todo o CSS fica restrito a `#msz`, para não conflitar com o Great Pages.
