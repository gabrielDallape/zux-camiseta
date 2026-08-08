# Prompt para gerar o carro no Gemini

> **Mudou a direção.** A arte agora é no estilo **sketcher**: o carro montado por
> traço solto e rabiscado, como o Maverick R da ECDwraps. Sai a silhueta de
> contorno fechado que o v2 usava.

## Imagens para anexar

| Imagem | Para quê |
|---|---|
| `referencias/1-maverick-ecdwraps.jpg` | Maverick R “Sketcher” — **o estilo de traço**, é a referência principal |
| `referencias/2-snowmobile-line-art.jpg` | Snowmobile das costas — **com quem a arte vai dividir a peça** |
| `referencia-composicao.png` | Como os dois veículos se posicionavam no v2, se for manter a dupla |

## Sobre a referência

O Sketcher é produto que a ECDwraps vende. Ele entra aqui como **direção de
estilo** — traçado, densidade, ângulo do risco. O desenho tem que sair do zero
para a ZUX; pedir uma cópia do wrap deles é o que não pode.

## O prompt

> Crie uma ilustração vetorial em UMA COR — preto puro sobre fundo branco — para
> estampa de camiseta off-road.
>
> **Cena:** um veículo UTV side-by-side esportivo, tipo Can-Am Maverick R, com
> gaiola de proteção completa, suspensão de curso longo e pneus de trilha
> agressivos. Vista lateral, de perfil, parado, rodas no chão, nariz para a
> esquerda.
>
> **Estilo — é o ponto principal:** desenho de **traço solto e rabiscado**, tipo
> esboço a caneta. O carro é sugerido por riscos que se cruzam e se sobrepõem,
> não por um contorno único fechando a silhueta. Riscos de comprimento e ângulo
> variados, alguns passando do ponto onde a forma termina. A gaiola e a suspensão
> viram um emaranhado de linhas. Áreas de carroceria ficam **abertas, em branco**
> — o traço só marca aresta, vinco e sombra. Energético, gestual, mas ainda
> legível como carro.
>
> Preto 100% chapado. SEM cinza, SEM meio-tom, SEM gradiente, SEM sombreamento
> pintado, SEM textura, SEM cor. O peso do traço tem que aguentar impressão a
> 38 cm de largura sem sumir: risco mínimo equivalente a 1,5 mm nesse tamanho.
>
> **Pneus e rodas:** esses sim fechados e sólidos — banda de rodagem cravada,
> aro desenhado. É o contrapeso escuro que segura o desenho.
>
> **Enquadramento:** composição horizontal. Fundo branco puro. Sem cenário: sem
> duna, sem montanha, sem árvore, sem sol, sem raios, sem linha de horizonte, sem
> chão, sem moldura, sem emblema em volta. O veículo flutua isolado no branco.
>
> **Sem texto nenhum na imagem** — nenhuma palavra, nenhum logotipo, nenhuma
> marca d'água. Deixe o painel lateral e a porta lisos e limpos, sem grafismo,
> porque um adesivo será aplicado ali depois.
>
> Alta resolução, no mínimo 3000 px de largura.

## Ressalva importante: não peça o ZUX na arte

Modelos de imagem erram letra pequena — o "ZUX" volta como "ZUK", "ZIJX" ou um
borrão. Peça a lataria **limpa** e me mande o resultado: eu aplico o adesivo com
a tipografia certa, na posição certa.

## Se quiser a dupla em vez de um carro só

Troque o parágrafo **Cena** por:

> **Cena:** dois veículos UTV side-by-side esportivos, tipo Can-Am Maverick R,
> atacando a subida em alta velocidade. Um em primeiro plano à esquerda, maior,
> com o nariz erguido em diagonal. O outro atrás e acima à direita, menor, na
> mesma diagonal, como se viesse perseguindo. Poeira saindo dos pneus traseiros,
> desenhada com o mesmo traço rabiscado, sem massa preta fechada.

O resto do prompt continua igual. Um carro de perfil pede uma faixa mais baixa
no peito; a dupla em diagonal ocupa mais altura. **Isso ainda não está decidido**
— ver a seção 05 da ficha.

## Quando ele insiste em botar fundo

Mande esta correção, sozinha, na mesma conversa:

> Refaça a mesma imagem, mas **sem fundo nenhum**.
>
> O fundo tem que ser branco puro chapado, 100% #FFFFFF, sem absolutamente nada
> atrás do veículo. Sem paisagem, sem duna, sem montanha, sem morro, sem céu,
> sem sol, sem raios, sem nuvem, sem árvore, sem horizonte, sem chão, sem estrada.
> Sem moldura, sem borda, sem círculo, sem emblema, sem faixa, sem retângulo de
> fundo. Sem textura de papel, sem granulado, sem respingo espalhado.
>
> Sem sombra projetada no chão e sem qualquer cinza — só preto puro e branco puro,
> nada entre os dois.
>
> O veículo deve ficar **recortado e isolado**, como um adesivo colado numa folha
> branca em branco. Deixe uma margem de folga em volta: nada pode encostar na
> borda da imagem.

Se ele oferecer fundo transparente, aceite. Mas **branco puro já serve** — eu
recorto aqui, é o mesmo processo que já usei no snowmobile e no logo. O que não
dá para recortar é cenário: se vier montanha atrás, o recorte leva a montanha
junto.

## Se o resultado vier ruim

- **Veio com contorno fechado, silhueta limpa:** é o erro mais provável, porque é
  o default do modelo. Repita `loose sketchy linework, overlapping strokes, no
  single closed outline, hand-drawn ink sketch feel`.
- **Veio cinza ou sombreado:** repita `pure black only, no grayscale, no shading,
  flat vector`.
- **Veio traço fino demais:** peça `thicker strokes, bold confident marks` — traço
  de cabelo não sobrevive à plotagem.
- **Ficou ilegível de tanto rabisco:** peça `fewer strokes, keep the vehicle
  clearly readable, let the body panels stay open and white`.
- **Veio com fundo de montanha:** repita `isolated on plain white, no background
  elements whatsoever`.
- **Veio quadriciclo em vez de side-by-side:** reforce `four wheels, two seats
  side by side, full roll cage, steering wheel — not an ATV quad`.

## Versão em inglês

> Single-color vector illustration, pure black on plain white, for an off-road
> t-shirt print. One sport side-by-side UTV (Can-Am Maverick R style) with a full
> roll cage, long-travel suspension and aggressive knobby tires. Side profile
> view, standing still, wheels on the ground, nose to the left.
>
> Style is the key: **loose sketchy hand-drawn linework**, like a pen sketch. The
> vehicle is described by overlapping crossing strokes, not by a single closed
> outline. Varied stroke length and angle, some strokes overshooting where the
> form ends. The roll cage and suspension read as a tangle of lines. Body panels
> stay open and white — strokes only mark edges, creases and shadow. Energetic
> and gestural but still clearly readable as a vehicle.
>
> 100% flat black. No grayscale, no halftone, no gradient, no painted shading, no
> texture, no color. Stroke weight must survive printing at 38 cm wide — minimum
> stroke equivalent to 1.5 mm at that size. Tires and wheels are the exception:
> solid and closed, with carved tread and drawn rims, as the dark counterweight.
>
> Horizontal composition. Pure white background — no scenery, no dunes, no
> mountains, no trees, no sun rays, no horizon line, no ground, no frame, no
> badge. Vehicle isolated on white. No text, no lettering, no logos, no
> watermark. Leave the side panel and door clean and blank — a decal will be
> applied later. Minimum 3000 px wide.

## Quando a arte voltar

Me manda o arquivo. Eu recorto o fundo, aplico o adesivo ZUX, encaixo na área do
peito e atualizo a ficha e o site.
