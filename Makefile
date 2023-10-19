SUBNAME = qdtools-test-data
SPEC = smartmet-$(SUBNAME)

# Installation directories
ifeq ($(origin PREFIX), undefined)
  PREFIX = /usr
else
  PREFIX = $(PREFIX)
endif
datadir = $(PREFIX)/share
mydatadir = $(datadir)/smartmet

# How to install
INSTALL_PROG = install -p -m 775
INSTALL_DATA = install -p -m 664

.PHONY: test rpm

# The rules
all: 

debug: all
release: all
profile: all

clean:

install:
	@mkdir -p $(mydatadir)/test/data/qdtools
	cp -r --preserve=timestamps data/* $(mydatadir)/test/data/qdtools/

rpm: $(SPEC).spec
	rm -f $(SPEC).tar.gz # Clean a possible leftover from previous attempt
	tar -czvf $(SPEC).tar.gz --transform "s,^,$(SPEC)/," *
	rpmbuild -tb $(SPEC).tar.gz
	rm -f $(SPEC).tar.gz
