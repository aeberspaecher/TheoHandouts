# ultimate target:
all:
	make -C EDyn-Fourieranalysis
	make -C EDyn-PDE
	make -C EDyn-Vektoranalysis
	make -C Mechanik-Schwingungen
	make -C Mechanik-GreensFkt

clean:
	make -C EDyn-Fourieranalysis clean
	make -C EDyn-PDE clean
	make -C EDyn-Vektoranalysis clean
	make -C Mechanik-Schwingungen clean
	make -C Mechanik-GreensFkt clean
