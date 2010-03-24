# This file from example for use of GNU gettext.
# Copyright (C) 2003-2006 Free Software Foundation, Inc.
# This file is in the public domain.
#
# Makefile configuration - processed by automake.

# Usually the message domain is the same as the package name.
DOMAIN = qtstuff

MSGMERGE = msgmerge
MSGMERGE_UPDATE = $(MSGMERGE) --update
MSGINIT = msginit
MSGCONV = msgconv
MSGFILTER = msgfilter
GMSGFMT = msgfmt

# This is computed as $(foreach lang, $(LINGUAS), $(srcdir)/$(lang).po)
POFILES = @POFILES@
# This is computed as $(foreach lang, $(LINGUAS), $(lang).po-update)
UPDATEPOFILES = @UPDATEPOFILES@
# This is computed as $(foreach lang, $(LINGUAS), $(lang).nop)
DUMMYPOFILES = @DUMMYPOFILES@
# This is computed as $(foreach lang, $(LINGUAS), $(srcdir)/$(lang).qm)
QMFILES = @QMFILES@

# This is computed as
# $(foreach lang, user-specified subset of $(LINGUAS), $(lang).qm)
CATALOGS = $(QMFILES)

SUFFIXES = .po .qm .sed .sin .nop .po-create .po-update

.po.qm:
	@lang=`echo $* | sed -e 's,.*/,,'`; \
	test "$(srcdir)" = . && cdcmd="" || cdcmd="cd $(srcdir) && "; \
	echo "$${cdcmd}rm -f $${lang}.qm && $(GMSGFMT) -c --qt --statistics -o $${lang}.qm $${lang}.po"; \
	cd $(srcdir) && rm -f $${lang}.qm && $(GMSGFMT) -c --qt --statistics -o t-$${lang}.qm $${lang}.po && mv t-$${lang}.qm $${lang}.qm


all-local: all-local-yes

all-local-yes: stamp-po
all-local-no:

# $(srcdir)/$(DOMAIN).pot is only created when needed. When xgettext finds no
# internationalized messages, no $(srcdir)/$(DOMAIN).pot is created (because
# we don't want to bother translators with empty POT files). We assume that
# LINGUAS is empty in this case, i.e. $(POFILES) and $(QMFILES) are empty.
# In this case, stamp-po is a nop (i.e. a phony target).

# stamp-po is a timestamp denoting the last time at which the CATALOGS have
# been loosely updated. Its purpose is that when a developer or translator
# checks out the package via CVS, and the $(DOMAIN).pot file is not in CVS,
# "make" will update the $(DOMAIN).pot and the $(CATALOGS), but subsequent
# invocations of "make" will do nothing. This timestamp would not be necessary
# if updating the $(CATALOGS) would always touch them; however, the rule for
# $(POFILES) has been designed to not touch files that don't need to be
# changed.
stamp-po: $(srcdir)/$(DOMAIN).pot
	test ! -f $(srcdir)/$(DOMAIN).pot || \
	  test -z "$(QMFILES)" || $(MAKE) $(QMFILES)
	@test ! -f $(srcdir)/$(DOMAIN).pot || { \
	  echo "touch stamp-po" && \
	  echo timestamp > stamp-poT && \
	  mv stamp-poT stamp-po; \
	}


# This target rebuilds a PO file if $(DOMAIN).pot has changed.
# Note that a PO file is not touched if it doesn't need to be changed.
$(POFILES): $(srcdir)/$(DOMAIN).pot
	@lang=`echo $@ | sed -e 's,.*/,,' -e 's/\.po$$//'`; \
	if test -f "$(srcdir)/$${lang}.po"; then \
	  test "$(srcdir)" = . && cdcmd="" || cdcmd="cd $(srcdir) && "; \
	  echo "$${cdcmd}$(MSGMERGE_UPDATE) $${lang}.po $(DOMAIN).pot"; \
	  cd $(srcdir) && $(MSGMERGE_UPDATE) $${lang}.po $(DOMAIN).pot; \
	else \
	  $(MAKE) $${lang}.po-create; \
	fi


install-data-local: install-data-local-yes
install-data-local-no: all-local
install-data-local-yes: all-local
	$(mkdir_p) $(DESTDIR)$(pkgdatadir)/locale
	@catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
	  cat=`basename $$cat`; \
	  if test -r $$cat; then realcat=$$cat; else realcat=$(srcdir)/$$cat; fi; \
	  $(INSTALL_DATA) $$realcat $(DESTDIR)$(pkgdatadir)/locale/$(DOMAIN)_$$cat; \
	  echo "installing $$realcat as $(DESTDIR)$(pkgdatadir)/locale/$(DOMAIN)_$$cat"; \
	done

installdirs-local: installdirs-local-yes
installdirs-local-no:
installdirs-local-yes:
	$(mkdir_p) $(DESTDIR)$(pkgdatadir)/locale

uninstall-local: uninstall-local-yes
uninstall-local-no:
uninstall-local-yes:
	catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
	  cat=`basename $$cat`; \
	  rm -f $(DESTDIR)$(pkgdatadir)/locale/$(DOMAIN)_$$cat; \
	done

html ID:

MOSTLYCLEANFILES =
MOSTLYCLEANFILES += stamp-poT
MOSTLYCLEANFILES += core core.* *.stackdump $(DOMAIN).po $(DOMAIN).1po $(DOMAIN).2po *.new.po
MOSTLYCLEANFILES += *.o

MAINTAINERCLEANFILES = stamp-po $(QMFILES)

EXTRA_DIST = LINGUAS $(POFILES) $(QMFILES)

# Hidden from automake, but really activated. Works around an automake-1.5 bug.
#distdir: distdir1
distdir1:
	$(MAKE) update-po
	if test -f $(srcdir)/$(DOMAIN).pot; then \
	  for file in $(DOMAIN).pot stamp-po; do \
	    if test -f $$file; then d=.; else d=$(srcdir); fi; \
	    cp -p $$d/$$file $(distdir)/$$file || exit 1; \
	  done; \
	fi

update-po: Makefile
	test -z "$(UPDATEPOFILES)" || $(MAKE) $(UPDATEPOFILES)
	$(MAKE) update-gmo
	$(MAKE) stamp-po

# General rule for creating PO files.

.nop.po-create:
	@lang=`echo $@ | sed -e 's/\.po-create$$//'`; \
	echo "File $$lang.po does not exist. If you are a translator, you can create it through 'msginit'." 1>&2; \
	exit 1

# General rule for updating PO files.

.nop.po-update:
	@lang=`echo $@ | sed -e 's/\.po-update$$//'`; \
	tmpdir=`pwd`; \
	echo "$$lang:"; \
	test "$(srcdir)" = . && cdcmd="" || cdcmd="cd $(srcdir) && "; \
	echo "$${cdcmd}$(MSGMERGE) $$lang.po $(DOMAIN).pot -o $$lang.new.po"; \
	cd $(srcdir); \
	if $(MSGMERGE) $$lang.po $(DOMAIN).pot -o $$tmpdir/$$lang.new.po; then \
	  if cmp $$lang.po $$tmpdir/$$lang.new.po >/dev/null 2>&1; then \
	    rm -f $$tmpdir/$$lang.new.po; \
	  else \
	    if mv -f $$tmpdir/$$lang.new.po $$lang.po; then \
	      :; \
	    else \
	      echo "msgmerge for $$lang.po failed: cannot move $$tmpdir/$$lang.new.po to $$lang.po" 1>&2; \
	      exit 1; \
	    fi; \
	  fi; \
	else \
	  echo "msgmerge for $$lang.po failed!" 1>&2; \
	  rm -f $$tmpdir/$$lang.new.po; \
	fi

$(DUMMYPOFILES):

update-gmo: Makefile $(QMFILES)
	@:
