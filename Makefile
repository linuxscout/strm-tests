#/usr/bin/sh
# Makefile - Build alyahmor tests and packages
SHELL := /bin/bash
.SHELLFLAGS := -e -o pipefail -c
# Current date format for versioned output folders
DATE := $(shell date +'%y.%m.%d-%H:%M')
TEX_DIR=resources/latex
GEN_DIR=tmp/edits
CONF_DIR=tests/config
# List of test IDs
TESTS := test0 test1 test2 test3 test4 test5 test6 test7 test8 test9 bankquestion
TESTSHTML := test0h test1h test2h test3h test4h test5h test6h test7h test8h test9h bankquestionh


# Default target
default: all

# Cleanup LaTeX artifacts
clean:
	rm -f $(TEX_DIR)/*.aux $(TEX_DIR)/*.log $(TEX_DIR)/*.pdf $(TEX_DIR)/*.toc $(TEX_DIR)/test.tex $(TEX_DIR)/correct.tex

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
	python3 -m strmquiz -f $(CONF_DIR)/quiz7.conf -g $(CONF_DIR)/args.6.json  --lang="ar-en" --templates templates -d tex -t "$(1)" -o tests/output/test.tex &> tmp/script.log
	cp tests/output/test.tex $(TEX_DIR)/test.tex
	cd $(TEX_DIR) && xelatex main_test.tex
	mkdir -p $(GEN_DIR)/test2-$(DATE)
	cp $(TEX_DIR)/test.tex $(TEX_DIR)/main_test.pdf $(TEX_DIR)/main_test.tex $(TEX_DIR)/karnaugh-map.sty $(GEN_DIR)/test2-$(DATE)/
	cp $(TEX_DIR)/test.tex $(TEX_DIR)/main_test.pdf $(TEX_DIR)/main_test.tex $(TEX_DIR)/karnaugh-map.sty $(GEN_DIR)/

endef

# Generate one rule per test
$(foreach T,$(TESTS),$(eval $(call test_template,$(T))))

# Correction PDF generation
correct:
	python3 strm_test/get-correction.py > $(TEX_DIR)/correct.tex
	cd $(TEX_DIR) && xelatex correction-s2.tex
	mkdir -p $(GEN_DIR)/test2-$(DATE)
	cp $(TEX_DIR)/correct.tex $(TEX_DIR)/correction-s2.pdf $(TEX_DIR)/correction-s2.tex $(TEX_DIR)/karnaugh-map.sty $(GEN_DIR)/test2-$(DATE)/


# Moodle export
moodle:
	python3 tests/genmoodle.py
	@echo "Result saved to tests/output/test.txt"

# Remove last character from a string
chop = $(subst $(space),,$(wordlist 1,$(call decr,$(words $(foreach c,$(1),$(c)))),$(foreach c,$(1),$(c))))



# Rule template to generate tests
test0h:TEST_ID=test0
test1h:TEST_ID=test1
test2h:TEST_ID=test2
test3h:TEST_ID=test3
test4h:TEST_ID=test4
test5h:TEST_ID=test5
test9h:TEST_ID=test9
test0h test1h test2h test3h test9h test5h test4h:
	@echo "Generating test: $(TEST_ID)"
	python3 -m strmquiz -f $(CONF_DIR)/quiz7.conf  -d html -t "$(TEST_ID)" -o tests/output/test.html
	mkdir -p $(GEN_DIR)/test2-$(DATE)
	cp tests/output/test.html $(GEN_DIR)/test2-$(DATE)/
	cp tests/output/test.html $(GEN_DIR)/

FORMAT?=tex
test0x:
	@echo "Generating test: $(TEST_ID)"
	python3 -m strmquiz -f $(CONF_DIR)/quiz7.conf  -d $(FORMAT) -t "$(TEST_ID)" -o tests/output/test.$(FORMAT)

# Generate one rule per test
$(foreach T,$(TESTSHTML),$(eval $(call test_template_html,$(T))))

# Rule template to generate tests
test0m:TEST_ID=test0
test1m:TEST_ID=test1
test2m:TEST_ID=test2
test3m:TEST_ID=test3
test4m:TEST_ID=test4
test5m:TEST_ID=test5
test9m:TEST_ID=test9
test0m test1m test2m test3m test9m test5m test4m:
	@echo "Generating test: $(TEST_ID)"
	python3 -m strmquiz -f $(CONF_DIR)/quiz7.conf -d md -t "$(TEST_ID)" -o tests/output/test.md
	mkdir -p $(GEN_DIR)/test2-$(DATE)
	cp tests/output/test.md $(GEN_DIR)/test2-$(DATE)/
	cp tests/output/test.md $(GEN_DIR)/



# Rule template to generate tests
test0t:TEST_ID=test0
test1t:TEST_ID=test1
test2t:TEST_ID=test2
test3t:TEST_ID=test3
test4t:TEST_ID=test4
test5t:TEST_ID=test5
test9t:TEST_ID=test9
test0t test1t test2t test3t test9t test5t test4t:
	@echo "Generating test: $(TEST_ID)"
	python3 -m strmquiz -f $(CONF_DIR)/quiz7.conf -g $(CONF_DIR)/args.6.json --lang="ar-en" --templates templates -d txt -t "$(TEST_ID)" -o tests/output/test.txt
	mkdir -p $(GEN_DIR)/test2-$(DATE)
	cp tests/output/test.txt $(GEN_DIR)/test2-$(DATE)/
	cp tests/output/test.txt $(GEN_DIR)/

# Generate random minterms
minterms:
	python3 tests/gen_random_minterms.py

# Launch the GUI
server:
	cd web;  uvicorn app:app --reload

test:
	pytest tests/

# Extract web strings to be translated
trans_web:
	python scripts/translation/extract_strings.py -t web/templates/ -o web/translations/translations.json

# Extract Tempalte strings to be translated
trans_templ:
	python scripts/translation/extract_strings.py -t templates/ -o templates/translations/translations.json