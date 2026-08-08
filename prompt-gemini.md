# Prompt para gerar o carro no Gemini

> **Não anexe imagem nenhuma.** Anexar joga o Gemini no modo de edição de imagem,
> que responde *“Sorry, I can't edit images for you yet”*. O estilo vai descrito
> no texto. A referência (`referencias/1-maverick-ecdwraps.jpg`) fica só para os
> nossos olhos.

**Comece uma conversa nova** e cole o texto abaixo inteiro, com a primeira linha.
É ela que manda gerar imagem — sem ela o Gemini responde como assistente de
texto e devolve código SVG desenhado por ele, que sai um rabisco inútil.

---

## Cole isto

> Gere uma imagem. Ilustração, não código, não SVG, não descrição.
>
> **O que desenhar:** um veículo UTV side-by-side esportivo, tipo Can-Am Maverick
> R, com gaiola de proteção completa, suspensão de curso longo e pneus de trilha
> agressivos. Vista lateral, de perfil, rodas no chão, nariz apontado para a
> esquerda. Proporções corretas de um UTV de verdade: entre-eixos largo, altura
> baixa em relação ao comprimento, rodas grandes.
>
> **O estilo, que é o ponto principal:** traço solto e rabiscado, como esboço a
> caneta nanquim feito por ilustrador. O carro é sugerido por riscos que se
> cruzam e se sobrepõem — **não** por um contorno único fechando a silhueta.
> Riscos de comprimento e ângulo variados, alguns passando do ponto onde a forma
> termina. A gaiola e a suspensão viram um emaranhado de linhas. As áreas de
> carroceria ficam **abertas, em branco**: o traço só marca aresta, vinco e
> sombra. Energético e gestual, mas com o veículo bem construído e claramente
> legível — é esboço de profissional, não rabisco solto.
>
> **Pneus e rodas são a exceção:** esses saem fechados e sólidos, com banda de
> rodagem cravada e aro desenhado. São o contrapeso escuro que segura o desenho.
>
> **Cor:** preto puro sobre fundo branco puro. Uma cor só. Sem cinza, sem
> meio-tom, sem gradiente, sem sombreamento pintado, sem textura, sem cor
> nenhuma. É arte para estampa de camiseta, impressa a 38 cm de largura — o risco
> mais fino precisa equivaler a 1,5 mm nesse tamanho, ou some na impressão.
>
> **Fundo:** branco puro chapado, 100% #FFFFFF. Sem cenário nenhum — sem duna,
> sem montanha, sem árvore, sem sol, sem raios, sem linha de horizonte, sem chão,
> sem sombra projetada, sem moldura, sem emblema em volta. O veículo isolado no
> branco, com margem de folga: nada encostando na borda.
>
> **Sem texto nenhum** — nenhuma palavra, nenhum logotipo, nenhuma marca d'água.
> Deixe o painel lateral e a porta lisos e limpos, sem grafismo: um adesivo vai
> ser aplicado ali depois.
>
> Composição horizontal. Alta resolução, no mínimo 3000 px de largura.

---

## Se ele responder com código SVG de novo

Não é o prompt que está errado — é a conversa, que ficou em modo texto. Mande:

> Não quero código. Gere uma imagem de verdade, renderizada.

Se insistir, abra conversa nova. Se ainda assim não gerar, a sua conta ou a sua
região não tem geração de imagem no Gemini — nesse caso vá para:

| Onde | Observação |
|---|---|
| **Google AI Studio** (`aistudio.google.com`) | Modelo de imagem do Gemini, mesmo prompt |
| **ImageFX** (`labs.google/fx`) | Ferramenta de imagem do Google, direto ao ponto |
| **ChatGPT** | Gera imagem no plano pago, mesmo prompt |

O prompt é o mesmo em qualquer uma — só apague a primeira linha nas ferramentas
que já são de imagem, porque nelas ela não faz falta.

## Se quiser a dupla em vez de um carro só

Troque o parágrafo **O que desenhar** por:

> **O que desenhar:** dois veículos UTV side-by-side esportivos, tipo Can-Am
> Maverick R, atacando a subida em alta velocidade. Um em primeiro plano à
> esquerda, maior, com o nariz erguido em diagonal. O outro atrás e acima à
> direita, menor, na mesma diagonal, como se viesse perseguindo. Poeira saindo
> dos pneus traseiros, desenhada com o mesmo traço rabiscado, sem massa preta
> fechada.

O resto continua igual. Um carro de perfil pede uma faixa mais baixa no peito; a
dupla em diagonal ocupa mais altura — as cotas de 38 × 16,6 cm que estão na ficha
são da dupla.

## Não peça o ZUX na arte

Modelos de imagem erram letra pequena — o "ZUX" volta como "ZUK", "ZIJX" ou um
borrão. Peça a lataria **limpa** e me mande o resultado: o adesivo entra depois,
com a tipografia certa, na posição certa.

## Se o resultado vier ruim

Mande a correção sozinha, na mesma conversa.

- **Veio com contorno fechado, silhueta limpa** — é o erro mais provável, porque
  é o default do modelo:
  > Refaça com traço solto e rabiscado, riscos soltos que se sobrepõem, sem
  > nenhum contorno único fechando a silhueta. Tem que parecer esboço a caneta
  > feito à mão, não vetor limpo.
- **Veio cinza ou sombreado:**
  > Só preto puro, sem cinza, sem meio-tom, sem sombreamento. Vetor chapado.
- **Veio traço fino demais:**
  > Traço mais grosso e mais firme. Risco de cabelo não sobrevive à impressão.
- **Ficou ilegível de tanto rabisco:**
  > Menos riscos. O veículo tem que continuar claramente legível, e as chapas de
  > carroceria têm que ficar abertas e brancas.
- **Veio com fundo de montanha ou duna:**
  > Refaça sem fundo nenhum. Branco puro chapado, 100% #FFFFFF, absolutamente
  > nada atrás do veículo. Sem paisagem, sem chão, sem sombra, sem moldura.
- **Veio quadriciclo em vez de side-by-side:**
  > Quatro rodas, dois bancos lado a lado, gaiola completa, volante — não é um
  > quadriciclo.
- **Veio infantil, com proporção errada** — foi o que aconteceu na primeira
  tentativa, quando ele desenhou em SVG:
  > O veículo tem que ter proporção correta de UTV de verdade: entre-eixos largo,
  > carroceria baixa em relação ao comprimento, rodas grandes e bem assentadas. É
  > esboço de ilustrador profissional, não desenho infantil.

## Versão em inglês

Costuma render melhor. Mesma regra: primeira linha manda gerar, sem anexo.

> Generate an image. An illustration — not code, not SVG, not a description.
>
> Draw one sport side-by-side UTV (Can-Am Maverick R style) with a full roll cage,
> long-travel suspension and aggressive knobby tires. Side profile view, wheels on
> the ground, nose pointing left.
>
> Style is the key: **loose sketchy hand-drawn linework**, like a pen sketch. The
> vehicle is described by overlapping crossing strokes, **not** by a single closed
> outline. Varied stroke length and angle, some strokes overshooting where the
> form ends. The roll cage and suspension read as a tangle of lines. Body panels
> stay open and white — strokes only mark edges, creases and shadow. Energetic and
> gestural but still clearly readable as a vehicle. Tires and wheels are the
> exception: solid and closed, with carved tread and drawn rims, as the dark
> counterweight.
>
> Pure black on pure white, single color. No grayscale, no halftone, no gradient,
> no painted shading, no texture, no color. This is t-shirt print art at 38 cm
> wide — the thinnest stroke must equal 1.5 mm at that size.
>
> Background: flat pure white, 100% #FFFFFF. No scenery whatsoever — no dunes, no
> mountains, no trees, no sun rays, no horizon line, no ground, no cast shadow, no
> frame, no badge. Vehicle isolated on white with margin all around; nothing
> touching the edge.
>
> No text, no lettering, no logos, no watermark. Leave the side panel and door
> clean and blank — a decal will be applied later.
>
> Horizontal composition. High resolution, minimum 3000 px wide.

## Quando a arte voltar

Me manda o arquivo. Eu recorto o fundo, aplico o adesivo ZUX na lataria, encaixo
na área do peito e atualizo a ficha e o site. Precisa vir com **2300 px de
largura no mínimo** para bater 150 dpi a 38 cm — 3000 px dá folga.
