ACLOCAL_AMFLAGS = -I m4
CONFIG_CLEAN_FILES = *.rej *.orig *.pyc *.pyo

SUBDIRS = po src qtstuff-po 
qtstuffdir = $(pkgdatadir)/locale

icondir = $(datadir)/pixmaps
icon_DATA = icons/aureport-gui.png

applicationsdir = $(datadir)/applications
applications_in_files = aureport-gui.desktop.in
applications_DATA = $(applications_in_files:.desktop.in=.desktop)
@INTLTOOL_DESKTOP_RULE@

CLEANFILES = $(applications_DATA)  
DISTCLEANFILES = $(CLEANFILES) \
	intltool-extract intltool-merge intltool-update
EXTRA_DIST = $(icon_DATA) autogen.sh aureport-gui.spec aureport-gui.desktop.in AUTHORS COPYING ChangeLog

rpm: dist
	mkdir -p rpmbuild/{SOURCES,SPECS,SRPMS,RPMS,BUILD}
	rpmbuild --define="_topdir `pwd`/rpmbuild" --nodeps -ta $(distdir).tar.gz
