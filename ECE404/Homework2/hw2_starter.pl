#!/usr/bin/perl -w
use strict;

### hw2_starter.pl

##  Author:  Avi Kak (kak@purdue.edu)
##
##  Date:  January 23, 2006
##

##  This starter file illusrates the following class method of the
##  Bit::Vector class:
##
##        my $bitvec = Bit::Vector->new( N )
## 
##  This creates a bit vector that can hold N bits.  After you have
##  created a bit vector in this manner, you can read into it from
##  a buffer by
##
##        $bitvec->Block_Store( $buff )
##
##  where we assume that the $buff was filled by a call to sysread, as
##  in
##        sysread( FROM, $buff, 8 )
##
##  Note that the last arg here, 8, is for the number of BYTES to be
##  read in one go.  A bit vector created in this manner, can be displayed
##  on a terminal by
##
##        print $bitvec->toBin()

##  Each round of Feistel processing requires that the 64 bit block be
##  divided into two 32 bit blocks.  To bring this about, you have to
##  first create two separate 32 bit bitvectors by
##
##        my $LE = Bit::Vector->new(32);
##        my $RE = Bit::Vector->new(32);
##
##  Now you can use the Interval_Copy method of the Bit::Vector class
##  to read into $LE and $RE by
##
##        $LE->Interval_Copy( $vector, 0, 32, 32 );
##        $RE->Interval_Copy( $vector, 0, 0, 32 );

##  To remember: Block_Store will store the bytes in a right to left
##  manner.  That is, the very first byte read from a file will be at
##  at the right end of the first bit vector created.  


use Bit::Vector;

open FROM, "junk.txt";
open TO, ">out.txt";
binmode( FROM );
binmode( TO );

my $buff;

sysread( FROM, $buff, 8 );
my $vector = Bit::Vector->new(64);
$vector->Block_Store( $buff );
print $vector->to_Bin(), "\n";

my $LE = Bit::Vector->new(32);
my $RE = Bit::Vector->new(32);

$LE->Interval_Copy( $vector, 0, 32, 32 );
print $LE->to_Bin(), "\n";
$RE->Interval_Copy( $vector, 0, 0, 32 );
print $RE->to_Bin(), "\n";

my @expansion_permutation = (31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0);



sub permute {
    my $vecString = shift;
    my @permute_indices = @_;
    my $newString = '';
    my @arr = split //, $vecString;
    my $size = @permute_indices;
    for (my $i=0; $i < $size; $i++) {
        $newString .= $arr[ shift(@permute_indices) - 1 ];
    }
    return $newString;
}

my $LE_binary_string = $LE->to_Bin();
my $RE_binary_string = $RE->to_Bin();

my $str = permute( $RE_binary_string, @expansion_permutation );

# At this point, $str has 48 bits in it.  It now needs to
# go through a 48 bit to 32 bit substitution step as explained
# in class.  

# The following statements are merely to show how you can
# concatenate two bit strings and output the result back to
# to a file.  We will now pretend that $str has only 32 bits.

$RE = Bit::Vector->new_Bin( 32, $str );
my $out_vector = Bit::Vector->new(0);
$out_vector = $LE->Concat($RE);
print $out_vector->to_Bin(), "\n";

my $out_buff = $out_vector->Block_Read();
syswrite( TO, $out_buff, 8 );
