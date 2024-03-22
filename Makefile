#/usr/bin/sh
# Build alyahmor package

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: test1 test2 test3 test4 test5 test6 test8 bank

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
test5:test_id=test5
test6:test_id=test6
test7:test_id=test7
test8:test_id=test8
bank:test_id=bankquestion
test1 test2 test3 test4 test5 test6 test7 test8 bank:
	python3 generate_tests.py -f config/quiz3.conf -d tex -t "$(test_id)" -o tests/output/test.tex
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
minterms:
	python3 tests/gen_random_minterms.py

run:
	python3 strm_tests_webviewer.py 

format=json
#~ format=text
#~ format=html
test1t:test_id=test1
test2t:test_id=test2
test3t:test_id=test3
test4t:test_id=test4
test5t:test_id=test5
test6t:test_id=test6
test7t:test_id=test7
test8t:test_id=test8
bankt:test_id=bankquestion
test1t test2t test3t test4t test5t test6t test7t test8t bankt:
#~ 	python3 generate_tests.py -f config/quiz2.conf -d $(format) -t "$(test_id)" -o tests/output/test.text
	python3 generate_tests.py -f config/quiz2.conf -d json -t "$(test_id)" -o tests/output/test.html
#~ 	python3 generate_tests.py -f config/quiz2.conf -d html -t "$(test_id)" -o tests/output/test.html
#~ 	python3 generate_tests.py -f config/quiz2.conf -d text -t "$(test_id)" -o tests/output/test.text
