#/usr/bin/sh
# Build alyahmor package

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: 

# Publish to github
publish:
	git push origin master 

date=$(shell date +'%y.%m.%d-%H:%M')
doc:
	epydoc -v --config epydoc.conf
test1:no=1
test2:no=2
test3:no=3
test4:no=4
test4:minterms=15
test1 test2 test3 test4:
	python3 strm-test/generate_tests.py  --min ${minterms} -d tex -n $(no) -o tests/output/test.tex
	cp tests/output/test.tex latex/test.tex
	cd latex; xelatex  test-n°2.tex
	cp latex/test.tex edits/
	cp latex/test-n°2.pdf edits/
	cp latex/test-n°2.tex edits/
	mkdir -p edits/test2-$(date)
	cp latex/test.tex edits/test2-$(date)/
	cp latex/test-n°2.pdf edits/test2-$(date)/
	cp latex/test-n°2.tex edits/test2-$(date)/
	cp latex/karnaugh-map.sty edits/test2-$(date)/
correct:
	python3 test/get-correction.py > latex/correct.tex
	cd latex; xelatex  correction-s2.tex
	cp latex/correct.tex edits/
	cp latex/correction-s2.pdf edits/
	cp latex/correction-s2.tex edits/
	mkdir -p edits/test2-$(date)	
	cp latex/correct.tex edits/test2-$(date)/
	cp latex/correction-s2.pdf edits/test2-$(date)/
	cp latex/correction-s2.tex edits/test2-$(date)/
	cp latex/karnaugh-map.sty edits/test2-$(date)/

test_rb:
	python3  test/quiz.py  -f test/data/test1.csv 
test0:
	python3 test/generate_tests.py
#~ test1:no=1
#~ test2:no=2
#~ test3:no=3
#~ test1 test2 test3:
#~ 	python strm-test/generate_tests.py  -d tex -n $(no) -o tests/output/test.tex

