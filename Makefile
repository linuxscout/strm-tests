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
test1:test_id=test1
test2:test_id=test2
test3:test_id=test3
test4:test_id=test4
test4:minterms=5,7,13,15
test5:test_id=test5
test5:minterms=5,7,13,15:6,7,9,11,13,14:10,11,14:15
test1 test2 test3 test4 test5:
	python3 strm-test/generate_tests.py -f ../config/quiz2.conf -d tex -t "$(test_id)" -o tests/output/test.tex
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
moodle:
	cd tests; python3 genmoodle.py
	echo " result is in tests/output/test.txt"
