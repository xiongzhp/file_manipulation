use strict;
use warnings;
$/=undef;
my $i=0;
open(IN, '<smallmol.sdf');
open(OUT, '>smallmoln.sdf');
my @mol = split('\$\$\$\$',<IN>);
print $#mol;
foreach (@mol) {   
    $_ =~ s/\n\d+/ligand$i/;
    $i++;
    print OUT $_."\$\$\$\$"."\n";
} 

close IN;
close OUT;