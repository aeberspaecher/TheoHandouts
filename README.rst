Handouts zum Tutorium Theoretische Physik
=========================================

Was?
----

In diesem Repositorium befinden sich die Handouts, die ich in einem Tutorium
zur Theoretischen Physik (Vorlesungen Mechanik und Elektrodynamik) an der
Otto-von-Guericke-Universität in den Jahren 2011 und 2012 verwendet habe.
Ausführliche Handouts habe ich immer dann ausgeteilt, wenn viel Stoff in
wenig Zeit zu erledigen war. Thematisch geht es in den Handouts immer um
Methodisches.

Status
------

Die Handouts sind so mehr oder weniger erfolgreich zur Frontalbespaßung
benutzt worden - mit Ausnahme des Handouts zur Fourieranalysis. Dieses ist
in der Entwicklung und wird ganz bestimmt bald irgendwann [tm]
fertiggeschrieben.

PDFs erzeugen
-------------

Einfach

::

  make

im Hauptverzeichnis tippen.

Neu
---

Waf steht für builds zur Verfügung::

  ./waf configure
  ./waf

Das erzeugt PDFs im build-Verzeichnis ``build``.

Abhängigkeiten
--------------

Das Makefile setzt pdflatex voraus. Außerdem werden bestimmt viele
LaTeX-Pakete benutzt, die man auf jeden Fall verfügbar hat, wenn man TeXlive_
in einer Komplettinstallation benutzt.

.. _TeXlive: http://www.tug.org/texlive/

Hinweis
-------

Mein sehr nützliches, schlecht dokumentiertes `Mathe-Convenience Paket
simpleMath <https://github.com/aeberspaecher/simpleMath>`_ gibt es auch auf
Github, ist aber auch als Teil dieses Repositoriums zu finden.

Danke an ...
------------

Allerbesten Dank an `Marco Doemeland <https://github.com/DarCMenO>`_ für die
Überarbeitung der Bilder in den Elektrodynamik-Handouts!
