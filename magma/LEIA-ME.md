# MAGMA: códigos por bloco (GreatPages)

Cada arquivo é o código completo de um bloco de código. Para atualizar, apague o código antigo do bloco e cole o arquivo inteiro.

| Arquivo | Onde colar | O que mudou |
|---|---|---|
| `geral/cabecalho.html` | Cabeçalho em todas as páginas (Início, Sobre, Contato, Órgãos Públicos) | Azul e laranja do sublinhado do menu ajustados para as cores exatas do logo |
| `geral/rodape.html` | Rodapé em todas as páginas | Telefone final 8932 removido; Facebook adicionado; razão social "MAGMA PROJETOS E LICENCIAMENTOS LTDA."; lista de Soluções com as novas categorias; links "Sobre" e "Contatos" corrigidos (estavam quebrados); verdes da marca |
| `inicio/01-hero-video.html` | Código do vídeo do topo (Início) | Véu verde por cima do vídeo no tom da marca (o botão do WhatsApp continua no código dele, que não mudou) |
| `inicio/02-solucoes.html` | Bloco "Nossas Soluções" | Diferenciais (Conformidade, Segurança...) em negrito mais forte; verdes da marca; textos alternativos das fotos corrigidos |
| `inicio/03-projetos.html` | Bloco "Projetos em destaque" | Verdes, azul e laranja da marca |
| `inicio/04-sobre-infografico-numeros.html` | Bloco "Conhecimento técnico / Conheça nossa história" | Nova ordem: história, depois o infográfico animado das 6 etapas (as etapas entram uma a uma e cada uma tem sua cena: pino no mapa, lupa no documento, lápis traçando o projeto, carimbo aprovando, guindaste na obra e selo de aprovação; depois todas as bolinhas seguem animadas: flutuam em onda, têm uma órbita tracejada girando e repetem a sua cena em sequência, enquanto o destaque percorre as etapas), depois os números animados; botão "Conheça nossa história" agora leva para a página Sobre |
| `inicio/05-clientes.html` | Bloco "Nossos Clientes" | Verdes da marca |
| `sobre/quem-somos.html` | Página Sobre | Nova seção "Por dentro da Magma": números e mosaico de fotos com "Ver mais +", que abre a galeria ampliada; verdes da marca |
| `orgaos-publicos/orgaos-publicos.html` | Página Órgãos Públicos (/magma/orgaos-publicos) | "Atendimento à Lei de Licitações e Contratos (Lei nº 14.133/2021)" na lista do topo, na etapa "Proposta técnica" e num quadro em destaque perto do formulário, com a razão social MAGMA PROJETOS E LICENCIAMENTOS LTDA; telefone com final 8932 removido; verdes da marca. O cabeçalho e o rodapé desta página também devem ser trocados pelos de `geral/` |
| `contato/contato.html` | Página Contato | Opções de "Assunto" do formulário com as novas categorias; verdes da marca |

## Paleta (a partir do logo)

- Verde da marca `#6D9A38`: cor única de títulos, botões, textos em destaque, links, linhas e ícones
- Verde `#5F8A30`: só no efeito de passar o mouse (hover) dos botões e links
- Azul `#486BA3` e laranja `#BF5E20`: cores do logo, usadas como contraste em detalhes

## Fotos da seção "Por dentro da Magma" (página Sobre)

As fotos atuais são temporárias, tiradas do próprio site. Para trocar pelas fotos do escritório e da equipe, altere o `src` e o `data-full` de cada `<button class="mg-qs-gal-item ...">`. As 6 primeiras aparecem no mosaico (a 6ª tem o "Ver mais +"). A partir da 7ª, as fotos só aparecem na galeria ampliada: para incluir mais, copie a última linha com `mg-qs-gal-item--extra`.
