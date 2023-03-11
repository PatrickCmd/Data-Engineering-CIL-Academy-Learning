#! /bin/bash

# - The `let` statement can be used to do mathematical functions
let X=10+2*7
let Y=X+2*4
echo "X is $X"
echo "Y is $Y"

# - An arithmetic expression can be evaluated by `$[expression]` or `$((expression))`
P="$((123+20))"
echo "Answer of P is: $P"

VALUE=$[123+20]
echo "Value is: $VALUE"
