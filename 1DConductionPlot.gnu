set autoscale
set title "1D Conduction Equation Soln"
set xlabel "Node Num"
set ylabel "Temperature"
#set term dumb
set datafile separator " "

filename = "1DConductionVarK.dat"

stats filename nooutput

#show variables

set xrange [STATS_min_x : STATS_max_x]
set yrange [STATS_min_y : STATS_max_y]

file_exists = 0
file_exists = system("! test -e 1DConductionVarK.dat; echo $?")

plot_now = system("echo $PLOTNOW")
#print plot_now

if (plot_now) {
    plot filename u 1:2 w l
} else {
    print plot_now
}
bind "x" "exit gnuplot"
pause 0.05
reread