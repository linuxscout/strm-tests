#/usr/bin/sh
# Makefile - Build alyahmor tests and packages

# Current date format for versioned output folders
DATE := $(shell date +'%y.%m.%d-%H:%M')

# List of test IDs
TESTS := test0 test1 test2 test3 test4 test5 test6 test7 test8 bankquestion

# Default target
default: all

# Cleanup LaTeX artifacts
clean:
	rm -f latex/*.aux latex/*.log latex/*.pdf latex/*.toc latex/test.tex latex/correct.tex

# Empty placeholder
backup:

# Declare phony targets
.PHONY: all clean backup publish doc correct run moodle minterms $(TESTS)

# Run all tests
all: $(TESTS)

# Git push
publish:
	git push origin master

# Generate documentation
doc:
	epydoc -v --config epydoc.conf

# Rule template to generate tests
define test_template
$(1):
	@echo "Generating test: $(1)"
	python3 -m strmquiz -f config/quiz5.conf --lang="ar-en" --templates strmquiz/templates -d tex -t "$(1)" -o tests/output/test.tex
	cp tests/output/test.tex latex/test.tex
	cd latex && xelatex test-n2.tex
	mkdir -p edits/test2-$(DATE)
	cp latex/test.tex latex/test-n2.pdf latex/test-n2.tex latex/karnaugh-map.sty edits/test2-$(DATE)/
	cp latex/test.tex latex/test-n2.pdf latex/test-n2.tex latex/karnaugh-map.sty edits/

endef

# Generate one rule per test
$(foreach T,$(TESTS),$(eval $(call test_template,$(T))))

# Correction PDF generation
correct:
	python3 strm_test/get-correction.py > latex/correct.tex
	cd latex && xelatex correction-s2.tex
	mkdir -p edits/test2-$(DATE)
	cp latex/correct.tex latex/correction-s2.pdf latex/correction-s2.tex latex/karnaugh-map.sty edits/test2-$(DATE)/

# Run test against a specific CSV
test_rb:
	python3 test/quiz.py -f test/data/test1.csv

# Simple test
#test0:
#	python3 test/generate_tests.py

# Moodle export
moodle:
	python3 tests/genmoodle.py
	@echo "Result saved to tests/output/test.txt"

# Generate random minterms
minterms:
	python3 tests/gen_random_minterms.py

# Launch the GUI
run:
	python3 strm_tests_webviewer.py
