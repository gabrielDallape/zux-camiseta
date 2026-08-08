# Monta o HTML de producao em A4 e imprime em PDF pelo Chrome.
#
# As pranchas sao extraidas do index.html em vez de redesenhadas: assim cota e
# desenho no papel sao sempre os mesmos que estao no site, sem risco de um ficar
# para tras do outro.
import os
import re
import subprocess

H = r'C:\Users\gadal\Desktop\camiseta\index.html'
S = os.path.dirname(os.path.abspath(__file__))
SAIDA_HTML = os.path.join(S, 'producao.html')
SAIDA_PDF = r'C:\Users\gadal\Desktop\camiseta\arte-impressao\ZUX-camiseta-v4-producao.pdf'
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

src = open(H, encoding='utf-8').read()

defs = src[src.index('      <defs>'):src.index('      </defs>') + len('      </defs>')]
figuras = re.findall(r'<figure class="plate"[^>]*>(.*?)</figure>', src, re.S)
assert len(figuras) == 4, len(figuras)
frente, peito, costas, manga = [f.strip() for f in figuras]


def so_svg(bloco):
    # guloso de proposito: a prancha da manga tem um <svg> aninhado, o da
    # bandeira, e a busca preguicosa fecharia nele, cortando o ZUX e as cotas
    return re.search(r'<svg .*</svg>', bloco, re.S).group(0)


CSS = '''
@page { size: A4 portrait; margin: 13mm 14mm 15mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  margin: 0; background: #fff; color: #14170F;
  font: 400 9.4pt/1.5 "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.mono { font-family: "Cascadia Mono", Consolas, "Courier New", monospace; }
.pagina { page-break-after: always; }
.pagina:last-child { page-break-after: auto; }

.cabeca { display: flex; justify-content: space-between; align-items: flex-end;
  border-bottom: 1.6pt solid #14170F; padding-bottom: 5pt; margin-bottom: 13pt; }
.cabeca h1 { margin: 0; font-size: 17pt; font-weight: 800; letter-spacing: -.01em;
  text-transform: uppercase; line-height: 1.05; }
.cabeca .rev { font-family: "Cascadia Mono", Consolas, monospace; font-size: 7.6pt;
  letter-spacing: .1em; text-align: right; color: #5B6152; }

h2 { font-size: 8.4pt; font-weight: 800; letter-spacing: .14em; text-transform: uppercase;
  margin: 0 0 7pt; padding-bottom: 3pt; border-bottom: .6pt solid #B9BEAD; }
section { margin-bottom: 15pt; }
p { margin: 0 0 6pt; max-width: 60em; }

.ident { display: grid; grid-template-columns: repeat(4, 1fr); gap: .6pt;
  background: #B9BEAD; border: .6pt solid #B9BEAD; margin-bottom: 15pt; }
.ident div { background: #fff; padding: 6pt 8pt; }
.ident dt { font-family: "Cascadia Mono", Consolas, monospace; font-size: 6.4pt;
  letter-spacing: .12em; text-transform: uppercase; color: #5B6152; margin: 0 0 2pt; }
.ident dd { margin: 0; font-size: 9pt; font-weight: 600; }

table { width: 100%; border-collapse: collapse; font-size: 8.4pt; }
th, td { text-align: left; padding: 5pt 6pt; border-bottom: .5pt solid #D3D7C9;
  vertical-align: top; }
thead th { font-family: "Cascadia Mono", Consolas, monospace; font-size: 6.4pt;
  letter-spacing: .12em; text-transform: uppercase; color: #5B6152; font-weight: 400;
  border-bottom: .9pt solid #14170F; white-space: nowrap; }
td.n { font-family: "Cascadia Mono", Consolas, monospace; white-space: nowrap;
  font-variant-numeric: tabular-nums; }
tbody tr.grupo td { border-top: .9pt solid #14170F; }
td.local { font-weight: 700; white-space: nowrap; }

.pranchas { display: grid; grid-template-columns: 1fr; gap: 10pt; }
.prancha { border: .6pt solid #B9BEAD; page-break-inside: avoid; }
/* a manga e estreita e alta: solta, ela sozinha estoura a altura da pagina */
.estreita { max-width: 52mm; margin: 0 auto; }
.prancha .rot { display: flex; justify-content: space-between;
  font-family: "Cascadia Mono", Consolas, monospace; font-size: 6.6pt;
  letter-spacing: .13em; text-transform: uppercase; color: #5B6152;
  padding: 4pt 6pt; border-bottom: .6pt solid #B9BEAD; }
.prancha .rot b { color: #14170F; }
.prancha svg { display: block; width: 100%; height: auto; }
.dupla { display: grid; grid-template-columns: 1fr 1fr; gap: 10pt; align-items: start; }
.dupla-larga { display: grid; grid-template-columns: 96mm 1fr; gap: 10pt; align-items: start; }

.aviso { border: 1pt solid #A8401A; padding: 8pt 10pt; margin-bottom: 13pt; }
.aviso p { margin: 0 0 5pt; font-size: 8.6pt; }
.aviso p:last-child { margin: 0; }
.aviso b { color: #A8401A; }

ul.lista { margin: 0; padding-left: 12pt; font-size: 8.6pt; }
ul.lista li { margin-bottom: 4pt; }
.rodape { margin-top: 12pt; padding-top: 5pt; border-top: .6pt solid #B9BEAD;
  font-family: "Cascadia Mono", Consolas, monospace; font-size: 6.6pt;
  letter-spacing: .1em; text-transform: uppercase; color: #5B6152;
  display: flex; justify-content: space-between; }

/* o tecido e um objeto fisico claro; no papel ele fica branco com contorno */
svg { --fabric: #FFFFFF; --fabric-line: #14170F; --fabric-soft: #9AA08D;
      --accent: #A8401A; }
'''


def cabeca(sub):
    return ('<div class="cabeca"><h1>Camiseta ZUX Expeditions<br><span '
            'style="font-size:9.6pt;font-weight:600;letter-spacing:.06em">%s</span></h1>'
            '<div class="rev">Ficha de produção v4<br>08/08/2026<br>Medidas em cm</div></div>'
            % sub)


RODAPE = ('<div class="rodape"><span>ZUX Expeditions · camiseta v4</span>'
          '<span>gabrieldallape.github.io/zux-camiseta</span></div>')

html = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
        '<title>ZUX Expeditions — camiseta, ficha de produção v4</title>',
        '<style>%s</style></head><body>' % CSS,
        '<svg width="0" height="0" style="position:absolute" aria-hidden="true">',
        defs, '</svg>']

# ---------------------------------------------------------------- pagina 1
html.append('<div class="pagina">')
html.append(cabeca('Ficha de produção — especificação'))
html.append('''
<dl class="ident">
  <div><dt>Peça</dt><dd>Camiseta manga longa</dd></div>
  <div><dt>Base de medidas</dt><dd>M · 52 × 72 cm</dd></div>
  <div><dt>Processo</dt><dd>Plotagem na peça pronta</dd></div>
  <div><dt>Tecido</dt><dd>Liso · cor a definir</dd></div>
</dl>

<div class="aviso">
  <p><b>Confirmar a área de prensa antes de tudo.</b> O tracejado das pranchas marca
  <b>32 × 47 cm</b>, e as duas artes grandes passam disso: o carro tem <b>38 cm</b> e o
  snowmobile, <b>40 cm</b>. Se a prensa da estamparia for mesmo de 32 cm, ou as duas artes
  encolhem, ou a peça pede outro equipamento. <b>É a primeira pergunta a fazer.</b></p>
  <p><b>Duas definições ainda abertas.</b> A <b>cor do tecido</b>: precisa ser escura o bastante
  para o branco do escudo aparecer e clara o bastante para o preto da arte aparecer. E o
  <b>adesivo ZUX na lataria do carro</b>, que não tem posição nem tamanho definidos — a arte do
  peito está sem ele.</p>
  <p>Fora esses três pontos, tudo abaixo está fechado e pode ser orçado.</p>
</div>

<section>
  <h2>Estampas, posição e medida</h2>
  <table>
    <thead>
      <tr><th>Peça</th><th>Elemento</th><th>Medida</th><th>Posição</th><th>Cor</th></tr>
    </thead>
    <tbody>
      <tr class="grupo">
        <td class="local" rowspan="2">Frente</td>
        <td>Escudo ZUX Expeditions</td>
        <td class="n">10 × 10,5</td>
        <td>Peito esquerdo de quem veste. Topo <b>6 cm</b> abaixo da gola; centro do escudo
            <b>10 cm</b> à esquerda do eixo, em vista frontal à direita</td>
        <td>Preto + branco</td>
      </tr>
      <tr>
        <td>Maverick, traço sketcher</td>
        <td class="n">38 × 20,2</td>
        <td>Centrado no eixo. Topo <b>26,8 cm</b> abaixo da gola</td>
        <td>Preto</td>
      </tr>
      <tr class="grupo">
        <td class="local" rowspan="2">Costas</td>
        <td>Snowmobile</td>
        <td class="n">40 × 14,9</td>
        <td>Centrado no eixo. Topo <b>10 cm</b> abaixo da gola</td>
        <td>Preto</td>
      </tr>
      <tr>
        <td>EXPEDITIONS</td>
        <td class="n">15 × 2,4</td>
        <td>Centrado no eixo, <b>3 cm</b> abaixo da base do snowmobile</td>
        <td>Preto</td>
      </tr>
      <tr class="grupo">
        <td class="local" rowspan="2">Manga</td>
        <td>Bandeira do Brasil</td>
        <td class="n">12 × 8,4</td>
        <td>Centrada na manga, <b>12 cm</b> abaixo da linha da cava</td>
        <td>Cores oficiais</td>
      </tr>
      <tr>
        <td>ZUX, horizontal</td>
        <td class="n">6 de largura</td>
        <td>Centrado, <b>4,2 cm</b> abaixo da bandeira. Altura de letra ≈ 1,9 cm</td>
        <td>Preto</td>
      </tr>
    </tbody>
  </table>
</section>

<section>
  <h2>Especificação de impressão</h2>
  <table>
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Processo</td><td>Estampa localizada na peça pronta. A área plana de trabalho é de
        32 × 47 cm por face — o tracejado nas pranchas</td></tr>
      <tr><td>Cores</td><td><b>Preto chapado, uma cor só</b>, em toda a arte. Duas exceções: o
        branco do escudo e a bandeira do Brasil</td></tr>
      <tr><td>Escudo, duas chapas</td><td>A chapa preta sai <b>cheia</b>, incluindo a área que o
        branco cobre — assim um desalinho de registro não abre fresta no contorno. A chapa branca
        entra por cima, no mesmo registro</td></tr>
      <tr><td>Se for recorte de vinil</td><td>Serve. O branco do escudo vira um segundo vinil
        sobreposto; a bandeira, três cores recortadas</td></tr>
      <tr><td>Se for DTF ou transfer</td><td>Serve, e resolve escudo e bandeira em uma passada</td></tr>
      <tr><td>Arquivos</td><td>PNG com fundo transparente, no tamanho físico final, dpi real
        gravado no arquivo</td></tr>
      <tr><td>Ampliação</td><td>Os arquivos estão em pixel nativo. Se precisar ampliar, ampliar
        na estamparia — ampliar aqui não cria detalhe, só amolece o traço</td></tr>
    </tbody>
  </table>
</section>

''')
html.append(RODAPE)
html.append('</div>')

# ---------------------------------------------------------------- pagina 2
html.append('<div class="pagina">')
html.append(cabeca('Frente'))
html.append('<div class="prancha" style="margin-bottom:10pt">'
            '<div class="rot"><b>Frente</b><span>cotas em cm</span></div>%s</div>' % so_svg(frente))
html.append('<div class="dupla-larga">')
html.append('<div class="prancha"><div class="rot"><b>Detalhe do peito</b><span>ampliado</span></div>%s</div>'
            % so_svg(peito))
html.append('''<div>
  <section style="margin:0">
    <h2>Peito</h2>
    <p style="font-size:8.4pt">O escudo fica no peito <b>esquerdo de quem veste</b>. Nas pranchas,
    desenhadas em vista frontal, ele aparece à direita.</p>
    <p style="font-size:8.4pt">O tracejado é a área plana que a prensa alcança na peça pronta,
    32 × 47 cm. O traço-ponto é o eixo central.</p>
  </section>
  <section style="margin:0">
    <h2>Atenção no escudo</h2>
    <p style="font-size:8.4pt">São <b>duas chapas</b>. A preta sai cheia, incluindo a área que o
    branco cobre; a branca entra por cima, no mesmo registro. É o branco que dá miolo às letras
    ZUX e desenha olhos e dentes do lobo.</p>
  </section>
  <section style="margin:0">
    <h2>Atenção no carro</h2>
    <p style="font-size:8.4pt">A lataria está <b>limpa de propósito</b>: o adesivo ZUX ainda vai
    ser aplicado. Não imprimir antes dessa definição.</p>
  </section>
</div>''')
html.append('</div>')
html.append(RODAPE)
html.append('</div>')

# ---------------------------------------------------------------- pagina 3
html.append('<div class="pagina">')
html.append(cabeca('Costas e manga'))
html.append('<div class="prancha" style="margin-bottom:10pt">'
            '<div class="rot"><b>Costas</b><span>cotas em cm</span></div>%s</div>' % so_svg(costas))
html.append('<div class="dupla">')
html.append('<div class="prancha estreita"><div class="rot"><b>Manga</b><span>cm</span></div>%s</div>'
            % so_svg(manga))
html.append('''<div>
  <section style="margin:0 0 11pt">
    <h2>Manga</h2>
    <p style="font-size:8.4pt">Desenhada como <b>manga esquerda</b>. A bandeira de 12 cm cabe com
    folga: naquela altura a manga tem 19,4 cm de largura aberta, sobrando 3,7 cm de cada lado. O
    ZUX embaixo dela é horizontal, 6 cm de largura.</p>
  </section>
  <section style="margin:0">
    <h2>A confirmar com a confecção</h2>
    <ul class="lista">
      <li>Bandeira nas <b>duas</b> mangas ou só numa — o ZUX sai nas duas</li>
      <li>Grade de tamanhos. As cotas são do tamanho <b>M</b>; confirmar se as estampas escalam
          junto ou ficam fixas em todos os tamanhos</li>
      <li>Manga longa confirmada, ou sai também versão manga curta</li>
    </ul>
  </section>
</div>''')
html.append('</div>')
html.append(RODAPE)
html.append('</div>')

# ---------------------------------------------------------------- pagina 4
html.append('<div class="pagina">')
html.append(cabeca('Arquivos e aprovação'))
html.append('''
<section>
  <h2>Arquivos de arte</h2>
  <table>
    <thead><tr><th>Arquivo</th><th>Onde vai</th><th>Tamanho</th><th>Densidade</th></tr></thead>
    <tbody>
      <tr><td class="mono">frente-escudo-zux-10cm-chapa-preta.png</td><td>Peito esquerdo</td>
          <td class="n">10 × 10,5 cm</td><td class="n">251 dpi</td></tr>
      <tr><td class="mono">frente-escudo-zux-10cm-chapa-branca.png</td><td>Por cima da preta</td>
          <td class="n">10 × 10,5 cm</td><td class="n">251 dpi</td></tr>
      <tr><td class="mono">frente-carro-sketcher-38cm.png</td><td>Centro do peito</td>
          <td class="n">38 × 20,2 cm</td><td class="n">172 dpi</td></tr>
      <tr><td class="mono">costas-snowmobile-40cm.png</td><td>Centro das costas</td>
          <td class="n">40 × 14,9 cm</td><td class="n">238 dpi</td></tr>
      <tr><td class="mono">costas-expeditions-15cm.png</td><td>Abaixo do snowmobile</td>
          <td class="n">15 × 2,4 cm</td><td class="n">534 dpi</td></tr>
      <tr><td class="mono">— falta —</td><td>Bandeira do Brasil, manga</td>
          <td class="n">12 × 8,4 cm</td><td>Vetor, cores oficiais</td></tr>
    </tbody>
  </table>
  <p style="font-size:8pt;margin-top:6pt;color:#5B6152">Todos com fundo transparente e o dpi real
  gravado no arquivo. A densidade é medida no tamanho físico da coluna ao lado — o piso do
  processo é 150 dpi.</p>
</section>

<section>
  <h2>O que ainda falta</h2>
  <table>
    <thead><tr><th>Pendência</th><th>Quem decide</th><th>O que trava</th></tr></thead>
    <tbody>
      <tr><td><b>Cor do tecido</b></td><td>Cliente</td>
          <td>Escura o bastante para o branco do escudo aparecer, clara o bastante para o preto
              da arte aparecer</td></tr>
      <tr><td><b>Adesivo ZUX na lataria</b></td><td>Cliente + arte</td>
          <td>Posição e tamanho. A arte do peito está sem ele</td></tr>
      <tr><td>Bandeira do Brasil em vetor</td><td>Arte</td>
          <td>Cores oficiais. A 12 cm a versão completa serve, sem simplificar</td></tr>
      <tr><td>Logo ZUX em vetor</td><td>Cliente</td>
          <td>O que existe foi reconstruído de uma foto de celular. Impressão pede AI, EPS ou SVG</td></tr>
      <tr><td>Grade de tamanhos</td><td>Cliente + confecção</td>
          <td>Quantidade por tamanho, e se as estampas escalam junto ou ficam fixas</td></tr>
    </tbody>
  </table>
</section>

<section>
  <h2>Antes de mandar imprimir</h2>
  <ul class="lista">
    <li>O <b>escudo tem duas chapas</b>. Conferir se a estamparia recebeu as duas e entendeu a
        ordem: preta cheia embaixo, branca por cima, mesmo registro</li>
    <li>O <b>carro está sem o adesivo ZUX</b>. Se for imprimir assim, é decisão, não esquecimento</li>
    <li>Pedir <b>prova em uma peça</b> antes da produção. O que mais arrisca aqui é o contraste
        entre a cor do tecido e o preto da arte, e isso só a peça física resolve</li>
    <li>Resolver a <b>área de prensa</b>: carro de 38 cm e snowmobile de 40 cm contra o
        tracejado de 32 cm. Nada mais vale enquanto isso não fechar</li>
  </ul>
</section>''')
html.append(RODAPE)
html.append('</div>')

html.append('</body></html>')

open(SAIDA_HTML, 'w', encoding='utf-8').write('\n'.join(html))
print('HTML: %.0f KB' % (os.path.getsize(SAIDA_HTML) / 1024))

subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox',
                '--user-data-dir=' + os.path.join(S, 'cprof'),
                '--no-pdf-header-footer', '--print-to-pdf=' + SAIDA_PDF,
                'file:///' + SAIDA_HTML.replace('\\', '/')], check=True,
               capture_output=True)
print('PDF: %s  (%.0f KB)' % (SAIDA_PDF, os.path.getsize(SAIDA_PDF) / 1024))
