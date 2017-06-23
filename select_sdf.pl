use strict;
use warnings;
$/=undef;
my $i=0;
my %hash;
open(IN, '<4bkjtop3000.sdf');
open(IN1, '<ddr2.txt');
open(OUT, '>top_inhibition.sdf');
my @idnum = split('\n', <IN1>);
# print @idnum;
foreach (@idnum) {
	$hash{$_}=1;
}
my @mol = split('\$\$\$\$',<IN>);
# print $mol[1];
foreach (@mol) {   
     /IDNUMBER>\n(\w+-)(\d+)\/(\d+)/;
    my $bought = $1.$2."/".$3;
    print $bought;
    print OUT $_."\$\$\$\$" if $hash{$bought} == 1; 
    $hash{$bought} = 2 if $hash{$bought} == 1;
} 

close IN;
close OUT;