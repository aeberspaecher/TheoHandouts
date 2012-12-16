#!/usr/bin/env python

top = '.'
out = "build"

handouts = ['Chaos', 'Mechanik-GreensFkt', 'Mechanik-Schwingungen', 'Mechanik-Kontinua',
            'EDyn-Vektoranalysis', 'EDyn-PDE', 'EDyn-Fourieranalysis']

def configure(conf):
    conf.load('tex')

    if not conf.env.PDFLATEX:
        conf.fatal("Could not find pdflatex")
    conf.recurse(handouts)

def build(bld):

    # copy simpleMath package to each directory
    for handout in handouts:
        bld(rule='cp ${SRC} ${TGT}', source='simpleMath.sty', target=handout)

    bld.add_group()

    bld.recurse(handouts)
