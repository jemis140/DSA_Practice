#!/usr/bin/perl
# File: a1q4.pl Author: Jemis Zadafiya
# Solution to question 4 of assignment 1, CSCI4152/6509 Fall 2021
use warnings;
use strict;

while(my $input = <>){
    if ($input =~ /(([a-zA-Z])([a-zA-Z0-9-=.+_]*)\@[a-zA-Z0-9]([a-zA-Z0-9-=.+_]*)\.([a-zA-Z0-9-=.+_]*)([a-zA-Z]))/){
	$input  =~ /(([a-zA-Z])([a-zA-Z0-9-=.+_]*)\@[a-zA-Z0-9]([a-zA-Z0-9-=.+_]*)\.([a-zA-Z0-9-=.+_]*)([a-zA-Z]))/gi;
	print "$1 : $input \n";
    } 
}    