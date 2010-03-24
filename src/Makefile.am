bin_SCRIPTS = aureport-gui 

sstsupportdir = $(bindir)
sstsupport_DATA = mkbar
pkgdata_PYTHON = data_visual.py \
		htmlCreator.py \
		main.py \
		secreport.py \
		util.py
nodist_pkgdata_PYTHON = settings.py 

DISTCLEANFILES = $(CLEANFILES) 
EXTRA_DIST = settings.py.in aureport-gui.in $(sstsupport_DATA) 

settings.py: settings.py.in Makefile
	sed -e 's|@''PACKAGE''@|$(PACKAGE)|g' \
		-e 's|@''PACKAGE_VERSION''@|$(PACKAGE_VERSION)|g' \
		-e 's|@''libexecdir''@|$(libexecdir)|g' \
		-e 's|@''localedir''@|$(localedir)|g' \
		-e 's|@''pkgdatadir''@|$(pkgdatadir)|g' \
		< settings.py.in > $@

aureport-gui: aureport-gui.in Makefile
	sed -e 's|@''PYTHON''@|$(PYTHON)|g' \
		-e 's|@''SHELL''@|$(SHELL)|g' \
		-e 's|@''pkgdatadir''@|$(pkgdatadir)|g' \
		< aureport-gui.in > $@
