use strict;
use warnings;
# use File::Slurp;
my %hash;
$/=undef;
my $i=0;
open(IN, '<round2.sdf');
open(OUT, '>round2_selected.sdf');
my @mol = split('\$\$\$\$',<IN>);
# print $mol[1];
foreach (@mol) {   
     /IDNUMBER>\n(\w+-)(\d+)\/(\d+)/;
    my $bought = $1.$2."/".$3;

    print OUT $_."\$\$\$\$\n" if not defined $hash{$bought}; 
    $hash{$bought} = 1;

}

close IN;
close OUT;