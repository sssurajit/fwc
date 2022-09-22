
#cd /home/assignment/assignment1/codes
pio run
pio run -t nobuild -t upload
pdflatex ide-assignment.tex
xdg-open ide-assignment.pdf

