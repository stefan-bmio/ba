# Erzeugung von Bildern mittels neuronaler Netze

Dieses Repository ist Bestandteil der Abschlussarbeit des Studiums Medieninformatik Online. Es beinhaltet die praktischen Arbeiten und Ergebnisse der Experimente.

In den Verzeichnissen befinden sich Dateien und Unterverzeichnisse aus verschiedenen Quellen. Die Tabelle unten enthält Beschreibungen der Verzeichnisinhalte und Quellenangaben. Quellen, die in der schriftlichen Arbeit zitiert werden, sind mit der entsprechenden Literaturverzeichnisnummer in eckigen Klammern versehen (Beispiel: Chollet [3]).

## Verzeichnisse

Die Verzeichnisse enthalten Literatur, Eingabedaten, ausführbaren Code und Ergebnisse der Experimente.

<table>
  <tr><th>Verzeichnis</th><th>Beschreibung</th><th>Inhalt</th><th>Quelle bzw. Autor</th><th>Erwähnungen</th></tr>

  <tr><td rowspan="3"><code>HED</code></td><td rowspan="3">Implementierung der Holistically-Nested Edge Detection</td><td><code>1.jpg</code></td><td><a href="https://www-old.emt.tugraz.at/~pinz/data/GRAZ_02/">TU Graz</a> (bike.zip, bike_171.bmp)</td><td rowspan="3">2, 16</td></tr>
  <tr><td><code>deploy.prototxt</code></td><td><a href="https://github.com/s9xie/hed/blob/master/examples/hed/deploy.prototxt">GitHub s9xie/hed</a></td></tr>
  <tr><td><code>main.py</code></td><td><a href="https://github.com/opencv/opencv/blob/master/samples/dnn/edge_detection.py">GitHub opencv/opencv</a></td></tr>

  <tr><td rowspan="5"><code>NST</code></td><td rowspan="5">Implementierung des Neural Style Transfer</td><td><code>main.py</code></td><td><a href="https://github.com/tensorflow/docs/blob/master/site/en/tutorials/generative/style_transfer.ipynb">GitHub tensorflow/docs</a></td><td rowspan="5">4, 16</td></tr>
  <tr><td><code>fog.jpg</code>, <code>style_fog.png</code></td><td><a href="https://cdn.britannica.com/76/179676-138-DF4D600A/Overview-fog-forms.jpg">Britannica</a></td></tr>
  <tr><td><code>orig.png</code></td><td><a href="https://commons.wikimedia.org/wiki/File:Neckertal_20150527-6384.jpg">Julia Leijola</a></td></tr>
  <tr><td><code>stylized_image.png</code></td><td><a href="https://commons.wikimedia.org/w/index.php?curid=42812335">Alexander Gardner</a>&nbsp;/<br/>Stefan Berger</td></tr>
  <tr><td><code>fog1.png</code>, <code>fog2.png</code></td><td>Stefan Berger</td></tr>

  <tr><td rowspan="5"><code>PIX2PIX</code></td><td rowspan="5">Beispielimplementierung&nbsp;1 der Image-To-Image-Translation</td><td><code>tools</code><code>main.py</code></td><td><a href="https://github.com/affinelayer/pix2pix-tensorflow">GitHub affinelayer/<br/>pix2pix&#8209;tensorflow</a></td><td rowspan="5">16</td></tr>
  <tr><td><code>main1.py</code></td><td><a href="https://github.com/affinelayer/pix2pix-tensorflow/blob/master/pix2pix.py">GitHub affinelayer/<br/>pix2pix&#8209;tensorflow</a>&nbsp;/ Stefan Berger</td></tr>
  <tr><td><pre>│└─ mappings<br/>│ └─ candles<br/>│  └─ 21</pre></td><td><a href="https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/simplified;tab=objects?prefix=candle&forceOnObjectsSortingFiltering=false&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22candle_5C_22_22%257D%255D%22))">quick draw candles</a> (Konvertierung nach JPG: Stefan Berger)</td></tr>
  <tr><td><pre>│└─ mappings<br/>│ └─ tables<br/>│  └─ 11_4<br/>│  └─ 15_0<br/>│  └─ 36_4</td></pre><td><a href="https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/simplified;tab=objects?prefix=table&forceOnObjectsSortingFiltering=false&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22table_5C_22_22%257D%255D%22))">quick draw tables</a> (Konvertierung nach JPG: Stefan Berger)</td></tr>
  <tr><td><pre>│└─ mappings<br/>│ └─ candles<br/>│  └─ 21b<br/>│  └─ random_candle26.jpg<br/>│ └─ tables<br/>│  └─ 11_4b<br/>│  └─ 15_0b<br/>│  └─ 36_4b<br/>│  └─ combined11_4<br/>│  └─ combined15_0<br/>│  └─ combined36_4<br/>│  └─ random_table11_render4.png<br/>│  └─ random_table15_render0.png<br/>│  └─ random_table36_render4.png<br/>│└─ result</pre></td><td>Stefan Berger</td></tr>

  <tr><td rowspan="2"><code>PIX2PIX_keras</code></td><td rowspan="2">Beispielimplementierung&nbsp;2 der Image-To-Image-Translation</td><td><code>results</code>, <code>model.png</code></td><td>Stefan Berger</td><td rowspan="2">16, 20, 29, 48</td></tr>
  <tr><td><code>main.py</code></td><td><a href="https://github.com/tensorflow/docs/blob/master/site/en/tutorials/generative/pix2pix.ipynb">GitHub tensorflow/docs</a> /<br/>Stefan Berger</td></tr>

  <tr><td rowspan="14"><code>bib</code></td><td rowspan="14">PDF-Dokumente verwendeter Literatur</td><td><code>1502.03167batchnorm.pdf</code></td><td><a href="https://arxiv.org/pdf/1502.03167.pdf">Ioffe, Szegedy</a> [17]</td><td>13</td></tr>
  <tr><td><code>1505.04597unet.pdf</code></td><td><a href="https://arxiv.org/pdf/1505.04597.pdf">Ronneberger et al.</a> [16]</td><td>12</td></tr>
  <tr><td><code>1511.06434v1unsuperv&#8230;sentation.pdf</code></td><td><a href="https://arxiv.org/pdf/1511.06434v1.pdf">Radford et al.</a> [13]</td><td>4</td></tr>
  <tr><td><code>1512.03385deepresidual.pdf</code></td><td><a href="https://arxiv.org/pdf/1512.03385.pdf">He et al.</a> [18]</td><td>14</td></tr>
  <tr><td><code>1611.07004pix2pix.pdf</code></td><td><a href="https://arxiv.org/pdf/1611.07004.pdf">Isola et al.</a> [1]</td><td>2, 4, 12, 20</td></tr>
  <tr><td><code>CUDA by Example an&#8230;Programming.pdf</code></td><td><a href="https://www.researchgate.net/publication/292148642_Cuda_by_Example_An_Introduction_To_Genera_Purpose_GPU_Programming">Sanders, Kandrot</a> [21]</td><td>19</td></tr>
  <tr><td><code>Deep Learning with Pyt&#8230;Edition.pdf</code></td><td>Chollet [3]</td><td>2, 3, 7, 11, 12, 13, 20, 21</td></tr>
  <tr><td><code>Deep Learning with Python.pdf</code></td><td>Chollet</td><td></td></tr>
  <tr><td><code>Deep Learning with Ten&#8230;Edition.pdf</code></td><td><a href="https://libribook.com/ebook/getfile1/11311/MTEzMTE=">Zaccone, Karim</a> [22]</td><td>21, 23</td></tr>
  <tr><td><code>Deep Learning with Ten&#8230;ompress.pdf</code></td><td><a href="https://vdoc.pub/download/deep-learning-with-tensorflow-explore-neural-networks-with-python-7cfbalhqju40">Zaccone, Karim</a></td><td></td></tr>
  <tr><td><code>JaynesProbabilityTheory.pdf</code></td><td><a href="http://www.med.mcgill.ca/epidemiology/hanley/bios601/GaussianModel/JaynesProbabilityTheory.pdf">Jaynes</a></td><td></td></tr>
  <tr><td><code>LEARNING PYTHON POWERF&#8230;OREILLY.pdf</code></td><td><a href="https://pdfroom.com/books/learning-python-powerful-object-oriented-programming-5th-edition-oreilly/wW5mwDBYgYo">Lutz</a> [20]</td><td>18, 19</td></tr>
  <tr><td><code>Probabilistic Reason&#8230;Inference.pdf</code></td><td><a href="https://dl.acm.org/doi/pdf/10.5555/534975">Pearl</a></td><td></td></tr>
  <tr><td><code>canny1986.pdf</code></td><td><a href="https://www.cse.ust.hk/~quan/comp5421/notes/canny1986.pdf">Canny</a> [2]</td><td>2, 16</td></tr>

  <tr><td><code>blender</code></td><td colspan="2">Dateien, die bei der Erstellung der Blender-Modelle entstanden sind</td><td>Stefan Berger</td><td>16</td></tr>

  <tr><td rowspan="2"><code>canny</code></td><td rowspan="2">Canny Edge Detection Kommandozeilen-programm</td><td><code>canny.py</code></td><td>Stefan Berger</td><td rowspan="2"></td></tr>
  <tr><td>Verzeichnisse mit<br/>Eingabe- und Ergebnisbildern</td><td>Stefan Berger</td></tr>

  <tr><td><code>pdf</code></td><td colspan="2">LaTeX- und andere Quelldateien der schriftlichen Arbeit</td><td>Stefan Berger</td><td></td></tr>

  <tr><td><code>training-images</code></td><td colspan="2">Eingabedaten für die Image-To-Image-Translation</td><td>Stefan Berger</td><td></td></tr>

  <tr><td><code>video</code></td><td colspan="2">Animation und Videodokumentation der Experimente</td><td>Stefan Berger</td><td></td></tr>

</table>
