#!/usr/bin/env sh
#

gnuplot -e """
  plot 'data.txt' using 1:2;
  replot y=3x+4;
  set term png;
  set output 'sample_gnuplot.png';
  replot;"""